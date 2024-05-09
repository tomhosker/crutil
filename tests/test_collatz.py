"""
This code tests the functions defined in the Collatz module.
"""

# Source imports.
from source.collatz import (
    make_contact,
    max_collatz_steps_under,
    max_collatz_steps_under_large
)

###########
# TESTING #
###########

def test_make_contact():
    """ Test that this function runs, and that it returns True. """
    assert make_contact()

def test_max_collatz_steps_under():
    """ Test that this function runs, and returns the correct outputs. """
    assert max_collatz_steps_under(1_000_000) == 837799
    assert max_collatz_steps_under_large(1_000_000) == 837799
