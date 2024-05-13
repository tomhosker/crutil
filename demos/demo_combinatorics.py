"""
This file defines a script which demonstrates the speed of the COMBINATORICS
module to a new user of this package.
"""

# Standard imports.
import math
from time import time

# Custom imports.
from crutil.combinatorics import factorial as factorial_crutil

#############
# FUNCTIONS #
#############

def demo_factorial(num):
    """ Ronseal. """
    click0 = time()
    result_python = math.factorial(num)
    click1 = time()
    result_crutil = factorial_crutil(num)
    click2 = time()
    python_time = click1-click0
    crutil_time = click2-click1
    times_faster = python_time/crutil_time
    assert result_python == result_crutil
    print(f"Python took {python_time} s to calculate {num}!, whereas")
    print(f"CRUtil took {crutil_time} s.")
    print(f"CRUtil is {times_faster} times faster.")

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    demo_factorial(1_000_000)

if __name__ == "__main__":
    run()
