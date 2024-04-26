"""
This code tests the functions defined in the primes module.
"""

# Standard imports.
import pytest

# Source imports.
from source.primes import (
    make_contact,
    is_prime,
    is_prime_i32,
    is_prime_bigint_rust,
    echo_big_integer,
    nth_prime_i32,
    nth_prime,
    MAX_PRIME_ORDINAL_I32
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
    assert is_prime_bigint_rust(10089886811898868001)
    assert not is_prime_bigint_rust(10089886811898868003)

def test_echo_bigint():
    """ Test the function returns the correct value. """
    assert echo_big_integer(2**32) == 2**32

def test_is_prime():
    """ Test the function on a couple of examples. """
    assert is_prime(188888881)
    assert not is_prime(188888882)
    assert is_prime(2907251641+(2**32))
    assert not is_prime(2907251642+(2**32))

def test_nth_prime_i32():
    """ Test the function on a couple of examples. """
    assert nth_prime_i32(10001) == 104743
    with pytest.warns(UserWarning):
        assert nth_prime_i32(MAX_PRIME_ORDINAL_I32+1) is None

def test_nth_prime():
    """ Test the function on a couple of examples. """
    assert nth_prime(10001) == 104743
    assert nth_prime(MAX_PRIME_ORDINAL_I32+1) == 2147483659
