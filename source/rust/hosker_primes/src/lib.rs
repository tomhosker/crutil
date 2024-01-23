/// This library defines some utility functions for working with primes.

// Non-standard imports.
use primes;

/***************************
 ** FOR INTERNAL USE ONLY **
 **************************/

/// Find the nth prime number.
fn _find_nth_prime(n: i32) -> i32 {
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
pub extern fn find_nth_prime(n: i32) -> i32 {
    return _find_nth_prime(n);
}
