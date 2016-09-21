// input: string s
// output: 4 integers: the counts of A C G T

use std::io;

#[derive(Copy, Clone)]
struct Counters {
    a : u32,
    c : u32,
    g : u32,
    t : u32
}


fn main() {
    let mut s : String = String::new();
    io::stdin().read_line(&mut s).expect("Failed to read input");

    let mut counter : Counters = Counters { a : 0, c : 0, g : 0, t : 0};
    for c in s.chars() {
        match c {
            'A' => counter.a += 1,
            'C' => counter.c += 1,
            'G' => counter.g += 1,
            'T' => counter.t += 1,
            _ => (),
        }
    }
    println! ("{} {} {} {}", counter.a, counter.c, counter.g, counter.t);
}
