"""
This code interfaces with the "primes" Rust library.
"""

# Standard imports.
import ctypes

# Local imports.
from .rust_utils import (
    RUtilTypeMismatch,
    get_local_rust_library,
    make_contact_template
)

# Local constants.
LIB_NAME = "hosker_primes"

#############
# FUNCTIONS #
#############

def make_contact():
    """ Prove that you can access this library. """
    return make_contact_template(LIB_NAME)

def check_matches_integer_type(integer, power_of_2):
    """ Check that a given integer can be represented as a Rust i32, i64,
    etc. """
    if (
        (not isinstance(integer, int)) or
        (integer < -2**power_of_2) or
        (integer >= 2**power_of_2)
    ):
        raise RUtilTypeMismatch(
            str(integer)+
            " does not represent a "+
            str(power_of_2)+
            "-bit integer."
        )

def find_nth_prime_i32(n: int) -> int:
    """ Find the nth prime, provided that n can be represented by 32 bits. """
    lib = get_local_rust_library(LIB_NAME)
    rust_func = lib.find_nth_prime_i32
    rust_func.argtypes = [ctypes.c_int32]
    rust_func.restype = ctypes.c_int32
    check_matches_integer_type(n, 32)
    return lib.find_nth_prime_i32(n)
