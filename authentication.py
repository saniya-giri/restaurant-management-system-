users = {
    "admin": {
        "password": "admin123",
        "role": "Admin"
    },

    "waitstaff": {
        "password": "staff123",
        "role": "Waitstaff"
    }
}

def login():
    print("\n================================")
    print("     RESTAURANT MANAGEMENT")
    print("          USER LOGIN")
    print("================================")

    attempts = 3

    while attempts > 0:

        username = input("\nEnter Username: ")
        password = input("Enter Password: ")

        if username in users:

            if users[username]["password"] == password:

                role = users[username]["role"]

                print("\nLogin Successful!")
                print("Username :", username)
                print("Role     :", role)

                if role == "Admin":
                    admin_menu()

                elif role == "Waitstaff":
                    waitstaff_menu()

                return

            else:
                attempts -= 1
                print("\nWrong Password!")
                print("Attempts left:", attempts)

        else:
            attempts -= 1
            print("\nUsername not found!")
            print("Attempts left:", attempts)

    print("\nToo many failed attempts.")
    print("Access Denied.")

def admin_menu():
    print("\n========== ADMIN ACCESS ==========")
    print("1. Manage Menu")
    print("2. Manage Orders")
    print("3. Manage Tables")
    print("4. Generate Bills")
    print("5. Manage Users")
    print("6. Logout")

def waitstaff_menu():
    print("\n======== WAITSTAFF ACCESS ========")
    print("1. Take Order")
    print("2. View Orders")
    print("3. Table Booking")
    print("4. View Tables")
    print("5. Logout")

login()