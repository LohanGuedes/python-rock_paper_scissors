import random

def main():

    #Computer Variables:
    computer_Option = ["Rock", "Paper", "Scissors"]
    computer_Selection = None
    computer_Score = 0

    #User Variables:
    user_Option = { 1:"Rock", 2:"Paper", 3:"Scissors"}
    user_Selection = None
    user_Score = 0

    #Game State Variables:
    game_over = False
    rounds = 0

    while(True):
        while user_Selection not in user_Option:
            print("Player, select one!")
            user_Selection = int(input("1. Rock, 2. Paper, 3. Scissors: "))

        user_Selection = user_Option[user_Selection]
        print("User:", user_Selection)
        computer_Selection = computer_Option[random.randint(0, 2)]
        print("Computer: ", computer_Selection)

        fun_return = determine_winner(user_Selection, computer_Selection)

        rounds += 1
        if rounds == 3:
            game_over = True

        if fun_return == "User":
            user_Score += 1
        elif fun_return == "Computer":
            computer_Score += 1

        if game_over == True:
            if user_Score > computer_Score:
                print("Player Wins!")
                print("Player Score:", user_Score)
                print("Computer Score:", computer_Score)
                break
            elif computer_Score > user_Score:
                print("Computer Wins!")
                print("Player Score:", user_Score)
                print("Computer Score:", computer_Score)
                break
            else:
                print("Tie!")
                break


def determine_winner(user_Selection, computer_Selection):
    if user_Selection == "Rock":
        if computer_Selection == "Paper":
            return "Computer"
        elif computer_Selection == "Scissors":
            return "User"
    if user_Selection == "Paper":
        if computer_Selection == "Scissors":
            return "Computer"
        elif computer_Selection == "Rocks":
            return "User"
    if user_Selection == "Scissors":
        if computer_Selection == "Rock":
            return "Computer"
        elif computer_Selection == "Paper":
            return "User"
    else:
        return "Tie"


# call the main function
main()
