"""
This code tests the functions defined in the c_utils module.
"""

# Source imports.
from source.c_utils import compile_c_packages, get_local_c_library

###########
# TESTING #
###########

def test_compile_c_packages():
    """ Test that this function runs, and that it returns True. """
    assert compile_c_packages()

def test_get_local_c_library():
    """ Test that this function runs, and that it returns True. """
    assert get_local_c_library("combinatorics")
