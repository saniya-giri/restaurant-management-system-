import json
import os

FILE = "authentication/admin.json"

def load_admin():
    if not os.path.exists(FILE):
        return None
    with open(FILE, "r") as file:
        return json.load(file)

def save_admin(admin):
    with open(FILE, "w") as file:
        json.dump(admin, file, indent=4)

def admin_signup():
    if load_admin() is not None:
        print("Admin already registered")
        return

    print("\n========== ADMIN SIGN UP ==========")

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    education = input("Enter Education: ")
    address = input("Enter Address: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    admin = {
        "name": name,
        "age": int(age),
        "education": education,
        "address": address,
        "email": email,
        "password": password
    }

    save_admin(admin)
    print("\nAdmin Signup Successful")

def admin_signin():
    admin = load_admin()
    if admin is None:
        print("Admin account does not exist. Please Sign Up first.")
        return False

    print("\n========== ADMIN SIGN IN ==========")
    name = input("Enter Name: ")
    password = input("Enter Password: ")

    if name == admin["name"] and password == admin["password"]:
        print("\nAdmin Login Successful!")
        print("Welcome", admin["name"])
        admin_dashboard()
        return True

    print("\nWrong Name or Password")
    return False

def admin_dashboard():
    while True:
        print("\n========== ADMIN DASHBOARD ==========")
        print("1. Table Management")
        print("2. Menu Management")
        print("3. Order Management")
        print("4. Payment & Billing")
        print("5. Feedback System")
        print("6. Staff Schedule")
        print("7. Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            print("Table Management Module")
        elif choice == "2":
            print("Menu Management Module")
        elif choice == "3":
            print(" Order Management Module")
        elif choice == "4":
            print("Payment & Billing Module")
        elif choice == "5":
            print("Feedback System Module")
        elif choice == "6":
            print(" Staff Schedule Module")
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("Invalid Choice!")

def admin_menu():
    while True:
        admin = load_admin()
        print("\n========== ADMIN ==========")

        if admin is None:
            print("1. Sign Up")
            print("2. Sign In")
            print("3. Back")
        else:
            print("1. Sign In")
            print("2. Back")

        choice = input("Enter Choice: ")

        if admin is None:
            if choice == "1":
                admin_signup()
            elif choice == "2":
                admin_signin()
            elif choice == "3":
                break
            else:
                print("Invalid Choice")
        else:
            if choice == "1":
                admin_signin()
            elif choice == "2":
                break
            else:
                print("Invalid Choice")
