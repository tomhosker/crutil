/// This library defines some utility functions for working with primes.

// Non-standard imports.
use num_bigint::{BigInt, Sign};
use primes;

/***************************
 ** FOR INTERNAL USE ONLY **
 **************************/

#[repr(C)]
pub struct List_4 {
    array: *const [i32; 4]
}

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
pub extern fn print_big_int(list: List_4) {
    unsafe { println!("{:?}", *list.array) };

//    let big_integer = BigInt::new(Sign::Plus, digits);

//    println!("What an ENORMOUS integer: {}", big_integer);
}
