import json
import os

FEEDBACK_FILE = "database/feedback.json"

def load_feedbacks():
    if not os.path.exists(FEEDBACK_FILE):
        return []
    with open(FEEDBACK_FILE, "r") as f:
        return json.load(f)

def save_feedbacks(feedbacks):
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(feedbacks, f, indent=4)

def add_feedback():
    feedbacks = load_feedbacks()
    name = input("Enter your name: ")
    comment = input("Enter feedback: ")
    feedbacks.append({"name": name, "comment": comment})
    save_feedbacks(feedbacks)
    print("Feedback submitted successfully")

def view_feedbacks():
    feedbacks = load_feedbacks()
    if not feedbacks:
        print("No feedback found")
        return
    print("\n=== FEEDBACK LIST ===")
    for i, fb in enumerate(feedbacks, start=1):
        print(f"{i}. {fb['name']} → {fb['comment']}")

def feedback_menu():
    while True:
        print("\n=== FEEDBACK MENU ===")
        print("1. Add Feedback")
        print("2. View Feedbacks")
        print("3. Back")

        choice = input("Enter choice: ")
        if choice == "1":
            add_feedback()
        elif choice == "2":
            view_feedbacks()
        elif choice == "3":
            break
        else:
            print("Invalid choice Please try again.")
