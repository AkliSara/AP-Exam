import json
from datetime import datetime

# Function to load data from a file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save data to a file
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to display a welcome message
def display_welcome():
    print("Welcome to the Computer Science Quiz!")
    print("1. Log in")
    print("2. Exit")

# Function to display subjects
def display_subjects():
    print("Choose a subject:")
    print("1. Mathematics")
    print("2. Python")
    print("3. Java")
    print("4. C")
    print("5. Cybersecurity")

# Function to manage users
def manage_user(users):
    username = input("Enter your username (name or ID): ").strip()

    if username in users:
        print(f"Welcome, {username}!")
        for _ in range(3):  # Limit login attempts
            password = input("Enter your password: ").strip()
            if password == users[username]['password']:
                print("Login successful!")
                return username
            else:
                print("Incorrect password. Please try again.")
        print("Too many failed attempts. Returning to the main menu.")
        return None
    else:
        print("New user detected. Creating profile.")
        password = input("Set a password: ").strip()
        if not password:  # Check if a valid password was entered
            print("The password cannot be empty. Please try again.")
            return None
        users[username] = {
            'password': password,
            'history': []
        }
        save_data("users.json", users)
        print("Profile created successfully!")
        return username

# Function to load questions from a file

# Function to ask questions and evaluate answers

# Function to save the user's score

# Function to choose a subject

# Function to display the user menu

# Main function
def main():
    users = load_data("users.json")

