import random

def game():
    choices = {"r": "rock", "p": "paper", "s": "scissors"}
    score = {"user": 0, "computer": 0}

    print("Welcome to Rock, Paper, Scissors Game!")
    num_chances = int(input("Enter the number of chances you want to play: "))

    for _ in range(num_chances):
        print("\n--------------------------------------------------------------")
        print("*Enter 'r' for rock, 'p' for paper, or '' for scissors to play.*")
        print("----------------------------------------------------------------")

        user_choice = input("Enter your choice: ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(list(choices.values()))

        print(f"\nYou chose: {choices[user_choice]}")
        print(f"Computer chose: {computer_choice}\n")

        if choices[user_choice] == computer_choice:
            print("It's a tie!")
        elif (choices[user_choice] == "rock" and computer_choice == "scissors") or \
             (choices[user_choice] == "scissors" and computer_choice == "paper") or \
             (choices[user_choice] == "paper" and computer_choice == "rock"):
            print("You win!")
            score["user"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1

        print(f"Score - You: {score['user']}, Computer: {score['computer']}")
    print("\n--------------------------------------------------------------")
    print("\nThanks for playing !")
    if score["user"] > score["computer"]:
        print("You won the game!")
    elif score["user"] < score["computer"]:
        print("Computer won the game!")
    else:
        print("It's a tie game!")
    print(f"Final Score - You: {score['user']}, Computer: {score['computer']}")

if __name__ == "__main__":
    game()
