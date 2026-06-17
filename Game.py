import random

print("=" * 50)
print("      ROCK PAPER SCISSORS GAME")
print("=" * 50)
print("Instructions:")
print("Choose Rock, Paper, or Scissors")
print("Type 'exit' anytime to quit the game.")
print("-" * 50)

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("\nEnter your choice (Rock/Paper/Scissors): ").lower()

    if user_choice == "exit":
        print("\nThanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour Choice     :", user_choice.capitalize())
    print("Computer Choice :", computer_choice.capitalize())

    if user_choice == computer_choice:
        print("Result: It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print("-------------")
    print("You      :", user_score)
    print("Computer :", computer_score)

    play_again = input("\nDo you want to play another round? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n" + "=" * 50)
print("FINAL SCORE")
print("=" * 50)
print("You      :", user_score)
print("Computer :", computer_score)

if user_score > computer_score:
    print("Overall Winner: You ")
elif computer_score > user_score:
    print("Overall Winner: Computer ")
else:
    print("Overall Result: Tie ")

print("\nGame Over. Thank you for playing!")