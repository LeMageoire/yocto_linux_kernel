
# $HOME/.profile* or similar files may first set $DEBUGINFOD_URLS.
# If $DEBUGINFOD_URLS is not set there, we set it from system *.url files.
# $HOME/.*rc or similar files may then amend $DEBUGINFOD_URLS.
# See also [man debuginfod-client-config] for other environment variables
# such as $DEBUGINFOD_MAXSIZE, $DEBUGINFOD_MAXTIME, $DEBUGINFOD_PROGRESS.

if [ -z "$DEBUGINFOD_URLS" ]; then
    prefix="/home/lemageoire/fsl-community-bsp/build-openrex/tmp/work/imx6qdlsabresd-poky-linux-gnueabi/linux-fslc/6.1.38+gitAUTOINC+085682f3fc-r0/recipe-sysroot-native/usr"
    debuginfod_urls=`sh -c "cat /home/lemageoire/fsl-community-bsp/build-openrex/tmp/work/imx6qdlsabresd-poky-linux-gnueabi/linux-fslc/6.1.38+gitAUTOINC+085682f3fc-r0/recipe-sysroot-native/etc/debuginfod/*.urls 2>/dev/null" | tr '\n' ' '`
    if [ -n "$debuginfod_urls" ]; then
        DEBUGINFOD_URLS="$debuginfod_urls"
        export DEBUGINFOD_URLS
    fi
    unset debuginfod_urls
    unset prefix
fi
