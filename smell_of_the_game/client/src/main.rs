use std::net::TcpStream;
use std::io::prelude::*;
use std::io::{BufWriter, BufReader};

use obfstr::obfstr;

fn main() {
    let host = String::from("127.0.0.1");
    let port = 25656;
    //let mut streamdata = Vec::<u8>::new();
    let mut streamdata = String::new();

    // init sequence
    println!("Connecting Game Server...");
    let mut stream = TcpStream::connect((host, port))
                               .expect("Connection Error. Please Contact Admin.");
    let mut bufwriter = BufWriter::new(&stream);
    let mut bufreader = BufReader::new(&stream);
    println!("Connection Complete.");
    println!("Initialize...");
    let _ = bufwriter.write(b":CMD:INIT\n");
    let _ = bufwriter.flush().unwrap();
    let _ = bufreader.read_line(&mut streamdata).unwrap();
    println!("{:?}", streamdata);
    data()

}

fn data() {
    obfstr! {
        let flag = "yuruhack{THIS_IS_BULLSHIT_BLAZING}";
    }
    println!("{}", flag);
}
