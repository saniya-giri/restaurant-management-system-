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

    if folder and not os.path.exists(folder):
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

        elif key in (b"\x00", b"\xe0"):
            msvcrt.getch()

        else:
            try:
                character = key.decode("utf-8")

                if character.isprintable():
                    password += character
                    print("*", end="", flush=True)

            except UnicodeDecodeError:
                pass

    return password


def name(user_name):
    user_name = user_name.strip()

    return (
        len(user_name.replace(" ", "")) >= 3
        and user_name.replace(" ", "").isalpha()
    )


def age(user_age):
    return (
        user_age.isdigit()
        and 18 <= int(user_age) <= 60
    )

def address(user_address):
    user_address = user_address.strip()
    return len(user_address) >= 5


def validate_email(user_email):
    user_email = user_email.strip()

    if " " in user_email:
        return False

    if user_email.count("@") != 1:
        return False

    email_parts = user_email.split("@")

    return (
        len(email_parts[0]) > 0
        and "." in email_parts[1]
        and not email_parts[1].startswith(".")
        and not email_parts[1].endswith(".")
    )


def check_email(email_id):
    email_id = email_id.strip().lower()

    admin = load_data(ADMIN_FILE)
    staff = load_data(STAFF_FILE)

    for member in admin + staff:
        if member["email"].strip().lower() == email_id:
            return True

    return False


def generate_staff_id(staff):
    while True:
        staff_id = str(random.randint(1000000000, 9999999999))

        if all(
            member["staff_id"] != staff_id
            for member in staff
        ):
            return staff_id

def admin_signup():
    admin = load_data(ADMIN_FILE)

    if len(admin) >= 1:
        print("\n---------- Admin already registered ----------")
        return False

    print("\n==================================================")
    print("================= ADMIN SIGN UP =================")
    print("==================================================\n")

    user_name = input("Enter your Name:- ").strip()
    while not name(user_name):
        print("----- Invalid name -----")
        user_name = input("Enter your Name:- ").strip()

    user_age = input("Enter your Age:- ").strip()
    while not age(user_age):
        print("---- Age must be between 18 and 60 ----")
        user_age = input("Enter your Age:- ").strip()

    qualification = input("Enter Qualification:- ").strip()

    user_address = input("Enter your Home Address:- ").strip()
    while not address(user_address):
        print("----- Address must contain at least 5 characters -----")
        user_address = input("Enter your Home Address:- ").strip()

    email_id = input("Enter your Email ID:- ").strip().lower()

    while not validate_email(email_id) or check_email(email_id):
        if not validate_email(email_id):
            print("------- Invalid email ID -------")
        else:
            print("------- This email is already registered -------")

        email_id = input("Enter your Email ID:- ").strip().lower()

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

    save_data(ADMIN_FILE, [admin_data])

    print("\n==========================================")
    print("Admin registered successfully")
    print("==========================================\n")

    return True


def staff_signup():
    staff = load_data(STAFF_FILE)

    if len(staff) >= 10:
        print("\n---------- Staff limit reached (10) ----------")
        return False

    print("\n===================================================")
    print("================= STAFF SIGN UP ==================")
    print("===================================================\n")

    user_name = input("Enter your Name:- ").strip()
    while not name(user_name):
        print("----- Invalid name -----")
        user_name = input("Enter your Name:- ").strip()

    user_age = input("Enter your Age:- ").strip()
    while not age(user_age):
        print("----- Age must be between 18 and 60 -----")
        user_age = input("Enter your Age:- ").strip()

    qualification = input("Enter your Qualification:- ").strip()

    user_address = input("Enter your Home Address:- ").strip()
    while not address(user_address):
        print("----- Address must contain at least 5 characters -----")
        user_address = input("Enter your Home Address:- ").strip()

    email_id = input("Enter your Email ID:- ").strip().lower()
    while not validate_email(email_id) or check_email(email_id):
        if not validate_email(email_id):
            print("------- Invalid email ID -------")
        else:
            print("------- This email is already registered -------")
        email_id = input("Enter your Email ID:- ").strip().lower()

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
        "password": password
    }

    staff.append(staff_data)
    save_data(STAFF_FILE, staff)

    print("\n===================================================")
    print("Staff registered successfully")
    print("Your Staff ID:", staff_id)
    print("===================================================")

    return True

