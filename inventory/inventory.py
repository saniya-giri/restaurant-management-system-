import json
import os

INVENTORY_FILE = "database/inventory.json"

def load_inventory():
    """Load inventory data from JSON file"""
    if not os.path.exists(INVENTORY_FILE):
        return []
    with open(INVENTORY_FILE, "r") as f:
        return json.load(f)

def save_inventory(data):
    """Save inventory data to JSON file"""
    with open(INVENTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def view_inventory():
    """Display all inventory items"""
    inventory = load_inventory()
    if not inventory:
        print("\n------ Inventory is empty ------")
    else:
        print("\n================ INVENTORY ITEMS ================")
        for item in inventory:
            print(f"ID: {item['id']} | {item['name']} - {item['quantity']} {item['unit']}")

def add_item():
    inventory = load_inventory()
    print("\n")
    print("==============================================")
    print("                 ADD ITEM")
    print("==============================================")

    name = input("Enter raw material name: ")
    while name.strip() == "":
        print("----- Raw material name cannot be empty -----")
        name = input("Enter raw material name: ")

    while True:
        quantity = input("Enter quantity: ")
        if quantity.isdigit() and int(quantity) > 0:
            quantity = int(quantity)
            break

        print("----- Quantity must be a valid number -----")

    while True:
        unit = input("Enter unit (kg/litre/pcs): ").lower()
        if unit in ["kg", "litre", "pcs"]:
            break

        print("----- Invalid unit -----")
        print("Please enter kg, litre or pcs")

    if len(inventory) == 0:
        new_id = 1

    else:
        new_id = inventory[-1]["id"] + 1
    inventory.append({
        "id": new_id,
        "name": name,
        "quantity": quantity,
        "unit": unit
    })
    save_inventory(inventory)
    print("\n==============================================")
    print("        Item added successfully!")
    print("==============================================")
    print("Item ID:", new_id)
    print("Name:", name)
    print("Quantity:", quantity)
    print("Unit:", unit)
    print("==============================================")

def update_item():
    """Update quantity of an existing raw material"""
    inventory = load_inventory()
    item_id = int(input("Enter item ID to update: "))
    for item in inventory:
        if item["id"] == item_id:
            item["quantity"] = int(input("Enter new quantity: "))
            save_inventory(inventory)
            print("Item updated successfully!")
            return
    print("Item not found!")

def delete_item():
    """Delete a raw material from inventory"""
    inventory = load_inventory()
    item_id = int(input("Enter item ID to delete: "))
    new_inventory = [item for item in inventory if item["id"] != item_id]
    save_inventory(new_inventory)
    print("Item deleted successfully!")

RECIPE_MAP = {
    "Paneer Pizza": {"Paneer": 1, "Cheese": 1, "Flour": 1, "Vegetables": 1},
    "Veg Pizza": {"Cheese": 1, "Flour": 1, "Vegetables": 1},
    "Chicken Pizza": {"Chicken": 1, "Cheese": 1, "Flour": 1, "Vegetables": 1},
    "Veg Burger": {"Bread": 1, "Vegetables": 1, "Cheese": 1},
    "Paneer Burger": {"Bread": 1, "Paneer": 1, "Cheese": 1},
    "Chicken Burger": {"Bread": 1, "Chicken": 1, "Cheese": 1},
    "French Fries": {"Potatoes": 2, "Oil": 1},
    "Peri Peri Fries": {"Potatoes": 2, "Oil": 1, "Spices": 1},
    "Dal Rice": {"Rice": 1, "Spices": 1, "Vegetables": 1},
    "Paneer Butter Masala": {"Paneer": 2, "Spices": 1, "Vegetables": 1},
    "Chicken Biryani": {"Chicken": 2, "Rice": 2, "Spices": 1},
    "Mutton Biryani": {"Mutton": 2, "Rice": 2, "Spices": 1},
    "Cold Coffee": {"Milk": 1, "Coffee Powder": 1, "Ice Cream": 1},
    "Mango Shake": {"Milk": 1, "Fruits": 1, "Ice Cream": 1}
}


def reduce_inventory(dish_name):
    inventory = load_inventory()
    if dish_name not in RECIPE_MAP:
        print(f"No recipe found for {dish_name}.")
        return

    required = RECIPE_MAP[dish_name]
    for material, qty in required.items():
        for item in inventory:
            if item["name"].lower() == material.lower():
                if item["quantity"] >= qty:
                    item["quantity"] -= qty
                else:
                    print(f"Not enough {material} in stock!")
    save_inventory(inventory)
    print(f"Inventory updated for {dish_name}.")