define() {
    local var=$1
    local value="$2"
    local text="# _define $var '$value'"

    # make the variable real
    eval $var="\"$value\""
    eval echo "\$text" $outfile_append
}
