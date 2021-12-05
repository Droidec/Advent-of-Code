/*
 * Advent of Code 2015 day 01 part two
 */

use std::fs::File; // File::open
use std::io::Read; // read_to_string
use std::process; // process::exit

// String slice constant
const INPUT_FILE: &str = "../inputs/01-input.txt";

fn main() {
    let mut file = File::open(INPUT_FILE).expect(&format!("Failed to open file '{}'", INPUT_FILE));
    let mut buffer = String::new();
    let mut floor = 0;

    // TODO: we should read byte per byte instead
    file.read_to_string(&mut buffer).expect("read_to_string failed");

    for (index, ch) in buffer.chars().enumerate() {
        match ch {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => panic!("Invalid character found at position {}", index + 1),
        };

        if floor == -1 {
            println!("Basement is reached at position {}", index + 1);
            process::exit(0);
        }
    }

    println!("The right floor is {}", floor);
}
