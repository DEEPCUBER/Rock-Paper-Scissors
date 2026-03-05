# ===================================== [Rock Paper Scissors HW] ===================================== #

#Solo homework project (NO TEACHER HELP ALLOWED and CLANKERGPT/MICROSLOP HELP!)

# ===================================== [Versions] ===================================== # 
#Version 1: Finished up helper functions, main functions (In a skeleton), and constants 5/03/26
#Version 2: Finished setting up functions welcome text, and instructions. (Commited to github) 5/03/26
#Version 3: No code changes, just testing user input specifically on instructions 5/03/26
#Version 4: Finished game logic (Commited to github) 5/03/26
#Version 5: Completed the main loop that holds everything together
#Version 6: Quality of life features including clearing the terminal whenever necessary 


#Modules - These help with stuff that is important to this game
import random #Helps with randomizing the answers that the terminal clanker will choose form
import os #Helps with clearing text in necessary places to make the game easier to play 

# ======== Constants ======== #
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

MOVES = (ROCK, PAPER, SCISSORS) #This constant is for the possible move options

WIN_RULES = {    #This constant is for determining the winning rules which makes things way easier
    ROCK: SCISSORS, 
    PAPER: ROCK,
    SCISSORS: PAPER
}

POINTSPERWIN = 1 #This constant is for determining the amount of points per win and is modular

#This constant is for determining the amount of gamerounds and can be changeable for fun play!
GAMEROUNDS = 3

#Helper functions

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Main functions

def greeting_text(): #greets the terminal gamer accompanying welcome_text() 
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

def instructions(): # This helps the user with instructions
    while True:
        print("Wow, I thought everyone knew this game but very well!")
        print("\n Type rock, paper, or scissors as your options")
        print("\n Always remember, \n rock beats paper, \n paper beats scissors \n and scissors beats rock")
        print(f"\n If you win, you get 1 point, if you lose, your opponent will get 1 point and it is first to {GAMEROUNDS}!")

        player_choice = input("Hey are you ready to play? Please say yes or no to start! Or press M to return to the main menu! :  ").lower().strip()

        if player_choice in ['yes', 'y']:
            print("THEN LET's GET READY TO RUMBLE!!!!!")
            rps_game()

        elif player_choice in ['no', 'n']:
            print("Oh...... Another time then!")
            break
        elif player_choice in ['main', 'menu', 'm']:
            return main()
        else:
            print("sorry that's invalid, please press yes or no")
    
def rps_game(): #This is the thing that handles the logic of RPS game using the constants and stuff
    terminal_gamer_score = 0
    clanker_score = 0

    print(""" 
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░███████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░██████████
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░███████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░██████████
█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░███████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░██████████
█░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░████░░▄▀░░██████████
█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█████████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░██████████
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░██████████
█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█████████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░██████████
█░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░░░░░████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░░░░░█
█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░█
█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░░░░░████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░░░░░█
█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█████░░████░░░░░░█████████░░░░░░██░░░░░░█░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█████░░█
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█
█░░▄▀░░█████████░░▄▀░░███████████░░▄▀░░███░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀░░█████████
█░░▄▀░░░░░░░░░░█░░▄▀░░███████████░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░███████████░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░███████████░░▄▀░░███░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░░░░░░░░░▄▀░░█
█████████░░▄▀░░█░░▄▀░░███████████░░▄▀░░███████████░░▄▀░░█████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████████████░░▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░░░▄▀░░░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█░░░░░░░░░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████""")
    print(f" Welcome to rock, paper, scissors stadium! It is first to {GAMEROUNDS}! If you beat the clanker you have saved earth!")
    
    while terminal_gamer_score < GAMEROUNDS and clanker_score < GAMEROUNDS:
        player_move = input("Hey, choose rock, paper, scissors:     ").lower().strip()

        if player_move not in MOVES:
            print("Nah bro, choose a move that is real")
            continue

        clanker_move = random.choice(MOVES)
        print(f"Clanker chose: {clanker_move}")

        if player_move == clanker_move:
            print("It's a draw! Try again")

        elif WIN_RULES[player_move] == clanker_move:
            print("Hey, you won this round, a few more to go! :)")
            player_score += 1

        else:
            print("The damn clanker won this round :(")
            clanker_score += 1 

        print(f"\n ============= Player has {terminal_gamer_score} points - Clanker has {clanker_score} points =============")

    if terminal_gamer_score == GAMEROUNDS:
        print("Hey you did it! You saved the earth from the damn clankers")
    else:
        print("Oh no, the damn Clanker won the match! They took over earth ")

    try_again = input("\n Hey, wanna try save the earth from clankers again? (Yes/no) to respond!:      ")

    if try_again in ["yes", "y"]:
        print("Hey, let's try again whenever you're ready")
        return main()
        
    elif try_again in ["no", "n"]:
        print("Oh, see you another time then as if the earth doesn't matter!")
        return False
    
def main(): #This is the backbone of my entire RPS game without it, I would be cooked
    welcome_text()
    greeting_text()

    while True:
        game_choice = input("\n Welcome dear player, do you want to play the game? (yes/no) \n Press I for instructions!:   ").lower().strip()

        if game_choice in ["yes", "y"]:
            print("Let's get ready to rumble!!!!!")
            rps_game()
        elif game_choice in ["no", "n"]:
            print("oh sad...... See you next time :(")
            break
        elif game_choice in ["instructions", "i",]:
            instructions()

        else:
            print("Nah that's invalid..... Please use yes or no or whatever works I guess. ")

#main loop that starts the game otherwise I'd be cooked
main()