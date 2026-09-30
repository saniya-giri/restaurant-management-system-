import json
import os
import random

FILE = "authentication/staff.json"

def load_staff():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as file:
        return json.load(file)

def save_staff(staff):
    with open(FILE, "w") as file:
        json.dump(staff, file, indent=4)

def generate_staff_id(staff):
    while True:
        staff_id = str(random.randint(1000000000, 9999999999)) 
        if all(member["staff_id"] != staff_id for member in staff):
            return staff_id

def staff_signup():
    staff = load_staff()
    if len(staff) >= 10:
        print("\n10 Staff already registered! Signup is closed.")
        return

    print("\n========== STAFF SIGN UP ==========")

    while True:
        name = input("Enter Name: ")
        if name.replace(" ", "").isalpha():
            break
        print("Please enter a valid name.")

    while True:
        age = input("Enter Age: ")
        if age.isdigit() and 18 <= int(age) <= 60:
            break
        print("Age must be between 18 and 60.")

    while True:
        education = input("Enter Education: ")
        if education.strip() != "":
            break
        print("Education cannot be empty.")

    while True:
        address = input("Enter Address: ")
        if len(address.strip()) >= 5:
            break
        print("Please enter a valid address.")

    while True:
        email = input("Enter Email: ")
        if "@" not in email or "." not in email:
            print("Please enter a valid email.")
            continue
        if any(member["email"].lower() == email.lower() for member in staff):
            print("This email is already registered.")
        else:
            break

    while True:
        password = input("Enter Password: ")
        if len(password) >= 6:
            break
        print("Password must be at least 6 characters.")

    staff_id = generate_staff_id(staff)

    new_staff = {
        "staff_id": staff_id,
        "name": name,
        "age": int(age),
        "education": education,
        "address": address,
        "email": email,
        "password": password
    }

    staff.append(new_staff)
    save_staff(staff)

    print("\nStaff Signup Successful")
    print("Your Unique Staff ID is:", staff_id)

def staff_signin():
    staff = load_staff()
    if len(staff) == 0:
        print("No Staff account exists. Please Sign Up first.")
        return False

    print("\n========== STAFF SIGN IN ==========")
    name = input("Enter Name: ")
    password = input("Enter Password: ")

    for member in staff:
        if member["name"] == name and member["password"] == password:
            print("\nStaff Login Successful")
            print("Welcome", member["name"])
            print("Staff ID:", member["staff_id"])
            staff_dashboard(member)  
            return True

    print("\nWrong Name or Password")
    return False

def staff_dashboard(member):
    while True:
        print(f"\n========== STAFF DASHBOARD ({member['name']}) ==========")
        print("1. View Assigned Tables")
        print("2. Take Customer Order")
        print("3. Generate Bill")
        print("4. Update Availability")
        print("5. Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            print("Showing assigned tables...")
        elif choice == "2":
            print("Taking customer order...")
        elif choice == "3":
            print("Generating bill...")
        elif choice == "4":
            print("Updating availability...")
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid Choice!")

def staff_menu():
    while True:
        print("\n========== STAFF ==========")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Back")

        choice = input("Enter Choice: ")

        if choice == "1":
            staff_signup()
        elif choice == "2":
            staff_signin()
        elif choice == "3":
            break
        else:
            print("Invalid Choice!")
