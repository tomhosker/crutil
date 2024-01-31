"""
This code tests the functions defined in the primes module.
"""

# Source imports.
from source.primes import (
    make_contact,
    is_prime_i32,
    is_prime_bigint,
    echo_big_integer
)

###########
# TESTING #
###########

def test_make_contact():
    """ Test that this function runs, and that it returns True. """
    assert make_contact()

def test_is_prime_i32():
    """ Test the function on a couple of examples. """
    assert is_prime_i32(188888881)
    assert not is_prime_i32(188888882)

def test_is_prime_bigint():
    """ Test the function on a couple of examples. """
    assert is_prime_bigint([2907251641, 1])
    assert not is_prime_bigint([2907251642, 1])

def test_echo_bigint():
    """ Test the function return the correct value. """
    assert echo_big_integer([0, 1]) == 2**32
