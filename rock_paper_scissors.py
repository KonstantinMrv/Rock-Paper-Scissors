import random
from colorama import Fore, Back, Style

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit(Fore.RED + "Invalid input. Choose [r]ock, [p]aper or [s]cissors and try again!")

computer_random_num = random.randint(1, 3)
computer_move = ""
if computer_random_num == 1:
    computer_move += "Rock"
elif computer_random_num == 2:
    computer_move += "Paper"
elif computer_random_num == 3:
    computer_move += "Scissors"
print(Fore.BLUE + f"The computer chose {computer_move}.")
print(Style.RESET_ALL)

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print(Fore.GREEN + "You won this round!")
elif player_move == computer_move:
    print(Fore.YELLOW + "Draw! Let's try again and see who is superior!")
else:
    print(Fore.RED + "You lose!")

