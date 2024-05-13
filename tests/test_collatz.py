"""
This code tests the functions defined in the Collatz module.
"""

# Source imports.
from source.collatz import (
    make_contact,
    next_collatz_python,
    count_collatz_steps_large,
    max_collatz_steps_under,
    max_collatz_steps_under_large
)

###########
# TESTING #
###########

def test_make_contact():
    """ Test that this function runs, and that it returns True. """
    assert make_contact()

def test_next_collatz_python():
    """ Test that this function runs, and returns the correct outputs. """
    assert next_collatz_python(2) == 1
    assert next_collatz_python(3) == 10

def test_count_collatz_steps_large():
    """ Test that this function runs, and returns the correct outputs. """
    assert count_collatz_steps_large(3) == 7

def test_max_collatz_steps_under():
    """ Test that this function runs, and returns the correct outputs. """
    assert max_collatz_steps_under(1_000_000) == 837799
    assert max_collatz_steps_under_large(1_000_000) == 837799
