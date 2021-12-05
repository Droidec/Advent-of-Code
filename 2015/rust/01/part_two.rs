/*
 * Advent of Code 2015 day 01 part two
 */

use std::fs::File; // File::open
use std::io::BufReader; // BufReader::new
use std::io::Read; // read
use std::process; // process::exit

// String slice constant
const INPUT_FILE: &str = "../inputs/01-input.txt";

fn main() {
    let file = File::open(INPUT_FILE).expect(&format!("Failed to open file '{}'", INPUT_FILE));
    let mut reader = BufReader::new(file); // optimize reading
    let mut buffer = [0; 1];
    let mut floor = 0;
    let mut index = 0;

    loop {
        let num_bytes = reader.read(&mut buffer).expect("read failed"); // Read 1 byte
        if num_bytes == 0 {
            break; // EOF
        }

        let inst = match std::str::from_utf8(&buffer) {
            Ok(ch) => ch,
            Err(_) => panic!("Invalid UTF-8 character found at position '{}'", index + 1),
        };

        match inst.chars().next().unwrap() {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => panic!("Invalid character found at position '{}'", index + 1),
        };

        if floor == -1 {
            println!("Basement is reached at position '{}'", index + 1);
            process::exit(0);
        }

        index += num_bytes;
    }

    println!("The basement was never reached?");
    process::exit(1);
}
