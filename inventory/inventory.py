import json
import os

INV_FILE = "database/inventory.json"

def load_inventory():
    if not os.path.exists(INV_FILE):
        return []
    try:
        with open(INV_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_inventory(data):
    with open(INV_FILE, "w") as f:
        json.dump(data, f, indent=4)

def view_inventory():
    inventory = load_inventory()
    if not inventory:
        print("Inventory is empty")
        return

    print("\n==================== INVENTORY ====================")
    print("{:<6} {:<20} {:<10} {:<10}".format("ID", "Item", "Quantity", "Unit"))
    print("---------------------------------------------------")
    for i in inventory:
        print("{:<6} {:<20} {:<10} {:<10}".format(i['id'], i['item'], i['quantity'], i['unit']))
    print("===================================================\n")

def add_item():
    inventory = load_inventory()
    item_id = str(len(inventory) + 1).zfill(3) 
    item = input("Enter Raw Material Name: ")
    quantity = input("Enter Quantity: ")
    unit = input("Enter Unit (kg/litre/pcs): ")

    new_item = {"id": item_id, "item": item, "quantity": quantity, "unit": unit}
    inventory.append(new_item)
    save_inventory(inventory)
    print(f" Item '{item}' added successfully!")

def update_item():
    inventory = load_inventory()
    item_id = input("Enter Item ID to update: ")
    for i in inventory:
        if i["id"] == item_id:
            new_qty = input("Enter new Quantity: ")
            i["quantity"] = new_qty
            save_inventory(inventory)
            print(f" Item {item_id} updated successfully!")
            return
    print("Item not found!")

def delete_item():
    inventory = load_inventory()
    item_id = input("Enter Item ID to delete: ")
    updated_inventory = [i for i in inventory if i["id"] != item_id]
    if len(updated_inventory) == len(inventory):
        print(" Item not found!")
    else:
        save_inventory(updated_inventory)
        print(f"Item {item_id} deleted successfully!")

def inventory_management():
    while True:
        print("\n========== INVENTORY MANAGEMENT ==========")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Back to Admin Dashboard")
            break
        else:
            print("Invalid choice! Try again.")
