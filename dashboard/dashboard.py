from menu import menu_data
from inventory import inventory
from orders.order import take_order, view_orders
from billing import billing
from tables import table

def admin_dashboard(admin_name):
    while True:
        print("\n=============================================================")
        print("======================== ADMIN DASHBOARD ====================")
        print("=============================================================\n")
        print("1. Billing")
        print("2. Inventory")
        print("3. Orders")
        print("4. Table Management")
        print("5. Menu Management")
        print("6. Reports")
        print("7. Logout")
        print("==========================================")
        choice = input("Enter choice:- ")
        print("==========================================\n")

        if choice == "1":
            from billing.billing import generate_bill
            order_id = input("Enter Order ID: ")
            generate_bill(order_id)

        elif choice == "2":
            print("\n====================================================")
            print("=============== INVENTORY MANAGEMENT ===============")
            print("====================================================\n")
            print("1. Add Item")
            print("2. Update Item")
            print("3. Delete Item")
            print("4. View Inventory")
            print("5. Back")
            print("==========================================")
            sub_choice = input("Enter choice:- ")
            print("==========================================\n")
            if sub_choice == "1":
                inventory.add_item()
            elif sub_choice == "2":
                inventory.update_item()
            elif sub_choice == "3":
                inventory.delete_item()
            elif sub_choice == "4":
                inventory.view_inventory()

        elif choice == "3":
            view_orders()

        elif choice == "4":
            print("\n================================================")
            print("=============== TABLE MANAGEMENT ===============")
            print("================================================\n")
            print("1. View Tables")
            print("2. Add Table")
            print("3. Update Table")
            print("4. Delete Table")
            print("5. Back")
            print("==========================================")
            sub_choice = input("Enter choice: ")
            print("==========================================\n")
            if sub_choice == "1":
                table.view_tables()
            elif sub_choice == "2":
                table.add_table()
            elif sub_choice == "3":
                table.update_table()
            elif sub_choice == "4":
                table.delete_table()

        elif choice == "5":
            print("\n===============================================")
            print("=============== MENU MANAGEMENT ===============")
            print("===============================================\n")
            print("1. View Menu")
            print("2. Add Item")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. Back")
            print("==========================================")
            sub_choice = input("Enter choice: ")
            print("==========================================\n")
            if sub_choice == "1":
                menu_data.view_menu()
            elif sub_choice == "2":
                menu_data.add_item()
            elif sub_choice == "3":
                menu_data.update_item()
            elif sub_choice == "4":
                menu_data.delete_item()

        elif choice == "6":
            billing.sales_report()

        elif choice == "7":
            print("Logging out...")
            break

        else:
            print("--------- Invalid choice ---------")

def staff_dashboard(staff_name):
    while True:
        print("\n================================================")
        print("=============== STAFF DASHBOARD ================")
        print("================================================\n")
        print("1. Take Customer Order")
        print("2. Generate Bill")
        print("3. View Menu")
        print("4. Book Table")
        print("5. Logout")
        print("==========================================")
        choice = input("Enter choice: ")
        print("==========================================\n")
        if choice == "1":
            take_order(staff_name)
        elif choice == "2":
            order_id = int(input("Enter Order ID: "))
            billing.generate_bill(order_id)
        elif choice == "3":
            menu_data.view_menu()
        elif choice == "4":
            table.book_table(staff_name)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("--------- Invalid choice ---------")
