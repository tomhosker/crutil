"""
This code defines a continuous integration routine for this repository.
"""

# Standard imports.
from importlib import import_module
from multiprocessing import Process

# Non-standard imports.
from hosker_utils.continuous_integration import run_continuous_integration

#############
# FUNCTIONS #
#############

def pre_test():
    """ Run the pre-test routines. """
    c_utils_module = import_module("source.c_utils")
    rust_utils_module = import_module("source.rust_utils")
    c_utils_module.compile_c_packages()
    rust_utils_module.compile_rust_packages()

def segregate_pre_test():
    """ Run the pre-test routines without upsetting the importation of the
    module to be tested, and thus messing up the code coverage. """
    proc = Process(target=pre_test)
    proc.start()
    proc.join()

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    segregate_pre_test()
    run_continuous_integration()

if __name__ == "__main__":
    run()
