import json
import os

MENU_FILE = "database/menu.json"

def load_menu():
    if not os.path.exists(MENU_FILE):
        return []
    try:
        with open(MENU_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_menu(data):
    with open(MENU_FILE, "w") as f:
        json.dump(data, f, indent=4)

def print_table(menu, category_name):
    if not menu:
        print(f"\nNo items found in {category_name}")
        return
    print(f"\n==================== {category_name} ====================")
    print("{:<8} {:<25} {:<10}".format("ID", "Name", "Price(₹)"))
    print("---------------------------------------------------------")
    for item in menu:
        print("{:<8} {:<25} {:<10}".format(item['id'], item['name'], item['price']))
    print("=========================================================\n")


def view_menu():
    menu = load_menu()

    if not menu:
        print(" ---------- Menu is empty ---------")
        return

    veg_items = [
        m for m in menu
        if m.get("category", "").lower() == "veg-food"
    ]

    nonveg_items = [
        m for m in menu
        if m.get("category", "").lower() == "non-veg-food"
    ]

    chinese_items = [
        m for m in menu
        if m.get("category", "").lower() == "chinese-food"
    ]

    drinks_items = [
        m for m in menu
        if m.get("category", "").lower() == "drinks"
    ]

    print_table(veg_items, "Veg-food")
    print_table(nonveg_items, "Non-Veg-food")
    print_table(chinese_items, "Chinese-food")
    print_table(drinks_items, "Drinks")

def add_item():
    menu = load_menu()
    item_id = input("Enter Item ID: ")
    name = input("Enter Dish Name: ")
    if len(name) < 2 or not name.isalpha():
            print("-------- invaild name --------")
            return
    price = (input("Enter Price: "))
    if not price.isdigit():
            print(" -------- invalide price --------")
            return
    category = input("Enter Category (Veg-food / Non-Veg-food / Chinese-food / Drinks): ")

    new_item = {"id": item_id, "name": name, "price": price, "category": category}
    menu.append(new_item)
    save_menu(menu)
    print("\n-----------------------------------------")
    print(f"Item '{name}' added successfully")
    print("-----------------------------------------\n")

def update_item():
    menu = load_menu()
    item_id = input("Enter Item ID to update: ")
    for item in menu:
        if item["id"] == item_id:
            new_name = input("Enter new Dish Name: ")
            new_price = float(input("Enter new Price: "))
            new_category = input("Enter new Category: ")
            item["name"] = new_name
            item["price"] = new_price
            item["category"] = new_category
            save_menu(menu)
            print("\n-----------------------------------------")
            print(f"Item {item_id} updated successfully")
            print("-----------------------------------------\n")
            return
    print("----------- Item not found -----------")

def delete_item():
    menu = load_menu()
    item_id = input("Enter Item ID to delete: ")
    updated_menu = [item for item in menu if item["id"] != item_id]
    if len(updated_menu) == len(menu):
        print("Item not found!")
    else:
        save_menu(updated_menu)
        print("-----------------------------------------")
        print(f"Item {item_id} deleted successfully!")
        print("-----------------------------------------\n")

def menu_management():
    while True:
        print("\n===============================================")
        print("=============== MENU MANAGEMENT ===============")
        print("===============================================\n")
        print("1. View Menu ")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Back")
        print("\n-------------------------------------")
        choice = input("Enter choice: ")
        print("--------------------------------------\n")

        if choice == "1":
            view_menu()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("-------- Back to Admin Dashboard ----------")
            break
        else:
            print("-------Invalid choice ------")
