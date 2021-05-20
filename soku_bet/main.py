from flask import Flask, render_template, redirect, url_for, session, request
import pickle
import random

app = Flask(__name__)
app.secret_key = "worker"

# GLOBAL
# ======================
UMA_LIST = [
        "ユルイウィーク",
        "サイレンスユルイ",
        "ユルイトップガン",
        "ユルイグルーヴ",
        "ユルイクロス",
        "ユルイタキオン",
        "ユルイワン",
        "ユルイチャン",
        "ユルイバクシンオー",
        "ユルイテイオー",
        "ユルイルドルフ",
        "ユルハヤヒデ",
        "ユルイシャワー",
        "ユルイネイチャ",
        "ユルイターボ",
        "ユルイブラック"
        ]

MONEY = 1000
# ======================


class UMA:
    def __init__(self, uma_list: list, own_money: int):
        self.own_money = own_money
        self.uma_list = uma_list
        self.uma_entries = []
        self.winner_tables = None

    def __randomset_frame(self) -> None:
        random.shuffle(self.uma_list)

    def __randomset_state(self) -> str:
        state = ["◎", "○", "▲", "△", "×"]
        return random.choice(state)

    def __gen_odds(self, state: str) -> int:
        odds = None
        if state == "◎" or state == "○":
            odds = random.randint(2, 8)
        elif state == "▲" or state == "△":
            odds = random.randint(10, 100)
        elif state == "×":
            odds = random.randint(101, 300)
        return odds

    def __gen_winner_table(self) -> list:
        faster = []
        middle = []
        slowly = []

        def __fortune(percentage: int):
            balance = random.random()
            return True if balance > percentage*0.01 else False

        for i in self.uma_entries:
            state = i["state"]
            if state == "◎" or state == "○":
                if __fortune(80):
                    faster.append(i)
                else:
                    middle.append(i)
            elif state == "▲" or state == "△":
                if __fortune(30):
                    faster.append(i)
                elif __fortune(30):
                    slowly.append(i)
                else:
                    middle.append(i)
            elif state == "×":
                if __fortune(20):
                    middle.append(i)
                else:
                    slowly.append(i)
        random.shuffle(faster)
        random.shuffle(middle)
        random.shuffle(slowly)
        return faster + middle + slowly

    def gen_entries(self) -> None:
        self.__randomset_frame()
        self.uma_entries = []
        for i in range(len(self.uma_list)):
            frame = i+1
            name = self.uma_list[i]
            state = self.__randomset_state()
            odds = self.__gen_odds(state)
            json = {"frame": frame, "name": name, "state": state, "odds": odds}
            self.uma_entries.append(json)
        self.winner_tables = self.__gen_winner_table()

    def get_entries(self) -> list:
        return self.uma_entries

    def get_winners(self) -> list:
        return self.winner_tables

    def get_winner_tansho(self) -> dict:
        return self.winner_tables[0]

    def get_winner_sanrentan(self) -> list:
        return self.winner_tables[0:3]

    def get_own_money(self) -> int:
        return self.own_money

    def is_win(self, buy_type: str, select_horse: list) -> bool:
        if buy_type == "tansho":
            winner = self.get_winner_tansho()
            user = select_horse
            print(winner, user)
            if winner["frame"] == user[0]:
                return True
            else:
                return False

        elif buy_type == "sanrentan":
            winner = self.get_winner_sanrentan()
            user = select_horse
            if winner[0]["frame"] == user[0] and winner[1]["frame"] == user[1] and winner[2]["frame"] == user[2]:
                return True
            else:
                return False


@app.route("/")
def page_main():
    if "keiba" not in session:
        keiba = UMA(UMA_LIST, MONEY)
        keiba.gen_entries()
        session["keiba"] = pickle.dumps(keiba)
    else:
        keiba = pickle.loads(session["keiba"])
    return render_template("header.html", entries=keiba.get_entries(), own_money=keiba.get_own_money())


@app.route("/new", methods=["POST"])
def page_new():
    if "keiba" in session:
        keiba = pickle.loads(session["keiba"])
        keiba.gen_entries()
        session["keiba"] = pickle.dumps(keiba)
    return redirect(url_for("page_main"))


@app.route("/buy", methods=["POST"])
def page_buy():
    if "keiba" in session:
        keiba = pickle.loads(session["keiba"])
        buy_type = request.form["buy_type"]
        select_horse = request.form["tansho_horse"]
        a = keiba.is_win(buy_type, list(select_horse))
        return str(a)
    else:
        return redirect(url_for("page_main"))


@app.route("/result")
def page_result():
    return "result!"


if __name__ == "__main__":
    app.run(debug=True)
