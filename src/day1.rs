use std::collections::HashSet;

#[aoc_generator(day1)]
pub fn input_generator(input: &str) -> Vec<u32> {
    let mut input: Vec<_> = input
        .lines()
        .map(|l| l.parse().unwrap())
        .collect();
        input.sort_unstable();
        input
}

#[aoc(day1, part1)]
pub fn solve_part1(input: &[u32]) -> u32 {
    let mut expenses: HashSet<u32> = HashSet::new();
    for i in 0..input.len() {
        let e = input[i];
        let expense = 2020 - e;
        if expenses.contains(&expense) {
            return e * expense;
        }
        expenses.insert(e);
    }
    panic!("no solution")
}

#[aoc(day1, part2)]
pub fn solve_part2(input: &[u32]) -> u32 {
    for i in 0..input.len() {
        let e = input[i];
        let remains = 2020 - e;
        let mut expenses: HashSet<u32> = HashSet::new();
        for j in i+1..input.len() {
            let f = input[j];
            let expense = remains.wrapping_sub(f);
            if expenses.contains(&expense) {
                return expense * e * f;
            }
            expenses.insert(f);
        }
    }
    panic!("no solution")
}