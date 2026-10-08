import json
import os
import random
import msvcrt

ADMIN_FILE = "database/admin.json"
STAFF_FILE = "database/staff.json"
def load_data(file):
    if not os.path.exists(file):
        return []

    with open(file, "r") as f:
        return json.load(f)

def save_data(file, data):
    folder = os.path.dirname(file)
    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def password_input(message):
    print(message, end="", flush=True)
    password = ""
    while True:
        key = msvcrt.getch()

        if key == b"\r":
            print()
            break

        elif key == b"\x08":
            if password:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            try:
                character = key.decode("utf-8")
                password += character
                print("*", end="", flush=True)
            except:
                pass
    return password

def name(user_name):
    return (
        user_name.replace(" ", "").isalpha()
            and len(user_name.replace(" ", "")) >= 3)

def age(user_age):
    return ( user_age.isdigit()
            and 18 <= int(user_age) <= 60)

def address(user_address):
    return (user_address.replace(" ", "").isalpha()and len(user_address.replace(" ", "")) >= 5)

def validate_email(user_email):
    return "@" in user_email   and "." in user_email

def generate_staff_id(staff):
    while True:
        staff_id = str( random.randint(1000000000, 9999999999))
        if all(member["staff_id"] != staff_id for member in staff):
            return staff_id

def admin_signup():
    admin = load_data(ADMIN_FILE)
    if len(admin) >= 1:
        print("\n---------- Admin already registered -----------")
        return

    print("\n==================================================")
    print("================= ADMIN SIGN UP =================")
    print("==================================================\n")

    user_name = input("Enter your Name:- ")
    while not name(user_name):
        print("----- Invalid name -----")
        user_name = input("Enter your Name:- ")

    user_age = input("Enter your Age:- ")
    while not age(user_age):
        print("---- Age must be between 18 and 60 ----")
        user_age = input("Enter your Age:- ")

    qualification = input("Enter Qualification:- ")

    user_address = input("Enter your Home Address:- ")
    while not address(user_address):
        print("----- Invalid address -----")
        user_address = input("Enter your Home Address:- ")
        
    email_id = input("Enter your Email_id:- ")
    while not validate_email(email_id):
        print("------- Invalid email_id -------")
        email_id = input("Enter your Email_id:- ")

    password = password_input("Enter Password:- ")
    while len(password) < 8:
        print("---- Password must be at least 8 characters ----")
        password = password_input("Enter Password:- ")

    admin_data = {
        "name": user_name,
        "age": int(user_age),
        "qualification": qualification,
        "address": user_address,
        "email": email_id,
        "password": password
    }
    save_data(ADMIN_FILE,[admin_data])
    print("\n==========================================")
    print("Admin registered successfully")
    print("==========================================\n")

def staff_signup():
    staff = load_data(STAFF_FILE)
    if len(staff) >= 10:
        print("\n---------- Staff limit reached (10) ----------" )
        return
    
    print("\n===================================================")
    print("================= STAFF SIGN UP ==================")
    print("===================================================\n")

    user_name = input("Enter your Name:- ")
    while not name(user_name):
        print("----- Invalid name -----")
        user_name = input("Enter your Name:- ")

    user_age = input("Enter your Age:- ")

    while not age(user_age):
        print("----- Age must be between 18 and 60 -----")
        user_age = input("Enter your Age:- ")

    qualification = input("Enter your Qualification:- ")

    user_address = input("Enter your Home Address:- ")
    while not address(user_address):
        print("----- Invalid address -----")
        user_address = input("Enter your Home Address:- " )

    email_id =input("Enter your Email_id:- ")
    while not validate_email(email_id):
        print("----- Invalid email -----")
        email_id = input("Enter your Email_id:- ")

    password = password_input("Enter Password:- ")
    while len(password) < 8:
        print("---- Password must be at least 8 characters ----")
        password = password_input("Enter Password:- ")

    staff_id = generate_staff_id(staff)

    staff_data = {
        "staff_id": staff_id,
        "name": user_name,
        "age": int(user_age),
        "qualification": qualification,
        "address": user_address,
        "email": email_id,
        "password": password }
    staff.append(staff_data)
    save_data(STAFF_FILE,staff )
    print("\n===================================================")
    print("Staff registered successfully")
    print("Your Staff ID:", staff_id)
    print("===================================================")