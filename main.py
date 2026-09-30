from authentication.admin import admin_menu
from authentication.staff import staff_menu


def main():

    while True:

        print("\n================================")
        print("      RESTAURANT DASHBOARD")
        print("================================")

        print("1. Admin")
        print("2. Staff")
        print("3. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            admin_menu()

        elif choice == "2":

            staff_menu()

        elif choice == "3":

            print("Thank You!")
            break

        else:

            print("Invalid Choice!")


main()