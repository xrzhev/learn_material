use rand::Rng;

//
// game
//

struct RockPaperSissor {
    winning_streak: u32,
}

struct RPSResult {
    winning_streak: u32,
    server_hand: u32,
    // 0: client win
    // 1: draw
    // 2: server win
    winner: u32,
}

impl RockPaperSissor {
    // hand
    // 0: Rock
    // 1: Paper
    // 2: Scissor
    fn battle(&mut self, user_hand: u32) -> RPSResult{
        let mut rng = rand::thread_rng();
        let server_hand = rng.gen_range(0..3);
        let hands = (user_hand, server_hand);

        // client win
        if hands == (0,2) || hands == (1,0) || hands == (2,1) {
            self.winning_streak += 1;
            RPSResult {
                winning_streak: self.winning_streak,
                server_hand: server_hand,
                winner: 0
            }
        //draw
        } else if hands == (0,0) || hands == (1,1) || hands == (2,2) {
            RPSResult {
                winning_streak: self.winning_streak,
                server_hand: server_hand,
                winner: 1
            }
        //lose
        } else {
            self.winning_streak = 0;
            RPSResult {
                winning_streak: self.winning_streak,
                server_hand: server_hand,
                winner: 2
            }
        }
    }
}


// stdin util
fn conn_recv() -> String {
    let mut user_input = String::new();
    std::io::stdin().read_line(&mut user_input).unwrap();
    user_input.trim().to_string()
}

// connection halt
fn conn_halt() {
    println!(":MSG:hmmm... it looks illegal? bye!");
    println!(":HALT:");
    std::process::exit(1);
}


fn main() {
    let mut user_input;
    let mut rps = RockPaperSissor {winning_streak: 0};

    // init sequence
    user_input = conn_recv();
    if user_input != ":CMD:INIT" {
        conn_halt();
    }
    // sync
    println!(":HAND:RDY");
    // game loop
    loop {
        user_input = conn_recv();
        let user_num = user_input.parse::<u32>();

        // pass only possible values in u32 and 0,1,2.
        // otherwise, conn_halt as an exception.
        let user_num = match user_num {
            Ok(num) => {
                if num != 0 && num != 1 && num != 2 { 
                    conn_halt();
                }
                num 
            },
            Err(err) => {
                conn_halt();
                panic!("Err: {}", err);
            }
        };
        let result = rps.battle(user_num);
        println!("Winner: {}, Streak: {}", result.winner, result.winning_streak);


        if rps.winning_streak == 100 {
            println!(":MSG:YOU WIN!");
            //it's a flag, definitively obvious and self-evident
            println!(":CMD:RESIGN");
            conn_halt();
        }
    }
}