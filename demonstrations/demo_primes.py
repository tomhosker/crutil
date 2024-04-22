"""
This file defines a script which demonstrates the capabilities of the PRIMES
module to a new user of this package.
"""

# Standard imports.
from time import time

# Non-standard imports.
from sympy import isprime as sympy_isprime

# Custom imports.
from hosker_rutil.primes import is_prime as rutil_isprime

# Local constants.
THREE_DIGIT_PRIME = 307
TEN_DIGIT_PRIME = 1000000007
TWENTY_DIGIT_PRIME = 10089886811898868001
HUNDRED_DIGIT_PRIME = (10**99)+6001

#############
# FUNCTIONS #
#############

def demo_finding_prime(prime):
    """ Ronseal. """
    click0 = time()
    assert rutil_isprime(prime)
    click1 = time()
    assert sympy_isprime(prime)
    click2 = time()
    rutil_time = click1-click0
    sympy_time = click2-click1
    print(f"rutil took {rutil_time} s to determine that {prime} is prime...")
    print("whereas...")
    print(f"sympy took {sympy_time} s to do the same.")

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    demo_finding_prime(THREE_DIGIT_PRIME)
    demo_finding_prime(TEN_DIGIT_PRIME)
    demo_finding_prime(TWENTY_DIGIT_PRIME)
    demo_finding_prime(HUNDRED_DIGIT_PRIME)

if __name__ == "__main__":
    run()
