"""
This code defines a continuous integration routine for this repository.
"""

# Non-standard imports.
from hosker_utils.continuous_integration import run_continuous_integration

# Local imports.
from source.c_utils import compile_c_packages
from source.rust_utils import compile_rust_packages

#############
# FUNCTIONS #
#############

def pre_test():
    """ Install this project's Rust libraries locally, in order to facilitate
    testing. """
    compile_c_packages()
    compile_rust_packages()

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    pre_test()
    run_continuous_integration()

if __name__ == "__main__":
    run()
