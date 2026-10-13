import json
import os
import msvcrt

ADMIN_FILE = "database/admin.json"
STAFF_FILE = "database/staff.json"

def load_data(file):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)

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
            character = key.decode("utf-8", errors="ignore")
            if character:
                password += character
                print("*", end="", flush=True)
    return password

def admin_login():
    admin = load_data(ADMIN_FILE)
    if not admin:
        print("\n------------------------------------------")
        print("          Please Sign Up first")
        print("------------------------------------------")
        return False

    print("\n==================================================")
    print("================== ADMIN SIGN IN =================")
    print("==================================================\n")
    email = input("Enter your Email:- ")
    password = password_input("Enter your Password:- ")
    if (admin[0]["email"] == email and admin[0]["password"] == password):
        print("\n====================================")
        print("Admin Sign-In Successful")
        print("====================================")
        print("Welcome", admin[0]["name"])
        print("====================================\n")
        return email
    else:
        print("\n------------------------------------------")
        print("        Wrong Email or Password")
        print("------------------------------------------")
        return False


def staff_login():
    staff = load_data(STAFF_FILE)
    if not staff:
        return False
    print("\n===================================================")
    print("=================== STAFF SIGN IN =================")
    print("===================================================\n")

    email = input("Enter your Email:- ")
    password = password_input("Enter your Password:- ")
    for member in staff:
        if (member["email"] == email and member["password"] == password):
            print("\n====================================")
            print("       Staff Sign-In Successful")
            print("====================================")
            print("Welcome", member["name"])
            print("Staff ID:", member["staff_id"])
            print("====================================\n")
            return email
    print("------------------------------------------")
    print("        Wrong Email or Password")
    print("------------------------------------------")
    return False


