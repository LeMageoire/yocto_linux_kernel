#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-only
#

# Kconfig symbol analsysis
#
# Copyright (C) 2018 Bruce Ashfield
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

## example:
##     KERNELVERSION=4.7-rc5 SRCARCH=x86 ARCH=x86 ./Kconfiglib/examples/symbol_why.py

import sys
import os
import glob
from collections import OrderedDict
from pathlib import Path
import textwrap

# Kconfiglib should be installed into an existing python library
# location OR a path to where the library is should be set via something
# like: PYTHONPATH="./Kconfiglib:$PYTHONPATH".
#
# But if neither of those are true, let's try and find it ourselves
#
pathname = os.path.dirname(sys.argv[0])
try:
    import kconfiglib
except ImportError:
    sys.path.append( pathname + '/Kconfiglib')
    try:
        import kconfiglib
    except ImportError:
        raise ImportError('Could not import kconfiglib, make sure it is properly installed')

import argparse
import re
import os

dotconfig = ''
ksrc = ''
verbose = ''
show_summary = False
show_vars = False
show_selected = False
show_prompt = False
show_conditions = False
show_value = False

show_redefinitions = True
show_only_mismatch = False
strict = False

parser = argparse.ArgumentParser(
                formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                description="Kconfig symbol determination")

parser.add_argument("-c", "--dotconfig",
                    help="path to the .config to load")
parser.add_argument("-s", "--ksrc",
                    help="path to the kernel source")
parser.add_argument("-v", action='store_true',
                    help="verbose")
parser.add_argument("--summary", action='store_true',
                    help="Show variable summary")
parser.add_argument("--blame", action='store_true',
                    help="perform config blame on symbol (or whole config)" )
parser.add_argument("--sanity", action='store_true',
                    help="perform config sanity on symbol (or whole config)" )
parser.add_argument("--extended", action='store_true',
                    help="output extended config information" )
parser.add_argument("--invalid", action='store_true',
                    help="process option or whole config for invalid specifications" )
parser.add_argument("--classify", action='store_true',
                    help="If present, use hardware/non-hardware classifiers to filter options" )
parser.add_argument("--mismatches", action='store_true',
                    help="Show .config values that do not match user defined values" )
parser.add_argument("--strict", action='store_true',
                    help="When checking or processing, strictly apply ARCH and other config settings (i.e. no global checking will be done)" )
parser.add_argument("-f", "--filter",
                    help="Path to a file containg a list of options to filter out of reports. Or a comma separate list of options.")
parser.add_argument("--all", action='store_true',
                    help="process all options, whether they are user set values or not" )
parser.add_argument("config", help="configuration option to check", nargs="?", default=None)
parser.add_argument('args', help="<path to .config> <path to kernel source tree>", nargs=argparse.REMAINDER)

args, unknownargs = parser.parse_known_args()

do_blame = False
do_summary = False
do_sanity = False
do_analysis = False
do_invalid = False
do_all = False
filter_file_or_list = ""
use_classifiers = False

# pull these out of args, since we want to test the variables .. and they
# can bet set by more than the command line
if args.dotconfig:
    dotconfig=args.dotconfig
if args.ksrc:
    ksrc=args.ksrc
if args.v:
    verbose=True
if args.config:
    option=args.config
else:
    option=""
if args.summary:
    do_summary=args.summary
if args.blame:
    do_blame = args.blame
if args.sanity:
    do_sanity = args.sanity
if args.extended:
    do_analysis = args.extended
if args.invalid:
    do_invalid = args.invalid
if args.mismatches:
    show_only_mismatch = args.mismatches
if args.strict:
    strict = args.strict
if args.filter:
    filter_file_or_list = args.filter
if args.all:
    do_all = args.all
if args.classify:
    use_classifiers = True


# a little extra processing, since argparse will stop at the first non
# dashed option. We take whatever is left over, check to see if all our
# options are defined .. and if they aren't we use these ones.

for opt in args.args:
    if opt == '-h' or opt == "--help":
        parser.print_help()
        sys.exit()
    elif opt == '-v':
        verbose=1
    elif opt == '--summary':
        do_summary=True
    elif re.match( "--dotconfig=*", opt):
        temp, dotconfig = opt.split('=', 2)
    elif re.match( "--ksrc=*", opt):
        temp, ksrc = opt.split('=', 2)
    else:
        if re.match( ".*\.config", opt ):
            dotconfig=opt
        elif not ksrc:
            ksrc=opt

if option and do_sanity:
    if not do_summary:
        # forcing summary on, since single variable is being prcessed
        do_summary = True

if option and do_analysis:
    if not do_summary:
        # forcing summary on, since single variable is being prcessed
        do_summary = True

if not os.path.exists( dotconfig ):
    print( "ERROR: .config '%s' does not exist" % dotconfig )
    sys.exit(1)


filter_list = []
if filter_file_or_list:
    list_of_options = []
    if os.path.exists( filter_file_or_list ):
        # open and read the options, one per line
        with open(filter_file_or_list) as fp:
            for cnt, line in enumerate(fp):
                list_of_options.append(line.rstrip())

    if not list_of_options:
        list_of_options = filter_file_or_list.split(',')

    # create a list of CONFIG_ REMOVED options
    for o in list_of_options:
        m = re.match( r"CONFIG_([^= ]+)", o)
        if m and m.group(1):
            filter_list.append( m.group(1) )
        else:
            filter_list.append( o )


# There are three required environment variables:
#  - KERNELVERSION
#  - SRCARCH
#  - ARCH
#  - srctree
#  - CC
#
# If SRCARCH isn't set, but ARCH is, we simply make SRCARCH=ARCH, but
# other missing variables are an error
#
if not os.getenv("KERNELVERSION"):
    hconfig = open( dotconfig )
    for line in hconfig:
        line = line.rstrip()
        x = re.match( "^# .*Linux/\w*\s*([0-9]*\.[0-9]*\.[0-9]*).*Kernel Configuration", line )
        if x:
            os.environ["KERNELVERSION"] = x.group(1)
            if verbose:
                print( "[INFO]: kernel version %s found in .config, if this is incorrect, set KERNELVERSION in the environement" % x.group(1) )

    if not os.getenv("KERNELVERSION"):
        os.environ["KERNELVERSION"] = "4.7"
        if verbose:
            print( "[INFO]: default kernel version 4.7 used, if this is incorrect, set KERNELVERSION in the environement" )

if not os.getenv("SRCARCH"):
    if os.getenv("ARCH"):
        os.environ["SRCARCH"] = os.getenv("ARCH")
    else:
        print( "ERROR: source arch must be set (via SRCARCH environment variable" )
        sys.exit(1)

if not os.getenv("ARCH"):
    print( "ERROR: arch must be set (via ARCH environment variable" )
    sys.exit(1)

if not os.getenv("CC"):
    os.environ["CC"] = "gcc"
    print( "[WARNING]: CC not found in environment, setting to gcc" )

if not os.getenv("LD"):
    os.environ["LD"] = "ld"
    print( "[WARNING]: LD not found in environment, setting to ld2l" )

if not ksrc:
    ksrc = "."

os.environ["srctree"] = ksrc

kconf = ksrc + "/Kconfig"
if not os.path.exists( kconf ):
    print( "ERROR: kernel source directory '%s' does not contain a top level Kconfig file" % ksrc )
    sys.exit(1)

if verbose:
    print( "[INFO]: dotconfig: " + dotconfig)
    print( "[INFO]: ksrc: " + ksrc )
    print( "[INFO]: option: " + option )
    print( "[INFO]: kernel ver: " + format(os.getenv("KERNELVERSION")) )
    print( "[INFO]: src arch: " + os.getenv("SRCARCH") )
    print( "[INFO]: arch: " + os.getenv("ARCH") )

def _is_num(name):
    # Heuristic to see if a symbol name looks like a number, for nicer output
    # when printing expressions. Things like 16 are actually symbol names, only
    # they get their name as their value when the symbol is undefined.

    try:
        int(name)
    except ValueError:
        if not name.startswith(("0x", "0X")):
            return False

        try:
            int(name, 16)
        except ValueError:
            return False

    return True

def _name_and_val_str(sc):
    # Custom symbol printer that shows the symbol value after the symbol, used
    # for the information display

    # Show the values of non-constant (non-quoted) symbols that don't look like
    # numbers. Things like 123 are actually symbol references, and only work as
    # expected due to undefined symbols getting their name as their value.
    # Showing the symbol value for those isn't helpful though.
    if isinstance(sc, kconfiglib.Symbol) and \
       not sc.is_constant and \
       not _is_num(sc.name):

        if not sc.nodes:
            # Undefined symbol reference
            return "{}(undefined/n)".format(sc.name)

        return '{}(={})'.format(sc.name, sc.str_value)

    # For other symbols, use the standard format
    return kconfiglib.standard_sc_expr_str(sc)

def _expr_str(expr):
    # Custom expression printer that shows symbol values
    return kconfiglib.expr_str(expr, _name_and_val_str)

def _split_expr_info(expr, indent):
    # Returns a string with 'expr' split into its top-level && or || operands,
    # with one operand per line, together with the operand's value. This is
    # usually enough to get something readable for long expressions. A fancier
    # recursive thingy would be possible too.
    #
    # indent:
    #   Number of leading spaces to add before the split expression.

    if len(kconfiglib.split_expr(expr, kconfiglib.AND)) > 1:
        split_op = kconfiglib.AND
        op_str = "&&"
    else:
        split_op = kconfiglib.OR
        op_str = "||"

    collected_syms = []
    s = ""
    for i, term in enumerate(kconfiglib.split_expr(expr, split_op)):

        # scan for duplicates
        if term not in collected_syms:
            collected_syms.append( term )
            s += "{}{} {}".format(" "*indent,
                              "  " if i == 0 else op_str,
                              _expr_str(term))

            # Don't bother showing the value hint if the expression is just a
            # single symbol. _expr_str() already shows its value.
            if isinstance(term, tuple):
                s += "  (={})".format(kconfiglib.TRI_TO_STR[kconfiglib.expr_value(term)])

            s += "\n"

    return s

def _direct_dep_info(sc):
    # Returns a string describing the direct dependencies of 'sc' (Symbol or
    # Choice). The direct dependencies are the OR of the dependencies from each
    # definition location. The dependencies at each definition location come
    # from 'depends on' and dependencies inherited from parent items.

    #print( "_direct_dep_info: expr_value of sc: %s" %  kconfiglib.expr_value(sc.direct_dep) )


    return 'Direct dependencies ({}={}):\n{}' \
        .format(sc.name,kconfiglib.TRI_TO_STR[kconfiglib.expr_value(sc.direct_dep)],
                _split_expr_info(sc.direct_dep, 2))

def referencing_nodes(node, sym):
    # Returns a list of all menu nodes that reference 'sym' in any of their
    # properties or property conditions

    res = []

    while node:
        if sym in node.referenced:
            res.append(node)

        if node.list:
            res.extend(referencing_nodes(node.list, sym))

        node = node.next

    return res

# from menuconfig.py
def _select_imply_info(sym,_kconf):
    # Returns a string with information about which symbols 'select' or 'imply'
    # 'sym'. The selecting/implying symbols are grouped according to which
    # value they select/imply 'sym' to (n/m/y).

    def sis(expr, val, title):
        # sis = selects/implies
        sis = [si for si in kconfiglib.split_expr(expr, kconfiglib.OR) if kconfiglib.expr_value(si) == val]
        if not sis:
            return ""

        res = title
        for si in sis:
            res += "  - {}\n".format(kconfiglib.split_expr(si, kconfiglib.AND)[0].name)
        return res + "\n"

    s = ""

    if sym.rev_dep is not _kconf.n:
        s += sis(sym.rev_dep, 2,
                 "Symbols currently y-selecting this symbol:\n")
        s += sis(sym.rev_dep, 1,
                 "Symbols currently m-selecting this symbol:\n")
        s += sis(sym.rev_dep, 0,
                 "Symbols currently n-selecting this symbol (no effect):\n")

    if sym.weak_rev_dep is not _kconf.n:
        s += sis(sym.weak_rev_dep, 2,
                 "Symbols currently y-implying this symbol:\n")
        s += sis(sym.weak_rev_dep, 1,
                 "Symbols currently m-implying this symbol:\n")
        s += sis(sym.weak_rev_dep, 0,
                 "Symbols currently n-implying this symbol (no effect):\n")

    return s

def _locs(sc):
    # Symbol/Choice.name_and_loc helper. Returns the "(defined at ...)" part of
    # the string. 'sc' is a Symbol or Choice.

    if sc.nodes:
        return "(defined at {})".format(
            ", ".join("{0.filename}:{0.linenr}".format(node)
                      for node in sc.nodes))

    return "(undefined)"


def print_conditions( config_option, conf, indent = 2, verbose = False ):
    config_option = re.sub( "CONFIG_", "", config_option )
    opt = conf.syms[config_option]


    # print( "opt: %s %s" % (type(opt), opt.str_value))
    # if isinstance( opt.direct_dep, kconfiglib.Symbol ):
    #     print( "direct dep: %s %s" % (type(opt.direct_dep), opt.direct_dep.str_value))
    # else:
    #    print( "direct dep is a tuple" )
    # print( "kconfiglib y: %s string: %s" % (kconfiglib.Kconfig.y,str(kconfiglib.Kconfig.y) ) )
    # print( "--{}--".format( opt.direct_dep ) )

    if isinstance( opt.direct_dep, kconfiglib.Symbol ) and opt.direct_dep.name == "y":
        return None


    dep_string = _direct_dep_info(opt)
    #print( "            dep string: --%s--" % dep_string )
    dep_string = dep_string.replace('\n', ' ').replace('\r', '')
    dep_string = ' '.join(dep_string.split())
    dep_string = dep_string.replace(':', ':\n       ')
    #print("Config '%s' has the following %s" % (config_option, dep_string))
    dep_string = "Config '{}' has the following {}".format( config_option, dep_string )
    dep_string_indented = textwrap.indent( dep_string, '        ' )
    print( dep_string_indented )

    depends_string=""
    refs = opt.referenced
    selected = opt.selects
    selected_names = []
    for s in selected:
        # print( "              dbg: selected: %s" % s[0].name )
        selected_names.append(s[0].name)

    #for r in refs:
    #    print( "               dbg: {} ref: {}".format(type(r),r.name))

    # XXX you are here, what are these refs ? should we be printing them ? at the
    # very least, they shouldn't be called "dependency values", since they aren't
    for s in refs:
        # this pulls out any config items that the symbol selects itself.
        # we are left with parent dependencies of the variable
        if not s.name in selected_names:
            # print( "            dbg: looking at selected name: %s" % (s.name))

            # don't bother with the default/constant value 'y', it is just
            # there as a reference.
            if s == conf.y or s == conf.n or s == conf.m:
                continue

            if not s.name:
                s.name = "choice"

            depends_string += " " + s.name + " [" + s.str_value + "]"

    # This should probably always be output
    if verbose:
        parent_deps = "Parent dependencies are:\n"
        parent_deps += "    {}".format( depends_string )
        parent_deps = textwrap.indent( parent_deps, '        ' )
        print( parent_deps )


def split_option( config_option_str ):
    option = config_option_str.rstrip( '\n' )
    opt = None
    val = None
    try:
        m = re.match( r"(CONFIG_[^= ]+)=([^ ]+.*)", option)
        opt = m.group(1)
        val = m.group(2)
    except:
        if re.search( "^#\s*CONFIG_", option ):
            # print( "option is a is not set!!! %s" % option )
            m = re.match(r"# (CONFIG_[^ ]+) is not set", option )
            if m:
                opt = m.group(1)
                val = "n"
            else:
                # this is an invalid option
                opt = "invalid option format"
                val = option

        # a fully commented line, is not an option and val ..
        elif re.search(r"^#.*$", option ):
            opt = None
            val = None

        elif re.search( r".*= *", option):
            # space after equals
            opt = "invalid option format"
            val = option
        elif re.search( r" *=", option):
            # space before equals
            opt = "invalid option format"
            val = option

    return opt,val

def blame_analysis( option, val, blame_string, mismatch, show_only_mismatch, use_classifiers = False ):
    if re.match( "^CONFIG_", option ):
        o = option
    else:
        o = "CONFIG_" + option


    o_noprefix = re.sub( "^CONFIG_", "", o )

    # temp
    # verbose = True
    if use_classifiers:
        if verbose:
            if o_noprefix in non_hw_dict:
                print( "[DBG]: option %s is non-hw %s" % (o_noprefix,non_hw_dict[o_noprefix]) )
            if o_noprefix in hw_dict:
                print( "[DBG]: option %s is hw %s" % (o_noprefix,hw_dict[o_noprefix]) )

        if (o_noprefix in non_hw_dict) and (not o_noprefix in hw_dict):
            if verbose:
                print( "[INFO]: mismatch on non-required config [%s] found (call without --classify for details)" % o_noprefix )

            return

    # if mismatch:
    #     print ("    [INFO]: value in .config doesn't match the specified value" )

    if mismatch:
        print( "    [NOTE]: '%s' last val (%s) and .config val (%s) do not match" % (o,last_val,val))

    if show_only_mismatch:
        #print( "\n{} is a mismatch: ".format(o) )
        print( "    [INFO]: %s : %s %s" % (o,val,blame_string))

    conf_str = str(conf.syms[o_noprefix])
    conf_str_indented = textwrap.indent( conf_str, '        ' )
    print( "    [INFO]: raw config text:\n\n%s\n" % conf_str_indented )

    print_conditions( o, conf, 6, True )

    # print( "deps: {}".format(conf.syms[o_noprefix].direct_dep ) )

    # print( "%s type: %s" % (o_noprefix, kconfiglib.TYPE_TO_STR[conf.syms[o_noprefix].type] ))
    # print( "%s assignable: %s" % (o_noprefix,conf.syms[o_noprefix].assignable ))

    if conf.syms[o_noprefix].assignable == ():
        print( "    [INFO]: config '%s' was set, but it wasn't assignable, check (parent) dependencies" % o )

    # TODO: in a mismatch, we should dump which symbols are selecting
    #       this one. see menuconfig.py for the code to do that.
    selected_by = _select_imply_info( conf.syms[o_noprefix],conf )
    if selected_by:
        print( "\n    [INFO]: selection details for '%s':" % (o) )
        selected_by = textwrap.indent( selected_by, '        ' )
        print( selected_by )


def config_queue_read( config_queue_file ):
    if verbose:
        print( "[INFO]: reading config.queue from: %s" % config_queue_file )

    p = Path(config_queue_file )
    frag_dir = p.parent

    # frag dict is a dictionary indexed by fragment path + name, that points
    # to a dictionary of config options -> values
    frag_dict = OrderedDict()

    # option dict is a diectionary indexed by the option name. it points to
    # a diectionary of fragment name and the value the fragment set it to.
    option_dict = OrderedDict()

    issues_dict = OrderedDict()
    issues_dict["duplicated_option"] = OrderedDict()
    issues_dict["redefined_option"] = OrderedDict()
    issues_dict["malformated_option"] = OrderedDict()


    non_hw_class_dict = OrderedDict()
    hw_class_dict = OrderedDict()
    y_or_m_dict = OrderedDict()

    try:
        p.resolve(True)
    except:
        return frag_dict,option_dict,issues_dict,hw_class_dict,non_hw_class_dict


    # There are two passes through the queue.
    #
    # First pass:
    #             - the fragments and how they are included for classification.
    #               "kconf include" ..
    #             - broad classification instructions (.kcf files)
    #
    # Second pass:
    #             - special files and their classification, this allows us to
    #               override / reclassify something that was "kconf included"
    #               a certain way.

    # first pass start
    with open(config_queue_file) as fp:
        for cnt, line in enumerate(fp):

            fragment = line.split( '#' )
            frag_name = fragment[0].rstrip()
            frag_type = fragment[1].rstrip().lstrip()

            # print("Line {}: {}".format(cnt, line))
            # print("{} Fragment: {}/{}".format(frag_type,frag_dir,frag_name))

            frag_dict[frag_name] = OrderedDict()

            frag_path = Path( str(frag_dir) + "/" + frag_name.rstrip() )
            frag_full_path = frag_path.resolve()

            frag_dirname = frag_path.parent.resolve()
            non_hardware_classification = Path( str(frag_dirname) + "/non-hardware.kcf" ).resolve()
            hardware_classification = Path( str(frag_dirname) + "/hardware.kcf" ).resolve()

            if non_hardware_classification.exists() and use_classifiers:
                if verbose:
                    print( "[DBG]: classification found: %s" % non_hardware_classification )
                with open( str(non_hardware_classification) ) as classification_file:
                    for cline in classification_file:
                        kconfig_start = Path( ksrc + "/" + cline.rstrip() )
                        if kconfig_start.exists():
                            with open( str(kconfig_start) ) as kfile:
                                for kline in kfile:
                                    m = re.match( r"^(menu).*config (\w*)", kline )
                                    if m:
                                        non_hw_class_dict[m.group(2)] = classification_file.name

                                        # being in both h/w and non-hardware leads us to results where we
                                        # can't easily silence a warning. So if we've added it to h/w we need
                                        # remove it from non-hardware. If we do it in both the hardware and
                                        # non hardware cases, the end result is that the last classification
                                        # wins, which is what we want.
                                        try:
                                            del hw_class_dict[m.group(2)]
                                        except:
                                            pass

                                    m = re.match( r"^config (\w*)", kline )
                                    if m:
                                        non_hw_class_dict[m.group(1)] = classification_file.name

                                        # being in both h/w and non-hardware leads us to results where we
                                        # can't easily silence a warning. So if we've added it to h/w we need
                                        # remove it from non-hardware. If we do it in both the hardware and
                                        # non hardware cases, the end result is that the last classification
                                        # wins, which is what we want.
                                        try:
                                            del hw_class_dict[m.group(1)]
                                        except:
                                            pass

                        # this is jut too slow, but keeping it for reference.
                        #     try:
                        #         ck = kconfiglib.Kconfig( cline.rstrip(), warn=False )
                        #     except:
                        #         ck = None
                        #     if ck:
                        #         #print( "=================== %s" % cline.rstrip() )
                        #         for c in ck.unique_defined_syms:
                        #             #print( "c: %s" % c.name )
                        #             non_hw_class_dict[c.name] = classification_file
                        #         #print( ck.unique_defined_syms )

                        else:
                            if verbose:
                                print( "[WARNING]: %s does not exist, but was a classifier" % kconfig_start )


            if hardware_classification.exists() and use_classifiers:
                if verbose:
                    print( "[DBG]: hardware classification found: %s" % hardware_classification )
                with open( str(hardware_classification) ) as classification_file:
                    for cline in classification_file:
                        kconfig_start = Path( ksrc + "/" + cline.rstrip() )
                        if kconfig_start.exists():
                            with open( str(kconfig_start) ) as kfile:
                                for kline in kfile:
                                    m = re.match( r"^(menu).*config (\w*)", kline )
                                    if m:
                                        hw_class_dict[m.group(2)] = classification_file.name

                                        # being in both h/w and non-hardware leads us to results where we
                                        # can't easily silence a warning. So if we've added it to h/w we need
                                        # remove it from non-hardware. If we do it in both the hardware and
                                        # non hardware cases, the end result is that the last classification
                                        # wins, which is what we want.
                                        try:
                                            del non_hw_class_dict[m.group(2)]
                                        except:
                                            pass

                                    m = re.match( r"^config (\w*)", kline )
                                    if m:
                                        hw_class_dict[m.group(1).rstrip()] = classification_file.name

                                        # being in both h/w and non-hardware leads us to results where we
                                        # can't easily silence a warning. So if we've added it to h/w we need
                                        # remove it from non-hardware. If we do it in both the hardware and
                                        # non hardware cases, the end result is that the last classification
                                        # wins, which is what we want.
                                        try:
                                            del non_hw_class_dict[m.group(1)]
                                        except:
                                            pass

                        else:
                            if verbose:
                                print( "[WARNING]: %s does not exist, but was a classifier" % kconfig_start )

            with open( str(frag_path) ) as config_frag:
                for cline in config_frag:
                    c,value = split_option( cline )
                    o_noprefix = ""
                    if c:
                        o_noprefix = re.sub( "^CONFIG_", "", c )
                    if c == "invalid option format":
                        if frag_name in issues_dict["malformated_option"]:
                            issues_dict["malformated_option"][frag_name].append( value )
                        else:
                            issues_dict["malformated_option"][frag_name] = [ value ]
                    elif c:
                        if frag_type == "hardware":
                            if use_classifiers:
                                # print( "            hw classification for: %s,%s" % (o_noprefix,str(frag_path)))
                                hw_class_dict[o_noprefix] = str(frag_path)
                                # we can't be both hardware and software, so we should be deleting
                                # one or the other if in both
                                try:
                                    del non_hw_class_dict[o_noprefix.rstrip()]
                                except:
                                    pass
                        elif frag_type == "non-hardware":
                            if use_classifiers:
                                # we can't be both hardware and software, so we should be deleting
                                # one or the other if in both
                                non_hw_class_dict[o_noprefix] = str(frag_path)
                                try:
                                    # print( "deleting %s from hw_class, since it is also software" % o_noprefix.rstrip() )
                                    del hw_class_dict[o_noprefix.rstrip()]
                                except:
                                    pass

                        if not c in frag_dict[frag_name]:
                            frag_dict[frag_name][c] = value
                        else:
                            if frag_name in issues_dict["duplicated_option"]:
                                issues_dict["duplicated_option"][frag_name].append( c )
                            else:
                                issues_dict["duplicated_option"][frag_name] = [ c ]

                        if not c in option_dict:
                            option_dict[c] = OrderedDict()

                        option_dict[c][frag_name] = value


    # 2nd pass start
    with open(config_queue_file) as fp:
        for cnt, line in enumerate(fp):

            fragment = line.split( '#' )
            frag_name = fragment[0].rstrip()
            frag_type = fragment[1].rstrip().lstrip()

            # print("Line {}: {}".format(cnt, line))
            # print("{} Fragment: {}/{}".format(frag_type,frag_dir,frag_name))

            frag_path = Path( str(frag_dir) + "/" + frag_name.rstrip() )
            frag_full_path = frag_path.resolve()

            frag_dirname = frag_path.parent.resolve()

            hardware_cfg = Path( str(frag_dirname) + "/hardware.cfg" ).resolve()
            non_hardware_cfg = Path( str(frag_dirname) + "/non-hardware.cfg" ).resolve()
            y_or_m = Path( str(frag_dirname) + "/y_or_m_enabled.cfg" ).resolve()

            if y_or_m.exists():
                with open( str(y_or_m) ) as classification_file:
                    for cline in classification_file:
                        m = re.match( r"(CONFIG_[^= ]+)", cline )
                        if m:
                            o_noprefix = re.sub( "^CONFIG_", "", m.group(1) )
                            y_or_m_dict[o_noprefix.rstrip()] = str(y_or_m.resolve())

            if hardware_cfg.exists() and use_classifiers:
                with open( str(hardware_cfg) ) as classification_file:
                    for cline in classification_file:
                        m = re.match( r"(CONFIG_[^= ]+)", cline )
                        if m:
                            o_noprefix = re.sub( "^CONFIG_", "", m.group(1) )
                            hw_class_dict[o_noprefix.rstrip()] = str(hardware_cfg.resolve())
                            # being in both h/w and non-hardware leads us to results where we
                            # can't easily silence a warning. So if we've added it to h/w we need
                            # remove it from non-hardware. If we do it in both the hardware and
                            # non hardware cases, the end result is that the last classification
                            # wins, which is what we want.
                            try:
                                del non_hw_class_dict[o_noprefix.rstrip()]
                            except:
                                pass

            if non_hardware_cfg.exists() and use_classifiers:
                with open( str(non_hardware_cfg) ) as classification_file:
                    for cline in classification_file:
                        m = re.match( r"(CONFIG_[^= ]+)", cline )
                        if m:
                            o_noprefix = re.sub( "^CONFIG_", "", m.group(1) )
                            non_hw_class_dict[o_noprefix.rstrip()] = str(non_hardware_cfg.resolve())
                            # being in both h/w and non-hardware leads us to results where we
                            # can't easily silence a warning. So if we've added it to h/w we need
                            # remove it from non-hardware. If we do it in both the hardware and
                            # non hardware cases, the end result is that the last classification
                            # wins, which is what we want.
                            try:
                                del hw_class_dict[o_noprefix.rstrip()]
                            except Exception as e:
                                pass



    for o in option_dict:
        fragments_defining_option = option_dict[o]
        if len( fragments_defining_option ) > 1:
            issues_dict["redefined_option"][o] = OrderedDict()
            for k in fragments_defining_option:
                issues_dict["redefined_option"][o][k] = fragments_defining_option[k]
                # val = fragments_defining_option[k]
                # print( "       - {}: {} ({})".format(o,k,val) )

    # this needs to just be captured in a class, so we can return one thing,
    # versus the growing list
    return frag_dict,option_dict,issues_dict,hw_class_dict,non_hw_class_dict,y_or_m_dict

# Create a Config object representing a Kconfig configuration. (Any number of
# these can be created -- the library has no global state.
show_errors = False
if verbose:
    show_errors = True

conf = kconfiglib.Kconfig( kconf, show_errors, show_errors )

# Load values from a .config file.
conf.load_config( dotconfig )

sym = None
if option:
    if option.startswith( "CONFIG_" ):
        option_orig = option
        option = option.replace( "CONFIG_", "" )
    else:
        option = option
        option_orig = "CONFIG_" + option

    sym = conf.syms[option]

    # make sure the option is valid:
    if option not in conf.syms:
        print("[ERROR]: config '{}' not found in the configuration".format(option))
        sys.exit(0)

    nodes = referencing_nodes(conf.top_node, conf.syms[option])
    if not nodes:
        print("[WARNING]: no references to {} found".format(option))

frag_dict,option_dict,issues_dict,hw_dict,non_hw_dict,y_or_m_dict = config_queue_read( ".kernel-meta/config.queue" )


# TODO: this should be a shared routine with the config queue reader
#       one that you pass a Kconfig file, and it returns a list of all
#       the options in it
kconfigs = glob.glob( ksrc + "/**/Kconfig*", recursive=True )
all_configs = []
for k in kconfigs:
    with open( k ) as kconfig_file:
        for kline in kconfig_file:
            m = re.match( r"^(menu).*config (\w*)", kline )
            if m:
                o_noprefix = m.group(2)
                all_configs.append( "CONFIG_" + o_noprefix.rstrip())
            m = re.match( r"^config (\w*)", kline )
            if m:
                o_noprefix = m.group(1)
                all_configs.append( "CONFIG_" + o_noprefix.rstrip())

# some defaults, until we get the command line arguments implemented
sanity = True

if option:
    if do_summary:
        print( "[INFO]: option '%s' summary:" % option )

        print( "   - raw config:\n" )
        conf_str = str(conf.syms[option])
        conf_str_indented = textwrap.indent( conf_str, '        ' )
        print( "%s" % conf_str_indented )

        print( "" )

        if option in conf.syms:
            print( "   - value in .config is: '%s'" % (conf.syms[option].str_value ))


        print("   - visibility: " + kconfiglib.TRI_TO_STR[sym.visibility])
        print("   - currently assignable values: " +
                  ", ".join([kconfiglib.TRI_TO_STR[v] for v in sym.assignable]))

        for node in sym.nodes:
            print( "   - defined at: {}:{}".format(node.filename, node.linenr))


        if option_orig in option_dict:
            print( "   - referenced by the following fragments:" )
            for f in list(option_dict[option_orig].keys()):
                f_str = "- {}".format(f)
                f_str = textwrap.indent( f, '             ' )
                print( f_str )

    if do_sanity:
        # Perform some single option specific sanity checks
        latched_value = ""
        for fragment in frag_dict:
            try:
                config_option_dict= frag_dict[fragment]
                config_val = config_option_dict[option_orig]
                if latched_value:
                    print( "   - assignment details: %s [%s] -> %s [%s]" %
                           (list(latched_value.keys())[0], list(latched_value.values())[0], fragment, config_val) )
                latched_value = { fragment : config_val }
                # print( "DBG: %s sets option %s" % (fragment, option_orig) )
            except Exception as e:
                pass
else:
    if do_sanity:
        # perform some global sanity checks, since no option was passed, or
        # continue to do them below during the processing

        # this is currently always on, so if you pass --sanity, you get the
        # redefinitions. It could be wired up to the command line in the future
        if show_redefinitions:
            # sanity #1. Show redefined config options
            first_option = True
            for o in issues_dict["redefined_option"]:

                m = re.match( r"CONFIG_([^= ]+)", o)
                if m and m.group(1):
                    testopt = m.group(1)
                    if testopt in filter_list:
                        # if the option is being filtered out, skip ..
                        continue

                fragments_defining_option = issues_dict["redefined_option"][o]
                if len( fragments_defining_option ) > 1:
                    if first_option:
                        print( "[INFO]: redefined configuration option report:\n" )
                        first_option = False
                    print( "    - option {} is defined more than once".format( o ) )
                    for k in fragments_defining_option:
                        val = fragments_defining_option[k]
                        print( "       - {} ({})".format(k,val) )

    if do_invalid:
        # sanity #2. duplicate options in a single fragment
        first_option = True
        for f in issues_dict["duplicated_option"]:
            for o in issues_dict["duplicated_option"][f]:
                m = re.match( r"CONFIG_([^= ]+)", o)
                if m and m.group(1):
                    testopt = m.group(1)
                    if testopt in filter_list:
                        # if the option is being filtered out, skip ..
                        continue

                if first_option:
                    print( "\n[INFO]: Fragments with duplicated configuration options:" )
                    first_option = False

                print( "    - fragment {} has a duplicated option: {}".format( f, o ) )


    if do_invalid:
        # sanity #3. invalid formatting of options
        first_option = True
        for f in issues_dict["malformated_option"]:
            if first_option:
                print( "\n[INFO]: Fragments with badly formatted configuration options:" )
                first_option = False

            for o in issues_dict["malformated_option"][f]:
                print( "    - fragment {} has the following issues: {}".format( f, o ) )

banner_string = "\n"
if do_analysis:
    if not option:
        #print( "[NOTE]: no specific option defined, full config analysis follows\n" )
        banner_string += "[NOTE]: no specific option defined, full config analysis follows\n"
    else:
        #print( "[NOTE]: extended configuration analysis for: %s\n" % option )
        banner_string += "[NOTE]: extended configuration analysis for: {}\n".format( option )


# gather some information on the configuration, we'll use this later
invalid_fragment_syms = list(option_dict.keys())
syms_we_think_are_in_the_config = {}
syms_user = OrderedDict()
syms_not_user = OrderedDict()

for o in conf.syms:
    try:
        invalid_fragment_syms.remove( "CONFIG_" + o )
    except:
        pass

    if conf.syms[o].user_value != None:
        syms_we_think_are_in_the_config["CONFIG_" + o] = True
        syms_user[o] = conf.syms[o]
    else:
        syms_not_user[o] = conf.syms[o]

if syms_user:
    banner_string += "[NOTE]: user selected configs:\n"

options_string = ""
for o in syms_user:
    analysis = False
    if do_analysis:
        if option:
            if option == o:
                analysis = True
        else:
            analysis = True

    if conf.syms[o].user_value != None:
        if analysis:
            options_string +=   "   - '{}' is a user set value, which resolved to: {} ({})\n".format(
                   o, conf.syms[o].user_value,conf.syms[o].str_value )

            for node in conf.syms[o].nodes:
                options_string += "       - defined at {}:{}\n".format(node.filename, node.linenr)

            if verbose or option == o:
                # only do this in verbose mode, since it takes a while .. so you need
                # to chose to wait.
                print( ".", end = " ", flush=True )
                nodes = referencing_nodes(conf.top_node, conf.syms[o])
                if not nodes:
                    options_string += "   - '{}' has no references\n".format( o )
                else:
                    options_string += "   - '{}' is referenced by ({}) Kconfigs\n".format (o,len(nodes))
                    if verbose:
                        for n in nodes:
                            n_string = str(n).split('\n')[0]
                            options_string += "           - {}\n".format( n_string )

            selected = conf.syms[o].selects
            if selected:
                options_string += "       - selected values:\n"
                for s in selected:
                    options_string += "              - {}\n".format(s[0].name)

            if conf.syms[o].rev_dep is not conf.syms[o].kconfig.n:
                options_string += "       - '{}' is selected\n".format( o )
            elif conf.syms[o].weak_rev_dep is not conf.syms[o].kconfig.n:
                options_string += "       - '{}' is implied\n".format( o )
            else:
                pass

if options_string:
    print( banner_string )
    print( options_string )

banner_string = ""
options_string = ""
if syms_not_user:
    if do_analysis and do_all:
        banner_string = "[NOTE]: calculated configs:\n\n"

for o in syms_not_user:
    analysis = False
    if do_analysis:
        if option:
            if option == o:
                analysis = True
        else:
            analysis = True

    if analysis and do_all:
        options_string += "   - '{}' was NOT in the .config, resolved value: {}\n".format(o,conf.syms[o].str_value)
        if conf.syms[o].rev_dep is not conf.syms[o].kconfig.n:
            options_string += "   - '{}' is selected\n".format( o )
        elif conf.syms[o].weak_rev_dep is not conf.syms[o].kconfig.n:
            options_string += "   - '{}' is implied\n".format( o )

if options_string:
    print( banner_string )
    print( options_string )

## TODO: rename do_analysis to do_extended to match the command line option name
if do_analysis or do_invalid:
    if not option:
        if invalid_fragment_syms:
            first_option = True
            for c in invalid_fragment_syms:
                # 2nd level check
                # "not strict" means we are checking outside of the supplied arch, and
                # other config details
                if not strict:
                    if c in all_configs:
                        continue

                if first_option:
                    print( "\n[INFO]: the following symbols were not found in the active configuration:" )
                    first_option = False

                print( "     - {}".format( c ) )
    else:
        if option in invalid_fragment_syms:
            print( "[WARNING]: option '%s' is not valid in the active configuration" % option )


syms_we_didnt_find_in_the_config = option_dict.copy()
if do_blame or show_only_mismatch:
    # print( "\n" )

    if do_blame:
        if not option:
            print( "[NOTE]: symbol blame for .config\n" )
        else:
            print( "[NOTE]: symbol blame for %s\n" % option )

    with open(dotconfig) as fp:

        config_found = False
        for cnt, line in enumerate(fp):
            blame_string = "## .config: {} :".format(cnt)
            o,val = split_option( line )
            if o:
                last_val = None
                try:
                    if option_dict[o]:
                        for f in option_dict[o]:
                            blame_string += "{} ({}) ".format(f,option_dict[o][f])
                            last_val = option_dict[o][f]
                except Exception as e:
                    # the symbol isn't in the option dict
                    pass

                o_noprefix = re.sub( "^CONFIG_", "", o )

                if not option:
                    if not show_only_mismatch:
                        print( "  %s : %s %s" % (o,val,blame_string))
                if option == o_noprefix:
                    config_found = True
                    if not show_only_mismatch:
                        print( "  %s : %s %s" % (o,val,blame_string))

                # TODO: we can test the Kconfiglib val for the symbols as well, and then
                # compare it to the .config AND last val, as another consistency check.

                deeper_check = False
                if o_noprefix == option:
                    deeper_check = True

                mismatch = False
                if last_val != None and last_val != val:
                    if option:
                        if o_noprefix == option:
                            mismatch = True
                    else:
                        mismatch = True

                if (o_noprefix in y_or_m_dict) and not strict:
                    if last_val == "y" or last_val == "m":
                        # this isn't a mismatch, since we've stated that yes or m are both
                        # fine
                        if verbose:
                            print( "[INFO]: option %s mismatch skipped, as y or m are both fine" % o_noprefix )

                        mismatch = False

                if deeper_check or mismatch:
                    blame_analysis( o, val, blame_string, mismatch, show_only_mismatch, use_classifiers )

                try:
                    # delete any option we see, whatever is left, wasn't found in the .config at all
                    # and is something we should be checking for mismatches.
                    del syms_we_didnt_find_in_the_config[o]
                except:
                    # could warn here, something is up. We just read a config value we didn't expect
                    pass

                if o in syms_we_think_are_in_the_config:
                    # this matches the list of symbols we think have user values from above, so
                    # it is sane.
                    pass
                else:
                    if do_sanity:
                        print( "[ERROR]: sanity check failed. .config contains a value that is not marked as a user specified value: %s" % o )
                        sys.exit(1)

        if option and not config_found:
            print( "    [INFO]: config '{}' was not in the .config".format(option) )
            blame_analysis( option, None, "# {} is not in .config".format(option), False, False, use_classifiers )

        if not option:
            for o in syms_we_didnt_find_in_the_config:
                o_noprefix = re.sub( "^CONFIG_", "", o )
                if o_noprefix in hw_dict:
                    # now finally, if it wasn't in the .config, but wasn't set to anything
                    # we can give that a pass (maybe add a --strict flag in the future )
                    last_val = ""
                    for f in syms_we_didnt_find_in_the_config[o]:
                        last_val = option_dict[o][f]

                    if last_val != "n":
                        if show_only_mismatch:
                            # print( "mismatch: %s [%s]" % (o,last_val))
                            # if the symbol is invalid (that's a different check, not this mismatch check, so
                            # we won't report it), then we shouldn't call blame
                            if not o in invalid_fragment_syms:
                                blame_string = ""
                                blame_analysis( o, "n", blame_string, True, show_only_mismatch, use_classifiers )
                                print( "\n" )
