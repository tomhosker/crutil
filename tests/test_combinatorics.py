"""
This code tests the functions defined in the combinatorics module.
"""

# Source imports.
from source.combinatorics import factorial

###########
# TESTING #
###########

def test_factorial():
    """ Test that this function runs, and returns the correct outputs. """
    assert factorial(10) == 3628800
    assert factorial(1000) # Value too large to express here.
