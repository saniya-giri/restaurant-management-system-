import json;
import os;
menu = {
    1: {"name": "Veg Burger", "price": 80},
    2: {"name": "Cheese Burger", "price": 100},
    3: {"name": "Paneer Burger", "price": 120},

    4: {"name": "Veg Pizza", "price": 150},
    5: {"name": "Cheese Pizza", "price": 180},
    6: {"name": "Paneer Pizza", "price": 200},

    7: {"name": "French Fries", "price": 70},
    8: {"name": "Peri Peri Fries", "price": 90},
    9: {"name": "Veg Momos", "price": 80},
    10: {"name": "Cheese Momos", "price": 110},

    11: {"name": "Veg Roll", "price": 80},
    12: {"name": "Paneer Roll", "price": 110},

    13: {"name": "Veg Sandwich", "price": 70},
    14: {"name": "Cheese Sandwich", "price": 90},

    15: {"name": "Cold Drink", "price": 40},
    16: {"name": "Lemonade", "price": 50},
    17: {"name": "Cold Coffee", "price": 80},

    18: {"name": "Ice Cream", "price": 60},
    19: {"name": "Chocolate Brownie", "price": 100}
}
def show_menu():
    print("\n========== FAST FOOD MENU ==========")

    for item_id, item in menu.items():
        print(item_id, ".", item["name"], "- ₹", item["price"])

def add_item():
    item_id = int(input("\nEnter Item ID: "))
    name = input("Enter Item Name: ")
    price = float(input("Enter Price: "))

    menu[item_id] = {
        "name": name,
        "price": price
    }

    print("Item added successfully!")


def update_item():
    show_menu()

    item_id = int(input("\nEnter Item ID to update: "))

    if item_id in menu:
        name = input("Enter New Item Name: ")
        price = float(input("Enter New Price: "))

        menu[item_id]["name"] = name
        menu[item_id]["price"] = price

        print("Item updated successfully!")

    else:
        print("Item not found!")

def delete_item():
    show_menu()

    item_id = int(input("\nEnter Item ID to delete: "))

    if item_id in menu:
        del menu[item_id]
        print("Item deleted successfully")

    else:
        print("Item not found")

def menu_handling():
    while True:

        print("\n========== MENU HANDLING ==========")
        print("1. Show Menu")
        print("2. Add Item")    
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            add_item()

        elif choice == "3":
            update_item()

        elif choice == "4":
            delete_item()

        elif choice == "5":
            print("Exiting Menu Handling...")
            break

        else:
            print("Invalid choice!")


menu_handling()#roehebejeudv3v3