import random
from colorama import Fore, Back, Style

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_score = 0
cpu_score = 0

player_move = input(Fore.RESET + "Choose [r]ock, [p]aper or [s]cissors: ")
wanna_play = True

while wanna_play:
    not_valid = True
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        while not_valid:
            player_move = input(Fore.RED + "Invalid input. Choose [r]ock, [p]aper or [s]cissors: ")
            if player_move == "r":
                player_move = rock
                not_valid = False
            elif player_move == "p":
                player_move = paper
                not_valid = False
            elif player_move == "s":
                player_move = scissors
                not_valid = False

    computer_random_num = random.randint(1, 3)
    computer_move = ""
    if computer_random_num == 1:
        computer_move += "Rock"
    elif computer_random_num == 2:
        computer_move += "Paper"
    elif computer_random_num == 3:
        computer_move += "Scissors"
    print(Fore.BLUE + f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_score += 1
        print(Fore.GREEN + "You won this round!")
        print(Fore.RESET + f"Your score: {player_score}")
        print(Fore.RESET + f"CPU score: {cpu_score}")
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw! Let's try again and see who is superior!")
        print(Fore.RESET + f"Your score: {player_score}")
        print(Fore.RESET + f"CPU score: {cpu_score}")
    else:
        cpu_score += 1
        print(Fore.RED + "You lose!")
        print(Fore.RESET + f"Your score: {player_score}")
        print(Fore.RESET + f"CPU score: {cpu_score}")

    another_one = input(Style.RESET_ALL + "Wanna play again? Type [y]es or [n]o: ")
    while True:
        if another_one == "y":
            player_move = input(Fore.RESET + "Choose [r]ock, [p]aper or [s]cissors: ")
            break
        elif another_one == "n":
            wanna_play = False
            print(Fore.MAGENTA + "Thanks for playing!")
            print(f"Final score: CPU - {cpu_score}; Player - {player_score}")
            break
        else:
            another_one = input(Fore.RED + "Invalid input. Type [y]es or [n]o: ")
