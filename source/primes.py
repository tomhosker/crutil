"""
This code interfaces with the "primes" Rust library.
"""



# Local imports.
from .rust_utils import get_local_rust_library, make_contact_template

# Local constants.
LIB_NAME = "primes"

#############
# FUNCTIONS #
#############

def make_contact():
    """ Prove that you can access this library. """
    return make_contact_template(LIB_NAME)
