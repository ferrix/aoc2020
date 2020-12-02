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
            let cred: Vec<&str> = l.trim().split(" ").collect();
            let mut parts = cred[0].split("-").map(|n| n.parse::<u32>());
            let letter = &cred[1].chars().nth(0);
            Cred {
                low: parts.next().unwrap().unwrap(),
                high: parts.next().unwrap().unwrap(),
                letter: letter.unwrap(),
                password:cred[2].to_string(),
            }
        }).collect()
}

#[aoc(day2, part1)]
pub fn solve_part1(input: &[Cred]) -> u32 {
    input
        .iter()
        .map(|c| {
            let count = c.password.matches(c.letter).count() as u32;

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
