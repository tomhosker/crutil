"""
This code defines some functions for working with Rust directly.
"""

# Standard imports.
import shutil
import subprocess
import traceback
import warnings
from ctypes import CDLL
from pathlib import Path

# Local constants.
PATH_OBJ_TO_EXECUTABLES_DIR = Path.home()/".hosker_rutil_executables"
PATH_OBJ_TO_RUST_PACKAGES_DIR = Path(__file__).parent/"rust"
MANIFEST_FILENAME = "Cargo.toml"
LUCKY_INT = 17
TRUE_INT = 1
FALSE_INT = 0
BITS = 32

###########
# CLASSES #
###########

class RUtilTypeMismatch(Exception):
    """ A custom exception. """

class RUtilBadBooleanInteger(Exception):
    """ A custom exception. """

#############
# FUNCTIONS #
#############

def get_so_filename(package_name):
    """ Get the executable filename for a given Rust package. """
    result = "lib"+package_name+".so"
    return result

def get_path_to_executable(package_name):
    """ Get the path to the .so file, the one adjacent to its source code, for
    a given Rust package. """
    so_filename = get_so_filename(package_name)
    result = str(PATH_OBJ_TO_EXECUTABLES_DIR/so_filename)
    return result

def compile_rust_package(path_to_package):
    """ Compile the Rust package for the given package. """
    path_obj_to_package = Path(path_to_package)
    path_to_manifest = str(path_obj_to_package/MANIFEST_FILENAME)
    package_name = path_obj_to_package.stem
    so_filename = get_so_filename(package_name)
    path_to_so_src = str(path_obj_to_package/"target"/"release"/so_filename)
    path_to_so_dst = get_path_to_executable(package_name)
    args = [
        "cargo",
        "build",
        "--manifest-path",
        path_to_manifest,
        "--release"
    ]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError:
        warnings.warn(
            "There was a problem compiling the Rust package with manifest: "+
            path_to_manifest
        )
        return False
    PATH_OBJ_TO_EXECUTABLES_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path_to_so_src, path_to_so_dst)
    return True

def compile_rust_packages():
    """ Create executables from the source code. """
    for path_obj in PATH_OBJ_TO_RUST_PACKAGES_DIR.glob("*"):
        if path_obj.is_dir():
            if not compile_rust_package(path_obj):
                return False
    return True

def get_local_rust_library(package_name):
    """ Return a Rust library in a form which Python can use. """
    path_to_executable = get_path_to_executable(package_name)
    try:
        result = CDLL(path_to_executable)
    except:
        warnings.warn(
            "There was a problem importing the Rust library with .so file: "+
            path_to_executable
        )
        return None
    return result

def make_contact_template(library):
    """ Prove that you can access the library in question. """
    try:
        library.make_contact(LUCKY_INT)
    except:
        traceback.print_exc()
        return False
    return True

def int_to_bool(integer):
    """ Convert an integer representation of a boolean into a boolean. """
    if integer == TRUE_INT:
        return True
    if integer == FALSE_INT:
        return False
    raise RUtilBadBooleanInteger("Bad boolean integer: "+str(integer))

def rusticate_int(integer: int) -> tuple[list[int], bool]:
    """ Convert a Python integer into a form that Rust can use. """
    is_non_negative = True
    if integer < 0:
        is_non_negative = False
        integer = integer*-1
    result = []
    bin_string = format(integer, "b")
    right_index = len(bin_string)
    left_index = right_index-BITS
    while left_index >= 0:
        digit_bin_string = bin_string[left_index:right_index]
        result.append(int(digit_bin_string, 2))
        left_index -= BITS
        right_index -= BITS
    if right_index > 0:
        digit_bin_string = bin_string[0:right_index]
        result.append(int(digit_bin_string, 2))
    return result, is_non_negative
