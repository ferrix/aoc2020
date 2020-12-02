use structopt::StructOpt;

#[derive(StructOpt)]
struct Cli {
    #[structopt(parse(from_os_str))]
    path: std::path::PathBuf,
}

fn main() {
    let args = Cli::from_args();

    let content = std::fs::read_to_string(&args.path)
        .expect("could not read file");

    let mut valid = 0;
    let mut new_valid = 0;

    for line in content.lines() {
        let strings: Vec<&str> = line.split(" ").collect();
        let mut parts = strings[0].split("-").map(|num| num.parse::<i32>());
        let lo = parts.next().unwrap().unwrap();
        let hi = parts.next().unwrap().unwrap();
        let letter = &strings[1][..(strings[1].len()-1)];
        let password = &strings[2];
        let count = password.matches(letter).count() as i32;

        if lo <= count && count <= hi {
            valid += 1;
        }

        if (password.chars().nth((lo-1) as usize) == letter.chars().nth(0)) != (password.chars().nth((hi-1) as usize) == letter.chars().nth(0)) {
            new_valid += 1;
        }
    }

    println!("{}", valid);
    println!("{}", new_valid);
}
