# commands that are safe, and that are automatically loaded.
basename() {
    if [ -n "${basename}" ]; then
        $basename $@
    fi
}

dirname() {
    if [ -n "${dirname}" ]; then
        $dirname $@
    fi
}

cp() {
    if [ -n "${cp}" ]; then
        $cp $@
    fi
}

mkdir() {
    if [ -n "${mkdir}" ]; then
        $mkdir $@
    fi
}

sed() {
    if [ -n "${sed}" ]; then
        $sed $@
    fi
}
