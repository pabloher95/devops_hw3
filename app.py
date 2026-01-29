from flask import Flask, request, jsonify, Response
import random

dice_art = {  # art from https://realpython.com/python-dice-roll/
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

# art from https://github.com/itsjordanmuller/2023-python-100-days/blob/main/Day-004/Exercises/1-heads-or-tails.py
coin_art = {
    0: """
  ╔════════╗  
 ╔╝ ░░░▒▒▓ ╚╗ 
╔╝ ░░░░▒▒▓▓ ╚╗
║ ░░░HEAD▒▓▓ ║
╚╗ ░░░▒▒▒▓▓ ╔╝
 ╚╗ ░░░▒▒▓ ╔╝ 
  ╚════════╝    
""",
    1: """
  ╔════════╗  
 ╔╝ ░░░▒▒▓ ╚╗ 
╔╝ ░░░░▒▒▓▓ ╚╗
║ ░░░TAIL▒▓▓ ║
╚╗ ░░░▒▒▒▓▓ ╔╝
 ╚╗ ░░░▒▒▓ ╔╝ 
  ╚════════╝  
""",
}


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Flask!"


@app.route("/rps", methods=["GET"])
def rps():
    choices = ["rock", "paper", "scissors"]

    user_choice = request.args.get("choice", "").lower()

    if user_choice not in choices:
        return jsonify({"error": "invalid choice"}), 400

    pc_choice = random.choice(choices)

    if user_choice == pc_choice:
        result = "draw"

    elif (
        (user_choice == "rock" and pc_choice == "scissors")
        or (user_choice == "paper" and pc_choice == "rock")
        or (user_choice == "scissors" and pc_choice == "paper")
    ):
        result = "win"
    else:
        result = "lose"

    return jsonify({"user": user_choice, "pc": pc_choice, "result": result})


@app.route("/diceroll", methods=["GET"])
def diceroll():
    dice = random.randint(1, 6)

    result = "\n".join(dice_art[dice])

    return Response(f"Dice Roll: {dice}\n{result}", mimetype="text/plain charset=utf-8")


@app.route("/coinflip", methods=["GET"])
def coinflip():
    result = random.randint(0, 1)

    result_str = 'Head' if result == 0 else "Tail"

    return Response(
        f"Coin Flip: {result_str}\n{coin_art[result]}", mimetype="text/plain charset=utf-8"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
