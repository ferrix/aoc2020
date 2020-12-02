extern crate serde;
extern crate serde_scan;

#[derive(Deserialize, Debug, PartialEq)]
pub struct Cred {
    low: u32,
    high: u32,
    letter: char,
    password: String,
}

#[aoc_generator(day2)]
pub fn input_generator(input: &str) -> Vec<Cred> {
    input
        .lines()
        .map(|l| {
            serde_scan::scan!("{}-{} {}: {}" <- l).unwrap()
        }).collect()
}

#[aoc(day2, part1)]
pub fn solve_part1(input: &[Cred]) -> u32 {
    input
        .iter()
        .map(|c| {
            let count = c.password.chars().filter(|x| *x == c.letter).count() as u32;

            if c.low <= count && count <= c.high {
                1
            } else {
                0
            }
        }).sum()
}

#[aoc(day2, part2)]
pub fn solve_part2(input: &[Cred]) -> u32 {
    input
        .iter()
        .map(|c| {
            if (c.password.chars().nth((c.low-1) as usize) == Some(c.letter)) != (c.password.chars().nth((c.high-1) as usize) == Some(c.letter)) {
                1
            } else {
                0
            }
        }).sum()
}
