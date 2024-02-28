"""
This code tests the functions defined in the rust_utils module.
"""

# Source imports.
from source.rust_utils import (
    compile_rust_packages,
    get_local_rust_library,
    rusticate_int
)

###########
# TESTING #
###########

def test_compile_rust_packages():
    """ Test that this function runs, and that it returns True. """
    assert compile_rust_packages()

def test_get_local_rust_library():
    """ Test that this function runs, and that it returns True. """
    assert get_local_rust_library("hosker_primes")

def test_rusticate_int():
    """ Test that this function runs, and that it returns the correct value. """
    assert rusticate_int(0) == ([0], True)
    assert rusticate_int(1) == ([1], True)
    assert rusticate_int((2**32)-1) == ([(2**32)-1], True)
    assert rusticate_int(2**32) == ([0, 1], True)
    assert rusticate_int((2**32)+1) == ([1, 1], True)
    assert rusticate_int((2**64)+1) == ([1, 0, 1], True)
    assert rusticate_int(-(2**64)-1) == ([1, 0, 1], False)
