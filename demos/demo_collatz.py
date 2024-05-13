"""
This file defines a script which demonstrates the capabilities of the COLLATZ
module to a new user of this package.
"""

# Standard imports.
from time import time

# Custom imports.
from crutil.rust_utils import MAX_I32
from crutil.collatz import (
    count_collatz_steps_large as count_collatz_steps_python,
    count_collatz_steps as count_collatz_steps_crutil
)

#############
# FUNCTIONS #
#############

def demo_count_collatz_steps(start):
    """ Ronseal. """
    click0 = time()
    collatz_steps_python = count_collatz_steps_python(start)
    click1 = time()
    collatz_steps_crutil = count_collatz_steps_crutil(start)
    click2 = time()
    python_time = click1-click0
    crutil_time = click2-click1
    times_faster = python_time/crutil_time
    assert collatz_steps_python == collatz_steps_crutil
    print(
        f"Python took {python_time} s to determine that {start} requires "+
        f"{collatz_steps_python} to reach 1, whereas"
    )
    print(f"CRUtil took {crutil_time} s.")
    print(f"CRUtil is {times_faster} times faster.")

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    demo_count_collatz_steps(MAX_I32)
    print("")
    demo_count_collatz_steps(int(MAX_I32/4))

if __name__ == "__main__":
    run()
