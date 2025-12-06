import random
while True:
    user_action = input("Enter a choice(rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computor_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computor chose {computor_action}.\n")

    if user_action == computor_action:
        print("A tie!")
    elif user_action == "rock":
        if computor_action == "scissors":
            print("rock smashes scissors you win!")
        else:
            print("Paper covers rock you lose!")

    elif user_action == "paper":
        if computor_action == "scissors":
            print("Scissors cut paper you lose!")
        else:
            print("Paper covers rock you win!")
    else:
        if user_action == "scissors":
            if computor_action == "scissors":
                print("Rock smashes scissors you lose!")
            else:
                print("scissors cuts paper you win!")
    play_again = input("Do you want to play again? y/n")
    if play_again == "y":
        break