import json
import os

FEEDBACK_FILE = "database/feedback.json"

def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return []
    try:
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_feedback(data):
    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=4)

def view_feedback():
    feedbacks = load_feedback()
    if not feedbacks:
        print("No feedback found!")
        return

    print("\n==================== FEEDBACK LIST ====================")
    print("{:<6} {:<15} {:<8} {:<40}".format("ID", "Name", "Rating", "Comment"))
    print("-------------------------------------------------------")
    for f in feedbacks:
        print("{:<6} {:<15} {:<8} {:<40}".format(f['id'], f['name'], f['rating'], f['comment']))
    print("=======================================================\n")

def add_feedback():
    feedbacks = load_feedback()
    fb_id = str(len(feedbacks) + 1).zfill(3)  
    name = input("Enter Customer Name: ")
    rating = input("Enter Rating (1-5): ")
    comment = input("Enter Feedback Comment: ")

    new_feedback = {"id": fb_id, "name": name, "rating": rating, "comment": comment}
    feedbacks.append(new_feedback)
    save_feedback(feedbacks)
    print(f"Feedback submitted successfully by {name}!")

def delete_feedback():
    feedbacks = load_feedback()
    fb_id = input("Enter Feedback ID to delete: ")
    updated_feedbacks = [f for f in feedbacks if f["id"] != fb_id]
    if len(updated_feedbacks) == len(feedbacks):
        print("Feedback not found!")
    else:
        save_feedback(updated_feedbacks)
        print(f" Feedback {fb_id} deleted successfully!")

def feedback_management():
    while True:
        print("\n========== FEEDBACK MANAGEMENT ==========")
        print("1. View Feedback")
        print("2. Add Feedback")
        print("3. Delete Feedback")
        print("4. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            view_feedback()
        elif choice == "2":
            add_feedback()
        elif choice == "3":
            delete_feedback()
        elif choice == "4":
            print("Back to Admin Dashboard")
            break
        else:
            print("Invalid choice! Try again.")
