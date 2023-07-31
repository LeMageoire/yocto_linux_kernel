# used in feature scripts
#    arg1: the branch name
merge()
{
    local text
    local mbranch_name=$1

    text="merge: ${mbranch_name}"

    # output to the global and branch specific queue
    eval echo "${mbranch_name}" >> "${mergequeue}"
    if [ -n "${branch_merge_queue}" ]; then
        eval echo "${mbranch_name}" >> "${branch_merge_queue}"
    fi

    # outfile_append is the meta-series
    eval echo "\$text" $outfile_append
}
