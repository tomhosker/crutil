/// This library defines some utility functions for working with primes.

// Non-standard imports.
use num_bigint::{BigInt, Sign};
use num_integer::Integer;
use num_iter;
use primes;

// Local constants.
const MAX_DIGITS: usize = 100;

/***************************
 ** FOR INTERNAL USE ONLY **
 **************************/

/// Find the nth prime number, provided that n is a 32-bit integer.
fn _find_nth_prime_i32(n: i32) -> i32 {
    let mut count = 1; // 2 being the first prime.
    let mut current = 3; // 3 being the second prime.

    while count < n {
        if primes::is_prime(current) {
            count += 1;
        }

        current += 2;
    }

    current -= 2;

    return current as i32;
}

/// Determine whether an arbitrarily large integer is prime.
fn _is_big_prime(potential_prime: BigInt) -> bool {
    println!("potential_prime: {:?}", potential_prime);

    if potential_prime == BigInt::from(2) {
        return true;
    }
    if potential_prime.is_even() {
        return false;
    }

    let max_potential_divisor = potential_prime.sqrt();

    for potential_divisor in num_iter::range_inclusive(BigInt::from(3), max_potential_divisor) {
        //println!("potential_divisor: {:?}", potential_divisor);
        if potential_prime.is_multiple_of(&potential_divisor) {
            return false;
        }
    }

    return true;
}

/// Find the nth prime number, for an arbitrarily large n.
fn _find_nth_prime_bigint(n: BigInt) -> BigInt {
    let mut count = BigInt::from(1); // 2 being the first prime.
    let mut current = BigInt::from(3); // 3 being the second prime.

    while count < n {
        println!("count: {:?}", count);
        if _is_big_prime(current.clone()) {
            count += 1;
        }

        current += 2;
    }

    current -= 2;

    return current;
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

/// A wrapper for the similarly-named function above.
#[no_mangle]
pub unsafe extern fn find_nth_prime_bigint(
    list: PortableDigitList
) -> Vec<u32> {
    let digits = Vec::from(*list.array);
    println!("Digits: {:?}", digits.clone());
    let big_integer = BigInt::new(Sign::Plus, digits);
    println!("Input big int: {:?}", big_integer.clone());
    let result_bigint = _find_nth_prime_bigint(big_integer);
    println!("Result big int: {:?}", result_bigint.clone());
    let (_, result) = result_bigint.to_u32_digits();
    println!{"{:?}", result};
    return result;
}

#[no_mangle]
pub unsafe extern fn print_big_int(list: PortableDigitList) {
    unsafe {
        let digits = Vec::from(*list.array);
        let big_integer = BigInt::new(Sign::Plus, digits);

        println!("What an ENORMOUS integer: {}", big_integer);
    }
}
