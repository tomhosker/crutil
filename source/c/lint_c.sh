#!/bin/sh

### This script lints all the C code in this directory, looking for both style
### issues and memory leaks.

# Local constants.
PATH_TO_HERE=$(dirname $0)
LINTING_ARGS="-Wall -Wextra -Wfloat-equal -pedantic -ansi -O2"
TEMP_FN="temp.out"

# Crash on the first error.
set -e

# Let's get cracking...
for lib in *; do
    path_to_main="$lib/main.c"
    if [ -f $path_to_main ]; then
        echo "Checking $(realpath $lib)..."
        if gcc $path_to_main -lgmp $LINTING_ARGS -o $TEMP_FN; then
            valgrind --leak-check=yes ./$TEMP_FN
            rm $TEMP_FN
        fi
    fi
done
