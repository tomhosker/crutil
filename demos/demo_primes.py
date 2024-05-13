"""
This file defines a script which demonstrates the capabilities of the PRIMES
module to a new user of this package.
"""

# Standard imports.
from time import time

# Non-standard imports.
import sympy
from sympy import isprime as python_isprime

# Custom imports.
from crutil.primes import (
    is_prime as crutil_isprime,
    is_prime_bigint_rust as rust_isprime,
    nth_prime as crutil_nth_prime
)

# Local constants.
THREE_DIGIT_PRIME = 307
THREE_DIGIT_COMPOSITE = 309
TEN_DIGIT_PRIME = 1000000007
TEN_DIGIT_COMPOSITE = 1000000011
TWENTY_DIGIT_PRIME = 10089886811898868001
TWENTY_DIGIT_COMPOSITE = 10089886811898868003
NTH_PRIMES = {
    100: 541,
    10000: 104729,
    1000000: 15485863,
    100000000: 2038074743
}

#############
# FUNCTIONS #
#############

def demo_specific_is_prime(prime):
    """ Ronseal. """
    click0 = time()
    assert python_isprime(prime)
    click1 = time()
    assert rust_isprime(prime)
    click2 = time()
    assert crutil_isprime(prime)
    click3 = time()
    python_time = click1-click0
    rust_time = click2-click1
    crutil_time = click3-click2
    print(f"Python took {python_time} s to determine {prime} is prime;")
    print(f"BigInt Rust took {rust_time} s to do the same;")
    print(f"CRUtil took {crutil_time} s.")

def demo_specific_is_composite(composite):
    """ Ronseal. """
    click0 = time()
    assert not python_isprime(composite)
    click1 = time()
    assert not rust_isprime(composite)
    click2 = time()
    assert not crutil_isprime(composite)
    click3 = time()
    python_time = click1-click0
    rust_time = click2-click1
    crutil_time = click3-click2
    print(f"Python took {python_time} s to determine {composite} is composite;")
    print(f"BigInt Rust took {rust_time} s to do the same;")
    print(f"CRUtil took {crutil_time} s.")

def demo_is_prime():
    """ Run this file. """
    demo_specific_is_prime(THREE_DIGIT_PRIME)
    print(" ")
    demo_specific_is_prime(TEN_DIGIT_PRIME)
    print(" ")
    demo_specific_is_prime(TWENTY_DIGIT_PRIME)
    print(" ")
    demo_specific_is_composite(THREE_DIGIT_COMPOSITE)
    print(" ")
    demo_specific_is_composite(TEN_DIGIT_COMPOSITE)
    print(" ")
    demo_specific_is_composite(TWENTY_DIGIT_COMPOSITE)
    print(" ")

def python_nth_prime(ordinal):
    """ Ronseal. """
    return sympy.ntheory.generate.prime(ordinal)

def demo_specific_nth_prime(ordinal, prime):
    """ Ronseal. """
    click0 = time()
    assert python_nth_prime(ordinal) == prime
    click1 = time()
    assert crutil_nth_prime(ordinal) == prime
    click2 = time()
    python_time = click1-click0
    crutil_time = click2-click1
    print(f"Python took {python_time} s to find prime with ordinal {ordinal};")
    print(f"CRUtil took {crutil_time} s to do the same.")

def demo_nth_prime():
    """ Ronseal. """
    for ordinal, prime in NTH_PRIMES.items():
        demo_specific_nth_prime(ordinal, prime)
        print(" ")

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    demo_is_prime()
    demo_nth_prime()

if __name__ == "__main__":
    run()
