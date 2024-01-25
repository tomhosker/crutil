/// This library defines some utility functions for working with primes.

// Non-standard imports.
use num_bigint::{BigInt, Sign};
use primes;

// Local constants.
const MAX_DIGITS: usize = 100;

/***************************
 ** FOR INTERNAL USE ONLY **
 **************************/

/// Find the nth prime number.
fn _find_nth_prime_i32(n: i32) -> i32 {
    let mut count = 0;
    let mut current = 0;

    while count < n {
        current += 1;

        if primes::is_prime(current) {
            count += 1;
        }
    }

    return current as i32;
}

/****************
 ** FOR EXPORT **
 ***************/

/// A portable representation of a large integer.
#[repr(C)]
pub struct PortableDigitList {
    array: *const [u32; MAX_DIGITS]
}

/// Reassure an external user that they can indeed access this library.
#[no_mangle]
pub extern fn make_contact(int: i32) {
    println!("Congratulations! You have made contact with the PRIMES library.");
    println!("This is the integer you gave me: {}", int);
}

/// A wrapper for the similarly-named function above.
#[no_mangle]
pub extern fn find_nth_prime_i32(n: i32) -> i32 {
    return _find_nth_prime_i32(n);
}

#[no_mangle]
pub extern fn print_big_int(list: PortableDigitList) {
    unsafe {
        let digits = Vec::from(*list.array);
        let big_integer = BigInt::new(Sign::Plus, digits);

        println!("What an ENORMOUS integer: {}", big_integer);
    }
}
