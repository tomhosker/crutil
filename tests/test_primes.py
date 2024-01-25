"""
This code tests the functions defined in the primes module.
"""

# Standard imports.
from time import time

# Source imports.
from source.primes import make_contact, find_nth_prime_i32

###########
# TESTING #
###########

def test_make_contact():
    """ Test that this function runs, and that it returns True. """
    assert make_contact()

def test_find_nth_prime_i32():
    """ Test that the function returns the correct answer - and rapidly. """
    start_time = time()
    assert find_nth_prime_i32(10000) == 104729
    execution_time = time()-start_time
    assert execution_time < 0.1 # In seconds.
