use std::io;

fn main () {
    let mut s : String = String::new();
    io::stdin().read_line(&mut s).expect("Failed to read input");

    let mut complement = String::with_capacity(s.len());

    for c in s.chars() {
        match c {
            'A' => complement.push('T'),
            'C' => complement.push('G'),
            'G' => complement.push('C'),
            'T' => complement.push('A'),
            _ => (),
        }
    }

    let complement : String = complement.chars().rev().collect();
    println!("{}", complement);
}
