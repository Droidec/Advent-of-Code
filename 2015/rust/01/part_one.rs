/*
 * Advent of Code 2015 day 01 part one
 */

use std::fs::File;
use std::io::BufReader;

// String slice constant
const INPUT_FILE: &str = "../inputs/01-input.txt";

fn main() {
    let mut file = BufReader::new(
        File::open(INPUT_FILE).expect(&format!("Failed to open file '{}'", INPUT_FILE)),
    );
}
