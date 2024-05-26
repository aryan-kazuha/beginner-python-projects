import random

def game_p():
    
    choices = ["rock","paper","scissors"]
    computer_choice = random.choice(choices)
    player = str(input("Enter you choice(rock,paper,scissor): "))
    player_choice = player.lower()

    if player_choice == "rock":
        if computer_choice == "rock":
            print(player_choice ," vs ",computer_choice)
            print("DRAW!")

        if computer_choice=="paper":
            print(player_choice ," vs ",computer_choice)
            print("computer wins!")

        if computer_choice=="scissors":
            print(player_choice ," vs ",computer_choice)
            print("player wins!")

    if player_choice == "paper":
        if computer_choice == "rock":
            print(player_choice ," vs ",computer_choice)
            print("player wins!")

        if computer_choice=="paper":
            print(player_choice ," vs ",computer_choice)
            print("DRAW!")


        if computer_choice=="scissors":
            print(player_choice ," vs ",computer_choice)
            print("computer wins!")

    if player_choice == "scissors":
        if computer_choice == "rock":
            print(player_choice ," vs ",computer_choice)
            print("computer wins!")

        if computer_choice=="paper":
            print(player_choice ," vs ",computer_choice)
            print("player wins!")


        if computer_choice=="scissors":
            print(player_choice ," vs ",computer_choice)
            print("DRAW!")

def main():
    while True:
        play_game = input("Do you want to play Rock Paper Scissors? (yes/no): ").lower()
        if play_game == "yes":
            game_p()
        elif play_game == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
main()