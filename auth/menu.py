from auth import sign_in, sign_up
def show_menu():
    while True:
        print("\n===========================================================")
        print("========== Welcome to Restaurant Management System ==========")
        print("=============================================================")
        print("\n===================== AUTH MENU ===================")
        print("1. Admin")
        print("2. Staff")
        print("3. Exit")
        print("\n==========================================")
        choice = input("Enter choice: ")
        print("==========================================")

        if choice == "1":
            admin_menu()

        elif choice == "2":
            staff_menu()

        elif choice == "3":
            exit()

        else:
            print("\n--------- Invalid choice ---------")


def admin_menu():

    from auth.sign_up import load_data, ADMIN_FILE

    while True:
        admin = load_data(ADMIN_FILE)

        print("\n========================================================")
        print("========================= ADMIN ========================")
        print("========================================================\n")
        if len(admin) == 0:

            print("1. Sign Up")
            print("2. Back")
            print("\n==========================================")
            choice = input("Enter choice: ")
            print("==========================================\n")
            if choice == "1":
                sign_up.admin_signup()

            elif choice == "2":
                break

            else:
                print("----------- Invalid choice -----------")
        else:
            print("1. Sign In")
            print("2. Back")

            print("\n==========================================")
            choice = input("Enter choice:- ")
            print("==========================================\n")
            if choice == "1":
                sign_in.admin_login()
            elif choice == "2":
                break
            else:
                print("----------- Invalid choice -----------")

def staff_menu():

    while True:

        print("\n=================================================")
        print("===================== STAFF =====================")
        print("=================================================\n")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Back")
        print("==========================================")
        choice = input("Enter choice: ")
        print("==========================================")

        if choice == "1":

            sign_up.staff_signup()

        elif choice == "2":

            sign_in.staff_login()

        elif choice == "3":

            break

        else:

            print("---------- Invalid choice -----------")