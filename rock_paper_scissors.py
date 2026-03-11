# ===================================== [Rock Paper Scissors HW] ===================================== #

#Solo homework project (NO TEACHER HELP ALLOWED and CLANKERGPT/MICROSLOP HELP!)


# VIEW MY VERSION HISTORY HERE OF CREATING THIS PROGRAM!

# ==== 5th March, 2026 Versions ==== #
#Version 1: Finished up helper functions, main functions (In a skeleton), and constants 
#Version 2: Finished setting up functions welcome text, and instructions. (Commited to github) 
#Version 3: No code changes, just testing user input specifically on instructions 
#Version 4: Finished game logic (Commited to github) 
#Version 5: Completed the main loop that holds everything together 5/03/26 added 6/03/26
# ==== 6th March, 2026 Versions ==== # 
#Version 6: Added some code comments so people can understand what I'm trying to do 6/03/26
#Version 7: Ran into a bug with player_score variable (FIXED)/(Commited to github) 6/03/26
#Version 8: Attempting quality of life changes to the game to make it easier to play and pick up(clear_terminal) COMPLETED 6/03/26 (COMMITED TO GITHUB)
#Version 9: Added a terminal response message before heading to instructions (forgot I deleted it) 6/03/26
#Version 10: Teeny Tiny change line 72 added a space to input message 
#Version 11: BIG UPDATE - Finally added quick moves for player to do (check line 36 for more info) and I have made the game easier to play (through clear text ofc) 
# ==== 7th March, 2026 Versions ==== # 
#Version 12: Fixed bug with variable name
#Version 13: Added "loading" gimmick like some games and latency when loading each round!
#Version 14: Continuing on version 13 with some stuff I missed
#Version 15: Teeny tiny update
#Version 16: Another teeny tiny update
#Version 17: Attempt of making the move rock available with r (For rock etc) Les go I did it!
#Version 18: Added a victory and losing animation
#Version 19: Added a few comments to parts I haven't explained how they work yet and a few renames
#Version 20: Added versions back since it looks weird on github
# ==== 11th March, 2026 Versions ==== # 
#Version 21: Changed the coding of the animations a bit to make it better using a list
#Small update


#Modules - These help with stuff that is important to this game especially helpful stuff
import random #Helps with randomizing the answers that the terminal clanker will choose form
import os #Helps with clearing text in necessary places to make the game easier to see without being cluttered
import time #Helps the user to see response message before clearing the terminal to the task
import string #Imports string module for a cool helper function
# ======== Constants ======== #
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

MOVES = (ROCK, PAPER, SCISSORS) #This constant is for the possible move options and how the terminal uses the random import to do a move

WIN_RULES = {    #This constant is for determining the winning rules which makes things way easier
    ROCK: SCISSORS, 
    PAPER: ROCK,
    SCISSORS: PAPER
}

MOVE_CONDITIONS = { #Makes it so that the player can quick press the letter that corresponds to the move (LES GO I FINALLY FIGURED IT OUT)
    "r": ROCK,
    "rock": ROCK,
    "p": PAPER,
    "paper": PAPER,
    "s": SCISSORS,
    "scissors": SCISSORS
}

POINTSPERWIN = 1 #This constant is for determining the amount of points per win and is modular
GAMEROUNDS = 5 #This constant is for determining the amount of gamerounds and can be changeable for fun play!

#Helper functions that help with quality of life in this program

def clear_terminal(): # clearing the terminal wherever necessary so it is much easier to play the game
    os.system('cls' if os.name == 'nt' else 'clear')

def cleaned_input(user_input:str) -> str: #Cleans input of a user #Borrowed from another school program I made with help of teacher
    cleaned = user_input.lower() #Uses .lower() to remove any capitals
    cleaned = cleaned.replace(" ", "") #Removes any weird spaces
    cleaned = cleaned.strip(string.punctuation) #Removes any unecessary punctuation
    return cleaned #Returns result

#Animation Functions

def victory_animation(): #Displays an 'animation' of the player winning the game
    winning = ["\n YOU WON!", "\n you won! :)"]
    for i in range(6):
        print(winning[i % 2])
        time.sleep(0.5)
        clear_terminal()
 
def loss_animation(): #Displays an 'animation' of the player losing the game
    losing = ["\n YOU LOST :(", "you lost :("]
    for i in range(6):
        print(losing[i % 2])
        time.sleep(0.5)
        clear_terminal()

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
    while True: #Wraps the instructions menu into a while true loop
        print("Wow, I thought everyone knew this game but very well!") #Instructions
        print("\n Type: \n r for rock, \n p for paper, \n s for scissors as your options") #Instructions
        print("\n Always remember, \n rock beats paper, \n paper beats scissors \n and scissors beats rock") #Instructions
        print(f"\n If you win, you get 1 point, if you lose, your opponent will get 1 point and it is first to {GAMEROUNDS}!") #Instructions on how to win

        player_choice = input("\n Hey are you ready to play? Please say yes or no to start! Or press M to return to the main menu! :  ").lower().strip() #Asks the user if they want to start/play/return to menu
        player_choice = cleaned_input(player_choice) 

        if player_choice in ['yes', 'y']: #If user's choice is yes or y it will load the game
            print("\n Let's go!!!!")
            time.sleep(1)
            clear_terminal()
            print("          \n        \n       Loading Game...............")
            time.sleep(1.5)
            clear_terminal()
            rps_game()

        elif player_choice in ['no', 'n']: #If user's choice is in no or n then it will exit the program
            print("Oh...... Another time then!")
            time.sleep(1.5)
            clear_terminal()
            print("          \n        \n       Exiting game........")
            time.sleep(1.5)
            clear_terminal()
            exit()
        elif player_choice in ['main', 'menu', 'm']: #If user's choice is in main, menu, or m then it will make them return to the main menu
            print("Play whenever you're ready!")
            time.sleep(1)
            clear_terminal()
            print("          \n        \n       Returning to menu.......")
            time.sleep(1.5)
            clear_terminal()
            return main()
        else: #Prompts the user to do a valid input
            print("sorry that's invalid, please press yes/no or M to return to menu.......")
    
def rps_game(): #This is the thing that handles the logic of RPS game using the constants and stuff
    terminal_gamer_score = 0 #Sets the player's score to zero every time
    jarvis_score = 0 #Sets clanker score to zero everytime

    print("""  
██████████████████████████████████████████████████████████████████████████████████████▀███████████████████████████
█▄─▄▄▀█▄─▄▄─█─▄▄▄▄███▀▀▀▀▀████─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─▀█▀─▄█▄─▄█▄─▀█▄─▄██▀▄─██▄─▄█████─▄▄▄▄██▀▄─██▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀█
██─▄─▄██─▄▄▄█▄▄▄▄─██████████████─████─▄█▀██─▄─▄██─█▄█─███─███─█▄▀─███─▀─███─██▀███─██▄─██─▀─███─█▄█─███─▄█▀██─▄─▄█
▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
███████████████████████████████████████████████████
█▄─█─▄█─▄▄▄▄█████▄─▄██▀▄─██▄─▄▄▀█▄─█─▄█▄─▄█─▄▄▄▄█░█
██▄▀▄██▄▄▄▄─███─▄█─███─▀─███─▄─▄██▄▀▄███─██▄▄▄▄─█▄█
▀▀▀▄▀▀▀▄▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▄▄▄▀▄▄▄▄▄▀▄▀ """) # Greets user with the RPS - TERMINAL GAMER VS JARVIS using fancy text!
    print(f"\n Welcome to rock, paper, scissors stadium! It is first to {GAMEROUNDS}! If you beat Jarvis then you are smarter than Iron Man!") # Shows the user the amount of rounds played to win
    
    while terminal_gamer_score < GAMEROUNDS and jarvis_score < GAMEROUNDS: #Wraps the whole game into a while loop so the game can keep going until it reaches GAMEROUNDS
        player_move = input(" \n Hey, choose r for rock, p for paper, s for scissors:     ").lower().strip()
        player_move = cleaned_input(player_move)

        if player_move in MOVE_CONDITIONS: #If player move is in the MOVE_CONDITIONS constant, then it will register as a valid input
            player_move = MOVE_CONDITIONS[player_move]

        else:
            print("\n          Nah bro, choose a move that is real") #Prompts the user to please pick a valid input then clears terminal to redo the loop
            time.sleep(1.5)
            print("          \n            \n       Try Again......")
            time.sleep(1.5)
            clear_terminal()
            continue

        jarvis_move = random.choice(MOVES) # This is how the terminal generates moves using the random module
        print(f" \n Jarvis chose:  {jarvis_move}")

        if player_move == jarvis_move: #When they both draw it won't count so it will keep playing
            print("\n It's a draw! Try again")
            time.sleep(1.5)
            print("\n Loading Next round.............")
            time.sleep(1.5)
            clear_terminal()

        elif WIN_RULES[player_move] == jarvis_move: # If the player does a move according to constant WIN_RULES and is part of the scenarios in WIN_RULES then they score a point against Jarvis
            print("\n Hey, you won this round, a few more to go! :)")
            terminal_gamer_score += POINTSPERWIN
            time.sleep(1.5)
            print("\n Loading next round...........")
            time.sleep(1.5)
            clear_terminal()

        else:
            print("\n Jarvis won this round ;)") # The opposite of the player winning according to comment on line 123
            jarvis_score += POINTSPERWIN
            time.sleep(1.5)
            print("\n Loading next round..........")
            time.sleep(1.5)
            clear_terminal()

        print(f"\n ============= Player has {terminal_gamer_score} points - Jarvis has {jarvis_score} points =============") # Shows the player what their score and Jarvis' score is

    if terminal_gamer_score == GAMEROUNDS: #If the player reaches the GAMEROUNDS, then the while loop is finished and displays the victory message
        print("\n Hey you did it! You beat Jarvis! :)")
        time.sleep(2)
        victory_animation()
    else:
        print("\n Jarvis won this game,") #If Jarvis reaches GAMEROUNDS, then the while loop is finished and displays that Jarvis won
        time.sleep(2)
        loss_animation()

    try_again = input("\n Hey, wanna try beat Jarvis again (Yes/no) to respond!:      ") #Asks the player if they want to try and win against them
    try_again = cleaned_input(try_again)

    if try_again in ["yes", "y"]: #Returns the player to main menu so they can play whenever they're ready
        print("Hey, let's try again whenever you're ready")
        time.sleep(1)
        print("Returning to menu........")
        time.sleep(2)
        clear_terminal()
        return True
        
    elif try_again in ["no", "n"]: #Breaks the loop because player doesn't want to play anymore 
        print("\n Well, Jarvis can play whenever you are around")
        time.sleep(3)
        print("\n Returning to menu....................")
        time.sleep(3)
        clear_terminal()
        return False
    else:
        print("\n Sorry, that's invalid please pick a valid option")
        time.sleep(2)
        clear_terminal()
        time.sleep(1)
    
def main(): #This is the backbone of my entire RPS game without it, I would be cooked
    while True: # Wraps everything in a loop
        welcome_text() #Greets user with welcome text function
        greeting_text() # Greets user with the greeting text function
    
        game_choice = input("\n Welcome dear player, do you want to play the game? (yes/no) or press I for instructions!:   ").lower().strip() # Prompts the user to press yes/no to start or leave game and pressing 'I' will lead to instructions
        game_choice = cleaned_input(game_choice)

        if game_choice in ["yes", "y"]: #If the user presses y or types yes then it will load the game
            print("\n               \n     Let's get ready to rumble!!!!!")
            time.sleep(1)
            clear_terminal()
            print("          \n        \n       Loading Game...............")
            time.sleep(1.5)
            clear_terminal()
            rps_game()
        elif game_choice in ["no", "n"]: #If the user presses n or types no then it will quit the game
            print("\n oh sad...... See you next time :(")
            time.sleep(1.5)
            clear_terminal()
            print("          \n         \n       Exiting game.....")
            time.sleep(1.5)
            clear_terminal()
            break
        elif game_choice in ["instructions", "i",]: #If the user presses I then it will allow them to view instructions
            print("See ya in game!")
            time.sleep(1)
            clear_terminal()
            print("          \n          \n      Loading Instructions..........")
            time.sleep(1.5)
            clear_terminal()
            instructions()

        else:
            print("\n Nah that's invalid..... Please use yes or no or whatever works I guess. ") #Prompts the user to do a valid option
            time.sleep(2)
            clear_terminal()

#main loop that starts the game otherwise I'd be cooked
main() 