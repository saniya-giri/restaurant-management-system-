import json
import os
import random
import getpass

STAFF_FILE = "database/staff.json"
     
def load_data(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        return []

def save_data(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def add_staff():
    staff = load_data(STAFF_FILE)

    staff_id = str(random.randint(1000000000, 9999999999))  # auto 10 digit ID

    name = input("Enter Staff Name: ")
    if len(name) < 2 or not name.isalpha():
        print("-------- invaild name --------")
        return

    age = input("Enter Age: ")
    if not age.isdigit():
        print(" -------- Age must contain only digit --------")
        return
    if not (18 <= int(age) <= 40):
        print("------ Age must be between 18 and 40 ------")
        return

    education = input("Enter Education: ")
    if education.strip() == "":
        print("------ Education cannot be empty --------")
        return

    address = input("Enter Address: ")
    if len(address) < 3 or not all(ch.isalpha() or ch.isspace() for ch in address):
        print("------ Address must be at least 3 letters and only alphabets -------")
        return

    email = input("Enter Email: ")
    if "@" not in email or "." not in email:
        print("------ Invalid Email format -------")
        return

    password = getpass.getpass("Enter Password (min 6 chars): ")
    if len(password) < 6:
        print("----- Password must be at least 6 characters -----")
        return

    new_staff = {
        "id": staff_id,
        "name": name,
        "age": age,
        "education": education,
        "address": address,
        "email": email,
        "password": password
    }

    staff.append(new_staff)
    save_data(STAFF_FILE, staff)
    print(f"\n------------ Staff registered successfully! (ID: {staff_id}) -----------\n")

def view_staff():
    staff = load_data(STAFF_FILE)
    if not staff:
        print("\n----------- No staff found. Please add staff first ----------\n")
        return

    print("\n======================== STAFF LIST =========================")
    print("{:<12} {:<15} {:<5} {:<15} {:<20} {:<20}".format(
        "ID", "Name", "Age", "Education", "Address", "Email"
    ))
    print("---------------------------------------------------------------")
    for s in staff:
        print("{:<12} {:<15} {:<5} {:<15} {:<20} {:<20}".format(
            s["id"], s["name"], s["age"], s["education"], s["address"], s["email"]
        ))
    print("===============================================================\n")

def update_staff():
    staff = load_data(STAFF_FILE)
    if not staff:
        print("\n----------- No staff found. Please add staff first ------------\n")
        return

    staff_id = input("Enter Staff ID to update: ")
    for s in staff:
        if s["id"] == staff_id:
            new_name = input("Enter new Name: ")
            if len(new_name) >= 2 and new_name.isalpha():
                s["name"] = new_name

            new_age = input("Enter new Age: ")
            if new_age.isdigit() and 18 <= int(new_age) <= 40:
                s["age"] = new_age

            new_edu = input("Enter new Education: ")
            if new_edu.strip() != "":
                s["education"] = new_edu

            new_addr = input("Enter new Address: ")
            if len(new_addr) >= 3 and all(ch.isalpha() or ch.isspace() for ch in new_addr):
                s["address"] = new_addr

            new_email = input("Enter new Email: ")
            if "@" in new_email and "." in new_email:
                s["email"] = new_email

            new_pass = getpass.getpass("Enter new Password: ")
            if len(new_pass) >= 6:
                s["password"] = new_pass

            save_data(STAFF_FILE, staff)
            print("\n--------- Staff updated successfully -----------\n")
            return
    print("\n----------- Staff not found -----------\n")

def remove_staff():
    staff = load_data(STAFF_FILE)
    if not staff:
        print("\n\---------- No staff found. Please add staff first -----------\n")
        return

    staff_id = input("Enter Staff ID to delete: ")
    update_staff = [s for s in staff if s["id"] != staff_id]
    if len(update_staff) == len(staff):
        print("\n----------- Staff not found ---------\n")
    else:
        save_data(STAFF_FILE, update_staff)
        print("\n-------- Staff deleted successfully ----------\n")

def manage_staff():
    while True:
        print("\n=============== MANAGE STAFF ===============")
        print("1. Add Staff")
        print("2. View Staff")
        print("3. Update Staff")   
        print("4. Remove Staff")
        print("5. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            add_staff()
        elif choice == "2":
            view_staff()
        elif choice == "3":
            update_staff()   
        elif choice == "4":
            remove_staff()
        elif choice == "5":
            print("Back to Dashboard")
            break
        else:
            print("Invalid choice")
