# ===================================== [Rock Paper Scissors Project] ===================================== #

#Solo homework project (NO TEACHER HELP ALLOWED)

# ===================================== [Versions] ===================================== # 
#Version 1: Setting up helper functions, main functions (In a skeleton), and constants 
#Version 2: Finished setting up instructions and finished setting up welcome text using fancy text 



#Modules - These help with stuff 
import random #Helps with randomizing the answers given from the terminal 
import os

# ======== Constants ======== #
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

MOVES = (ROCK, PAPER, SCISSORS) #This constant is for the possible move options

#This constant is for determining the winning rules
WIN_RULES = {
    ROCK: SCISSORS, 
    PAPER: ROCK,
    SCISSORS: PAPER
}

POINTSPERWIN = 1 #This constant is for determining the amount of points per win and can be changed 

#This constant is for determining the amount of gamerounds and can be modular
GAMEROUNDS = 3

#Helper functions
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Main functions

def greeting_text():
    print("Welcome dear terminal gamer....... this is classic rock, paper, scissors")

def welcome_text(): #Welcomes the user into the rock, paper, scissors game using fancy text
    print("""
██████████████████████████████████████████████████████████████████████████████████████████
█▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─▄▄─███▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄█████
██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█████─███─██─████─▄─▄█─██─█─███▀██─▄▀██░░██
▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▀▀
██████████████████████████████████████████████████████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███████─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄█░░████▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
""")

def instructions():
    while True:
        print("Wow, I thought everyone knew this game but very well!")
        print("Type rock, paper, or scissors as your options")
        print("Always remember, \n rock beats paper, \n paper beats scissors \n and scissors beats rock")
        print(f"If you win, you get 1 point, if you lose, your opponent will get 1 point and it is first to {GAMEROUNDS}!")

        player_choice = input("Hey are you ready to play? Please say yes or no to start!:  ").lower().strip()

        if player_choice in ['yes', 'y']:
            print("Then let us begin!")
            return main()

        elif player_choice in ['no', 'n']:
            print("Oh...... Another time then!")
            break
        else:
            print("sorry that's invalid, please press yes or no")

        
def rps_game(): #This is the thing that handles the logic of the game and determining if the player can beat the clanker
    pass
        


def main(): #This is the backbone of my entire RPS game without it, I would be cooked
    pass
#main loop
main()


