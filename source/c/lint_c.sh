#!/bin/sh

### This script lints all the C code in this directory.

# Local constants.
PATH_TO_HERE=$(dirname $0)
LINTING_ARGS="-lgmp -Wall -Wextra -Wfloat-equal -pedantic -ansi -O2"
TEMP_FN="temp.out"

# Let's get cracking...
for lib in "*/"; do
    path_to_main="$lib/main.c"
    if [ -f $path_to_main ]; then
        if gcc $path_to_main -lgmp $LINTING_ARGS -o $TEMP_FN; then
            rm $TEMP_FN
        fi
    fi
done
