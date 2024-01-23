"""
This code tests the functions defined in the rust_utils module.
"""

# Source imports.
from source.rust_utils import (
    compile_rust_packages,
    get_local_rust_library,
    make_contact_template
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

def test_make_contact_template():
    """ Test that this function runs, and that it returns True. """
    assert make_contact_template("hosker_primes")
