#[aoc_generator(day3)]
pub fn input_generator(input: &str) -> Vec<String> {
    input
        .lines()
        .map(|l| l.to_string())
        .collect()
}

#[aoc(day3, part1)]
pub fn solve_part1(input: &[String]) -> u64 {
    input
        .iter().enumerate()
        .map(|(i, x)| {
            (x.chars().nth(3*i % x.len()).unwrap() == '#') as u64
        }).sum()
}

#[aoc(day3, part2)]
pub fn solve_part2(input: &[String]) -> u64 {
    input
        .iter().enumerate()
        .map(|(i, x)| {
            let ll = x.len();
            [
                (x.chars().nth(i % ll).unwrap() == '#') as u64,
                (x.chars().nth(3*i % ll).unwrap() == '#') as u64,
                (x.chars().nth(5*i % ll).unwrap() == '#') as u64,
                (x.chars().nth(7*i % ll).unwrap() == '#') as u64,
                (x.chars().nth((i/2) as usize % ll).unwrap() == '#' && i % 2 == 0) as u64,
            ]
        }).fold([0 as u64,0,0,0,0], |a, b| {
            [
                a[0]+b[0],
                a[1]+b[1],
                a[2]+b[2],
                a[3]+b[3],
                a[4]+b[4],
            ]
        }).iter().product()
}
