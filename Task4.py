import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock–Paper–Scissors Game!")
    print("---------------------------------------")

    while True:
        print("\nChoose one: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid choice! Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"\n🧍 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("🤝 It's a tie!")
        elif winner == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💀 Computer wins this round!")
            computer_score += 1

        print(f"\n🏆 Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n👋 Thanks for playing! Final Scores:")
            print(f"👉 You: {user_score} | 💻 Computer: {computer_score}")
            print("Goodbye!")
            break

# Run the game
play_game()
