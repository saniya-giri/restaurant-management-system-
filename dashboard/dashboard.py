from menu import menu_data
from inventory import inventory
from orders.order import order_management
from billing.billing import billing
from tables.table import table_management
from auth.sign_up import staff_signup, load_data, save_data
from reports.report import reports
from feedback.feedbacks import feedback_management

STAFF_FILE = "database/staff.json"

def admin_dashboard(admin_name):

    while True:

        print("\n=============================================================")
        print("======================== ADMIN DASHBOARD ====================")
        print("=============================================================")
        print(f"Welcome, {admin_name}")
        print("-------------------------------------------------------------")
        print("1. Menu Management")
        print("2. Staff Management")
        print("3. Order Management")
        print("4. Table Management")
        print("5. Bill Management")
        print("6. Report Management")
        print("7. Feedback Management")
        print("8. Inventory Management")
        print("9. Logout")
        print("=============================================================")

        choice = input("Enter choice: ")
        if choice == "1":

            while True:

                print("\n================ MENU MANAGEMENT ===============")
                print("1. View Menu")
                print("2. Add Item")
                print("3. Update Item")
                print("4. Delete Item")
                print("5. Back")
                print("=================================================")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    menu_data.view_menu()

                elif sub_choice == "2":
                    menu_data.add_item()

                elif sub_choice == "3":
                    menu_data.update_item()

                elif sub_choice == "4":
                    menu_data.delete_item()

                elif sub_choice == "5":
                    break

                else:
                    print("--------- Invalid choice ---------")

        elif choice == "2":

            manage_staff()


        elif choice == "3":
            order_management()
            

        elif choice == "4":
            table_management()

        elif choice == "5":
            billing()
        elif choice == "6":
            reports()
        elif choice == "7":
            feedback_management()
        elif choice == "8":
            while True:
                print("\n================ INVENTORY MANAGEMENT ===============")
                print("1. Add Item")
                print("2. Update Item")
                print("3. Delete Item")
                print("4. View Inventory")
                print("5. Back")
                print("======================================================")

                sub_choice = input("Enter choice: ")
                if sub_choice == "1":
                    inventory.add_item()

                elif sub_choice == "2":
                    inventory.update_item()

                elif sub_choice == "3":
                    inventory.delete_item()

                elif sub_choice == "4":
                    inventory.view_inventory()

                elif sub_choice == "5":
                    break

                else:
                    print("--------- Invalid choice ---------")

        elif choice == "9":
            print("\n--------- Logging out... ---------")
            break
        else:
            print("\n--------- Invalid choice ---------")

def manage_staff():
    while True:
        print("\n============= MANAGE STAFF =============")
        print("1. Add Staff")
        print("2. View Staff")
        print("3. update Staff")
        print("4. Remove Staff")
        print("5. Back")
        print("========================================")

        choice = input("Enter yor choice: ")

        if choice == "1":
            staff_signup()

        elif choice == "2":
            staff = load_data(STAFF_FILE)
            if staff:
                print("\n================== STAFF LIST ==================")
                for member in staff:
                    print(
                        f"ID: {member.get('staff_id')} | "
                        f"Name: {member.get('name')} | "
                        f"Email: {member.get('email')}"
                    )
            else:
                print("\n--------- No staff registered yet. ---------")
        elif choice == "3":
            staff = load_data(STAFF_FILE)

            if not staff:
                print("\n--------- No staff available. ---------")
                continue

            staff_id = input("Enter Staff ID to update: ").strip()

            for member in staff:
                current_id = str(
                    member.get("staff_id", member.get("id", ""))
                )

                if current_id == staff_id:
                    print("\nLeave a field empty to keep the old value.")

                    name = input("Enter new Name: ").strip()
                    if name:
                        if len(name) >= 2 and name.replace(" ", "").isalpha():
                            member["name"] = name
                        else:
                            print("Invalid name! Old name retained.")

                    age = input("Enter new Age: ").strip()
                    if age:
                        if age.isdigit() and 18 <= int(age) <= 40:
                            member["age"] = age
                        else:
                            print("Invalid age! Old age retained.")

                    education = input("Enter new Education: ").strip()
                    if education:
                        member["education"] = education

                    address = input("Enter new Address: ").strip()
                    if address:
                        if len(address) >= 3:
                            member["address"] = address
                        else:
                            print("Invalid address! Old address retained.")

                    email = input("Enter new Email: ").strip()
                    if email:
                        if "@" in email and "." in email:
                            duplicate = any(
                                other is not member
                                and other.get("email", "").lower() == email.lower()
                                for other in staff
                            )

                            if duplicate:
                                print("Email already registered! Old email retained.")
                            else:
                                member["email"] = email
                        else:
                            print("Invalid email! Old email retained.")

                    save_data(STAFF_FILE, staff)
                    print("\n--------- Staff updated successfully! ---------")
                    break
            else:
                print("\n--------- Staff ID not found. ---------")

        elif choice == "4":
            staff = load_data(STAFF_FILE)
            if not staff:
                print("\n--------- No staff available. ---------")
                continue
            print("\n================== STAFF LIST ==================")
            for member in staff:
                print(
                    f"ID: {member.get('staff_id')} | "
                    f"Name: {member.get('name')} | "
                    f"Email: {member.get('email')}"
                )
            staff_id = input("\nEnter Staff ID to remove: ")
            new_staff = []
            found = False
            for member in staff:
                if member["staff_id"] == staff_id:
                    found = True
                else:
                    new_staff.append(member)
            if found:
                save_data(STAFF_FILE, new_staff)
                print("\n--------- Staff removed successfully ----------")
            else:
                print("\n--------- Staff ID not found ----------")

        elif choice == "5":
            break

        else:
            print("\n------------ Invalid choice ------------")

def staff_dashboard(staff_name):
    while True:
        print("\n=================================================")
        print("================ STAFF DASHBOARD ===============")
        print("=================================================")
        print(f"Welcome, {staff_name}")
        print("-------------------------------------------------")
        print("1. Take Customer Order")
        print("2. Generate Bill")
        print("3. View Menu")
        print("4. Book Table")
        print("5. Logout")
        print("=================================================")

        choice = input("Enter choice: ")

        if choice == "1":

            order_management(staff_name)

        elif choice == "2":

            orders = order_management()

            if not orders:

                print("\n--------- No orders found ---------")
                continue

            print("\n=========== AVAILABLE ORDERS ===========")

            for order in orders:

                print(
                    f"Order ID: {order.get('order_id')} | "
                    f"Staff: {order.get('staff')} | "
                    f"Total: ₹{order.get('total_bill')}"
                )

            order_id = input("\nEnter Order ID: ")

            billing.generate_bill(order_id)



        elif choice == "3":

            menu_data.view_menu()


    

        elif choice == "4":

            table_management.book_table(staff_name)


        elif choice == "5":

            print("\n--------- Logging out... ---------")
            break


        else:

            print("\n--------- Invalid choice ---------")

