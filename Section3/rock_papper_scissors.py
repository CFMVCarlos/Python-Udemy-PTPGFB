import random
import sys

# STEP 1: STARTING INFORMATION
print("Welcome to Rock, Paper, Scissors!")
movs: dict[str, str] = {"rock": "🪨", "scissors": "✂️", "paper": "📜"}
valid_moves: list[str] = list(movs.keys())

# STEP 2: INFINITE LOOP
while True:
    user_move: str = input("Rock, paper, or scissors? >>").casefold()

    if user_move == "exit":
        print("Goodbye!")
        sys.exit()

    if user_move not in valid_moves:
        print("Invalid move. Try again.")
        continue

    ai_move: str = random.choice(valid_moves)

    print("----")
    print(f"You: {movs[user_move]}")
    print(f"AI: {movs[ai_move]}")
    print("----")

    if user_move == ai_move:
        print("It's a tie!")
    elif (
        (user_move == "rock" and ai_move == "scissors")
        or (user_move == "scissors" and ai_move == "paper")
        or (user_move == "paper" and ai_move == "rock")
    ):
        print("You win!")
    else:
        print("AI winds...")
