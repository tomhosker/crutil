"""
This code defines some functions for working with C directly.
"""

# Standard imports.
import subprocess
import warnings
from ctypes import CDLL
from pathlib import Path

# Local constants.
PATH_OBJ_TO_C_PACKAGES_DIR = Path(__file__).parent/"c"
MAIN_FN = "main.c"
LIB_FN = "shared.so"

#############
# FUNCTIONS #
#############

def compile_c_package_with_gmp(path_to_folder):
    """ Compile the C package contained in the given folder, using the GMP
    library for working with large integers. """
    path_obj_to_folder = Path(path_to_folder)
    path_to_main = str(path_obj_to_folder/MAIN_FN)
    path_to_lib = str(path_obj_to_folder/LIB_FN)
    args = ["gcc", path_to_main, "-lgmp", "-shared", "-o", path_to_lib]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError:
        warnings.warn(
            "There was a problem compiling the C package in folder: "+
            path_to_folder
        )
        return False
    return True

def compile_c_packages():
    """ Create executables from the source code. """
    for path_obj in PATH_OBJ_TO_C_PACKAGES_DIR.glob("*"):
        if path_obj.is_dir():
            path_to_folder = str(path_obj)
            if not compile_c_package_with_gmp(path_to_folder):
                return False
    return True

def get_local_c_library(package_name):
    """ Return a C library in a form which Python can use. """
    path_obj_to_package = PATH_OBJ_TO_C_PACKAGES_DIR/package_name
    path_to_so_file = str(path_obj_to_package/LIB_FN)
    try:
        result = CDLL(path_to_so_file)
    except:
        warnings.warn(
            "There was a problem importing the C library with .so file: "+
            path_to_so_file
        )
        return None
    return result
