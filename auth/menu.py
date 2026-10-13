from auth.sign_up import admin_signup, load_data
from auth.sign_in import admin_login, staff_login
from dashboard.dashboard import admin_dashboard, staff_dashboard
ADMIN_FILE = "database/admin.json"

def main_menu():
    while True:
        admin = load_data(ADMIN_FILE)
        if not admin:
            print("\n=====================================================")
            print("========== RESTAURANT MANAGEMENT SYSTEM ============")
            print("=====================================================\n")
            print("1. Admin Sign Up")
            print("2. Back")
            print("\n=====================================================")
            choice = input("Enter your choice: ")
            print("=====================================================\n")
            if choice == "1":
                admin_signup()
            elif choice == "2":
                print("---------- Exit ----------")
                break
            else:
                print("------------- Invalid choice -------------")
        else:
            login_menu()

def login_menu():
    while True:
        print("\n=====================================================")
        print("======================= LOGIN =======================")
        print("=====================================================\n")
        print("1. Admin Sign In")
        print("2. Staff Sign In")
        print("3. Exit")
        print("\n=====================================================")
        choice = input("Enter your choice: ")
        print("=====================================================\n")

        if choice == "1":
            admin_name = admin_login()
            if admin_name:
                admin_dashboard(admin_name)

        elif choice == "2":
            staff_name = staff_login

            if staff_name:
                staff_dashboard(staff_name)     
            else:
                print("\n---------- Please Sign Up first ----------")

        elif choice == "3":
            break

        else:
            print("\n------------ Invalid choice ------------")
