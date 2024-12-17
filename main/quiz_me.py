def run_game():
    # main function for playing the game
    welcome = "Welcome to Quiz Me!"
    print(welcome)
    response = input("Would you like to create a profile? Yes or No\n")

    if response == "yes": 
        profile()
    else:
       play()

def profile():
    print("Create Profile:")
    name = input("Full Name: ")
    username = input("Username: ")

    print("Welcome " + username)

def play():
    print("Starting game...")
    return play

# code for the quiz_me.py goes here...



if __name__ == "__main__":
    run_game()