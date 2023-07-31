# tracks the global branch name
track_branch()
{
    local new_branch=$1

    if [ -n "${cbranch_name}" ]; then
        parent_branch="${cbranch_name}"
        cbranch_name="${cbranch_name}/${new_branch}"
    else
        cbranch_name="${new_branch}"
    fi

    if [ -n "${verbose}" ]; then
        echo "[INFO]: tracked branch is now: ${cbranch_name}" >&2
    fi
}

# used in feature scripts
#    arg1: the branch name
#    arg2: the source branch name
#    arg3 and up: flags
branch()
{
    local text

    track_branch $1

    if [ -n "${parent_branch}" ]; then
        text="branch rename: ${parent_branch} ${parent_branch}/base"
        eval echo "\$text" $outfile_append
    fi
    text="branch: ${cbranch_name}"
    eval echo "\$text" $outfile_append

    # generate branch specific queues
    branch_patch_queue="patch.$(echo ${cbranch_name} | sed 's%/%.%g').queue"
    branch_patch_queue="$(dirname ${patchqueue})/${branch_patch_queue}"

    branch_merge_queue="patch.$(echo ${cbranch_name} | sed 's%/%.%g').queue"
    branch_merge_queue="$(dirname ${patchqueue})/${branch_merge_queue}"
}
