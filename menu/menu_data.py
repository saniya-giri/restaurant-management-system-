import json
import os

MENU_FILE = "database/menu.json"

def load_menu():
    if not os.path.exists(MENU_FILE):
        return []
    with open(MENU_FILE, "r") as f:
        return json.load(f)

def save_menu(data):
    folder = os.path.dirname(MENU_FILE)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(MENU_FILE, "w") as f:
        json.dump(data, f, indent=4)

def view_menu():
    menu = load_menu()
    if not menu:
        print("\n------ Menu is empty ------")
    else:
      print("\n==================== FOOD MENU =====================")

    print("=======================================================")
    print("| ID   |     Food Name              | Price  |")
    print("=======================================================")

    for item in menu:
        print(
        f"|{item['id']:<4} "
        f"| {item['name']:<22} "
        f"| ₹{item['price']:<5} |"
    )
    print("========================================================")

def add_item():
    menu = load_menu()
    new_id = max([m["id"] for m in menu], default=0) + 1
    name = input("Enter Dish Name: ")
    price = int(input("Enter Price: "))
    menu.append({"id": new_id, "name": name, "price": price})
    save_menu(menu)
    print("Menu item added successfully!")

def update_item():
    menu = load_menu()
    view_menu()
    item_id = int(input("Enter Dish ID to update: "))
    for m in menu:
        if m["id"] == item_id:
            m["name"] = input("Enter New Dish Name: ")
            m["price"] = int(input("Enter New Price: "))
            save_menu(menu)
            print("Menu item updated successfully!")
            return
    print("Dish not found!")

def delete_item():
    menu = load_menu()
    view_menu()
    item_id = int(input("Enter Dish ID to delete: "))
    new_menu = [m for m in menu if m["id"] != item_id]
    save_menu(new_menu)
    print(" Menu item deleted successfully!")
