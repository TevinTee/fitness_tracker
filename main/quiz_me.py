import json;
import os;

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
    file_path = "profiles.json"

    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            profiles = json.load(json_file)  # Load existing profiles
    else:
        profiles = []  # Initialize as an empty list if file doesn't exist

    if any(profile["username"] == username for profile in profiles):
        print(f"\nError: The username '{username}' is already taken. Please try a different one.")
        username = input("Username: ")

    # Add the new profile to the list
    profiles.append({"name": name, "username": username})
    
    # Save the updated profiles back to the JSON file
    with open(file_path, "w") as json_file:
        json.dump(profiles, json_file, indent=4)

    print(f"\nWelcome {username}. Your profile has been saved.")


# write code for different game modes, check score, start game...
def play():

    print("Starting game...")
    return play()


def clear_json_file(file_path):
    # Overwrite the JSON file with an empty list
    with open(file_path, "w") as json_file:
        json.dump([], json_file, indent=4)
    print(f"The file '{file_path}' has been cleared.")

# File path to the JSON file
file_path = "profiles.json"

# Clear the JSON file
clear_json_file(file_path)

if __name__ == "__main__":
    run_game()