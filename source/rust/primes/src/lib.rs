/// This library defines some utility functions for working with primes.

// Imports.
use std::ffi::CStr;
use std::os::raw::c_char;
use std::str;

/// Turn a C-string into a string slice and print to console:
#[no_mangle]
pub extern "C" fn make_contact(c_string_ptr: *const c_char) {
    let bytes = unsafe { CStr::from_ptr(c_string_ptr).to_bytes() };
    let silly_word = str::from_utf8(bytes).unwrap();

    println!("Congratulations! You have made contact with the PRIMES library.");
    println!("This is the silly word you gave me: {}", silly_word);
}
