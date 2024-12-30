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

# Function to load questions from a file

# Function to ask questions and evaluate answers

# Function to save the user's score

# Function to choose a subject

# Function to display the user menu
def user_menu():
    print("\nWhat would you like to do?")
    print("1. View history")
    print("2. Take a quiz")
    print("3. Log out")
    return input("Your choice: ").strip()

# Main function
def main():
    users = load_data("users.json")

    # ur turn now
