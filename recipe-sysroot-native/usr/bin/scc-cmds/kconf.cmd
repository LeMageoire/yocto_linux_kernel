# processes .scc kconf commands of the format: kconf <type> <fragment>
#
# Not only do we process the config, the config is migrated into the source
# tree, along with any special files: hardware.cfg, non-hardware.cfg, required.cfg and optional.cfg
#
# The special files, and type of the fragment are used to generate extra information about the
# kernel configuration fragment that can be used later in an audit phase.
#
kconf() {
    local type=$1
    local frag=$2
    local flags=$3
    local text="kconf $frag # $type"
    local simple_config_name=$(basename ${frag})

    relative_config_name=${frag}
    relative_config_dir=""
    if [ -n "${prefix}" ]; then
        relative_config_name=$(echo ${relative_config_name} | sed "s%${prefix}%%")
        relative_config_dir=$(dirname ${relative_config_name})
        mkdir -p ${outdir}/configs/${cbranch_name}/${relative_config_dir}
    else
        mkdir -p ${outdir}/configs/${cbranch_name}/
    fi

    #echo "copying config: ${simple_config_name} to ${outdir}/configs/${cbranch_name}/${relative_config_dir}" >&2

    # we could compare the source and dest, and either warn or clobber, but
    # for now, we just clobber
    cp -f "$frag" "${outdir}/configs/${cbranch_name}/${relative_config_dir}"

    # if there are any classifiers in the fragment dir, we copy them as well
    frag_dir=$(dirname ${frag})
    # echo "frag dir: ${frag_dir}" >&2
    for c in ${frag_dir}/*.kcf ${frag_dir}/hardware.cfg ${frag_dir}/non-hardware.cfg ${frag_dir}/required.cfg ${frag_dir}/optional.cfg ${frag_dir}/y_or_m_enabled.cfg; do
        local simple_special_name=$(basename ${c})
        if [ -e "${c}" ]; then
            cp -f ${c} "${outdir}/configs/${cbranch_name}/${relative_config_dir}"
            # echo "c: ${c}" >&2
            # echo "relative config dir: ${relative_config_dir}"  >&2
            # echo "cbranch: ${cbranch_name}"  >&2
            # echo "outdir: ${outdir}"  >&2
            # echo "config: ${outdir}/configs/${cbranch_name}/${relative_config_dir}/${simple_special_name}" >&2
            if [ "${c}" == "${frag_dir}/non-hardware.cfg" ]; then
                echo ${outdir}/configs/${cbranch_name}/${relative_config_dir}/${simple_special_name} >> ${outdir}/non-hardware_frags.txt
            fi
            if [ "${c}" == "${frag_dir}/hardware.cfg" ]; then
                echo ${outdir}/configs/${cbranch_name}/${relative_config_dir}/${simple_special_name} >> ${outdir}/hardware_frags.txt
            fi
        fi
    done

    eval echo "configs/${cbranch_name}/${relative_config_dir}/${simple_config_name} \# ${type}" >> "${configqueue}"
    eval echo "\$text" $outfile_append

    if [ "${type}" == "hardware" ]; then
        echo "${outdir}/configs/${cbranch_name}/${relative_config_dir}/${simple_config_name}" >> ${outdir}/hardware_frags.txt
    fi
    if [ "${type}" == "non-hardware" ]; then
        echo "${outdir}/configs/${cbranch_name}/${relative_config_dir}/${simple_config_name}" >> ${outdir}/non-hardware_frags.txt
    fi
    if [ "${type}" == "required" ]; then
        echo "${outdir}/configs/${cbranch_name}/${relative_config_dir}/${simple_config_name}" >> ${outdir}/required_frags.txt
    fi
    if [ "${type}" == "optional" ]; then
        echo "${outdir}/configs/${cbranch_name}/${relative_config_dir}/${simple_config_name}" >> ${outdir}/optional_frags.txt
    fi
}
