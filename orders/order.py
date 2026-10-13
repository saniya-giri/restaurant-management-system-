import json
import os
import uuid


ORDERS_FILE = "database/orders.json"
MENU_FILE = "database/menu.json"



def load_orders():

    if not os.path.exists(ORDERS_FILE):
        return []

    try:

        with open(ORDERS_FILE, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:

        return []


def save_orders(data):

    with open(ORDERS_FILE, "w") as f:
        json.dump(data, f, indent=4)



def load_menu():

    if not os.path.exists(MENU_FILE):
        return []

    try:

        with open(MENU_FILE, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:

        return []

def print_table(menu, category_name):

    if not menu:
        return

    print(f"\n==================== {category_name} ====================")

    print(
        "{:<6} {:<25} {:<10}".format(
            "ID",
            "Name",
            "Price(₹)"
        )
    )

    print("---------------------------------------------------------")

    for item in menu:

        print(
            "{:<6} {:<25} {:<10}".format(
                item["id"],
                item["name"],
                item["price"]
            )
        )

    print("=========================================================\n")


def show_menu():

    menu = load_menu()

    if not menu:
        print("Menu is empty!")
        return

  
    categories = {}

    for m in menu:
        category = m.get("category", "Other")

        if category not in categories:
            categories[category] = []

        categories[category].append(m)

    for category_name, items in categories.items():
        print_table(items, category_name)


def view_orders():

    orders = load_orders()

    if not orders:

        print("No orders found!")
        return

    print("\n==================== ORDERS LIST ====================")

    print(
        "{:<12} {:<10} {:<20} {:<10} {:<12} {:<12}".format(
            "Order ID",
            "Table",
            "Dish",
            "Qty",
            "Status",
            "Payment"
        )
    )

    print("------------------------------------------------------")

    for o in orders:

        print(
            "{:<12} {:<10} {:<20} {:<10} {:<12} {:<12}".format(
                o.get("id"),
                o.get("table_id"),
                o.get("dish"),
                o.get("quantity"),
                o.get("status"),
                o.get("payment_status")
            )
        )

    print("======================================================\n")



def take_order(staff_name):

    orders = load_orders()

    order_id = str(uuid.uuid4())[:8]

  
    show_menu()

    table_id = input("Enter Table ID: ")

    dish_id = input("Enter Dish ID from menu: ")

    quantity = input("Enter Quantity: ")

    menu = load_menu()

    dish_name = None
    dish_price = 0

    for item in menu:

        if str(item["id"]) == str(dish_id):

            dish_name = item["name"]
            dish_price = item["price"]

            break

    if not dish_name:

        print("Invalid Dish ID! Order cancelled.")
        return

  
    try:
        total_bill = int(dish_price) * int(quantity)
    except ValueError:
        print("Invalid quantity!")
        return

    new_order = {

        "id": order_id,
        "order_id": order_id,
        "table_id": table_id,
        "dish": dish_name,
        "quantity": quantity,
        "staff": staff_name,
        "price": dish_price,
        "total_bill": total_bill,
        "status": "Pending",
        "payment_status": "Unpaid"
    }

    orders.append(new_order)

    save_orders(orders)

    print("\n==============================================")
    print("          ORDER ADDED SUCCESSFULLY")
    print("==============================================")
    print("Order ID:", order_id)
    print("Staff:", staff_name)
    print("Table:", table_id)
    print("Dish:", dish_name)
    print("Quantity:", quantity)
    print("Total Bill: ₹", total_bill)
    print("==============================================\n")


def add_order():

    staff_name = input("Enter Staff Name: ")

    take_order(staff_name)


def update_order():
    orders = load_orders()

    if not orders:
        print("No orders found! Please add an order first.")
        return

    order_id = input("Enter Order ID to update: ").strip()

    for o in orders:
        if str(o.get("id")) == order_id:

            new_quantity = input("Enter new Quantity: ").strip()

            if not new_quantity.isdigit() or int(new_quantity) <= 0:
                print("Invalid quantity! Enter a number greater than 0.")
                return

            new_status = input(
                "Enter new Status (Pending/Completed): "
            ).strip().capitalize()

            if new_status not in ["Pending", "Completed"]:
                print("Invalid status!")
                return

            o["quantity"] = int(new_quantity)
            o["total_bill"] = int(o["price"]) * int(new_quantity)
            o["status"] = new_status

            save_orders(orders)

            print(f"Order {order_id} updated successfully!")
            print("New Total Bill: ₹", o["total_bill"])
            return

    print("Order not found! Please enter a valid Order ID.")

def delete_order():
    orders = load_orders()

    if not orders:
        print("No orders found! Please add an order first.")
        return

    order_id = input("Enter Order ID to delete: ").strip()

    updated_orders = [
        o for o in orders
        if str(o.get("id")) != order_id
    ]

    if len(updated_orders) == len(orders):
        print("Order not found! Please enter a valid Order ID.")
        return

    save_orders(updated_orders)
    print(f"Order {order_id} deleted successfully!")


def order_management():

    while True:

        print("\n========== ORDER MANAGEMENT ==========")
        print("1. View Orders")
        print("2. Add Order")
        print("3. Update Order")
        print("4. Delete Order")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            view_orders()

        elif choice == "2":

            add_order()

        elif choice == "3":

            update_order()

        elif choice == "4":

            delete_order()

        elif choice == "5":

            print("Back to Admin Dashboard")
            break

        else:

            print("Invalid choice! Try again.")