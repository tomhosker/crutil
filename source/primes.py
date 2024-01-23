"""
This code interfaces with the "primes" Rust library.
"""

# Local imports.
from .rust_utils import get_local_rust_library, make_contact_template

# Local constants.
LIB_NAME = "hosker_primes"

#############
# FUNCTIONS #
#############

def make_contact():
    """ Prove that you can access this library. """
    return make_contact_template(LIB_NAME)

def find_nth_prime(n):
    """ Ronseal. """
    lib = get_local_rust_library(LIB_NAME)
    return lib.find_nth_prime(n)
