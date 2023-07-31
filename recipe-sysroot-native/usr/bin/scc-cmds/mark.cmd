mark() {
       local text="# _mark $@"
       eval echo \$text  $outfile_append
}
