import json
import time

import time
import threading
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

class Timer:
    def __init__(self):
        self.elapsed_time=0
        self.running = False
    def start(self):
        self.running = True
        while self.running and self.elapsed_time < 60:
            time.sleep(1)
            self.elapsed_time +=1
        if self.elapsed_time >=60:
            print("\nTime's up!")
            self.running = False

    def stop(self):
        self.running = False

    def adjust(self, seconds):
        self.elapsed_time = max(0, self.elapsed_time + seconds)


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
def load_questions(filename):
    return load_data(filename)

# Function to ask questions and evaluate answers
def ask_questions(questions, timer):
    score = 0
    start_time =time.time()
    timer_thread = threading.Thread(target=timer.start)
    timer_thread.start()

    for i, question in enumerate(questions, 1):
        if not timer.running:
            break
        print(f"Question {i}: {question['text']}")
        for option in question['options']:
            print(option)

        try:
            answer = input("Your answer: ").strip().lower()
            if not timer.running:
                break

            if answer == question['correct']:
                score += 1
                timer.adjust(-5)
            else:
                timer.adjust(5)
        except EOFError:
            break

    timer.stop()
    total_time = int(time.time() - start_time )
    print(f"\nQuiz finished.Total time: {total_time //60}:{total_time % 60}s")
    return score, total_time

# Function to save the user's score
def save_score(users, username, score, subject, total_time):
    users[username]['history'].append({
        'date': datetime.now().strftime("%Y-%m-%d"),
        'subject': subject,
        'score': score,
        'time': f"{total_time//60}:{total_time % 60}s"
    })
    save_data("users.json", users)




# Function to choose a subject
def choose_subject():
    display_subjects()
    subjects = {
        "1": "Mathematics",
        "2": "Python",
        "3": "Java",
        "4": "C",
        "5": "Cybersecurity"
    }
    choice = input("Your choice: ").strip()
    return subjects.get(choice, None)

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

    while True:
        display_welcome()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = manage_user(users)
            if username is None:
                continue  # Return to the main menu if login fails
            while True:
                action = user_menu()

                if action == "1":
                    print(f"\nHistory of {username}:")
                    for entry in users[username]['history']:
                        print(f"- Date: {entry['date']}, Subject: {entry['subject']}, Score: {entry['score']}, Time: {entry['time']}")

                elif action == "2":
                    subject = choose_subject()
                    if not subject:
                        print("Invalid subject. Please try again.")
                        continue

                    print("You have 60 seconds to complete the quiz.")
                    questions = load_questions(f"questions_{subject.lower()}.json")
                    timer= Timer()
                    score, total_time = ask_questions(questions, timer)
                    print(f"Your final score: {score}/{len(questions)}")
                    save_score(users, username, score, subject, total_time)
                    print("Thank you for participating!")
                elif action == "3":
                    print("Logging out...")
                    break
                else:
                    print("Invalid option. Please try again.")

        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
