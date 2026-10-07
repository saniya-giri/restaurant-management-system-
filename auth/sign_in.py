import json
import os
import msvcrt

from dashboard.dashboard import admin_dashboard, staff_dashboard
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
            try:
                character = key.decode("utf-8")
                password += character
                print("*", end="", flush=True)
            except:
                pass
    return password
def admin_login():
    admin = load_data(ADMIN_FILE)
    if not admin:
        print("------- Please Sign Up first -------")
        return False

    print("\n==================================================")
    print("================= ADMIN SIGN IN ==================")
    print("==================================================\n")

    name = input("Enter your Name:- ")
    password = password_input("Enter your Password:- ")
    if admin[0]["name"] == name and admin[0]["password"] == password:
        print("\n====================================")
        print("Admin sign-in Successful")
        print("====================================\n")
        admin_dashboard(name)
        return True
    else:
        print("----- Wrong Name or Password -----")
        return False
def staff_login():
    staff = load_data(STAFF_FILE)
    if not staff:
        print("-------- Please Sign Up first --------")
        return False
    print("\n===================================================")
    print("=================== STAFF SIGN IN =================")
    print("===================================================\n")

    name = input("Enter your Name:- ")
    password = password_input("Enter your Password:- ")
    for member in staff:
        if member["name"] == name and member["password"] == password:
            print("\n====================================")
            print("Staff sign-in Successful")
            print("Welcome", member["name"])
            print("Staff ID:", member["staff_id"])
            print("====================================\n")

            staff_dashboard(name)
            return True
    print("-------- Wrong Name or Password ---------")
    return False