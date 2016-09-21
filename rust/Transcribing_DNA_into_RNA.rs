use std::io;

fn main () {
    let mut s : String = String::new();
    io::stdin().read_line(&mut s).expect("Failed to read input");

    let s2 = s.replace("T", "U");
    println!("{}", s2);
}
