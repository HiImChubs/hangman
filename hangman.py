#Hangman.py
#Connor Whiteside


limit = 6

def start_screen():
    print("""



 _    _          _                                             _                                                                 
| |  | |        | |                                           | |                                                                  
| |  | |   ___  | |   ___    ___    _ __ ___     ___          | |_    ___        
| |/\| |  / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \         | __|  / _ \      
\  /\  / |  __/ | | | (__  | (_) | | | | | | | |  __/         | |_  | (_) |     
 \/  \/   \___| |_|  \___|  \___/  |_| |_| |_|  \___|          \__|  \___/      
                                                                                                                          
 _____                               _          _   _            
|  __ \                             | |        | | | |           
| |  \/_   _  ___  ___ ___    __ _  | |     ___| |_| |_ ___ _ __ 
| | __| | | |/ _ \/ __/ __|  / _` | | |    / _ \ __| __/ _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | (_| | | |___|  __/ |_| ||  __/ |   
 \____/\__,_|\___||___/___/  \__,_| \_____/\___|\__|\__\___|_|   
                                                                 
                                                                                                                                                                                       
    """)
def get_puzzle():
    return "hangman"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess(name):
    print()
    guess = input("Enter a letter " + name +": ")
    print()
    return guess

def display_board(solved):
    print(solved)

def play_again():
    while True:
        print()
        decision = input("Congrats, YOU WON, Would you like to play again? (y/n) ")
        decision = decision.lower()
        print()
        
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            print()

def show_result():
    print("""
 _____   _                       _               _____        
|_   _| | |                     | |             |  ___|        
  | |   | |__     __ _   _ __   | | __  ___     | |_ ___  _ __ 
  | |   | '_ \   / _` | | '_ \  | |/ / / __|    |  _/ _ \| '__|
  | |   | | | | | (_| | | | | | |   <  \__ \    | || (_) | |   
  \_/   |_| |_|  \__,_| |_| |_| |_|\_\ |___/    \_| \___/|_|   

 _____   _                   _                 
| ___ \ | |                 (_)                
| |_/ / | |   __ _   _   _   _   _ __     __ _
|  __/  | |  / _` | | | | | | | | '_ \   / _` |
| |     | | | (_| | | |_| | | | | | | | | (_| |
\_|     |_|  \__,_|  \__, | |_| |_| |_|  \__, |
                      __/ |               __/ |
                     |___/               |___/ 

 Made by Connor   """)              
def play():
    print("What is your name")
    name = input()
    tries = 0
    start_screen()
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)

    print(solved)

    while solved != puzzle and tries < limit:
        letter = get_guess(name)
        letter = letter.lower()
        if letter not in puzzle:
            tries += 1
            
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)
playing = True
while playing:
    play()
    playing = play_again()

show_result()
