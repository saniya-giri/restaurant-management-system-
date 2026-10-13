import json
import os

ORDERS_FILE = "database/orders.json"
BILL_FILE = "database/bills.json"
INV_FILE = "database/inventory.json"

def load_json(file):
    if not os.path.exists(file):
        return []
    try:
        with open(file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def reports():
    orders = load_json(ORDERS_FILE)
    bills = load_json(BILL_FILE)
    inventory = load_json(INV_FILE)

    print("\n==================== REPORTS ====================")

    total_orders = len(orders)
    print(f"Total Orders: {total_orders}")

    total_bills = len(bills)
    print(f"Total Bills: {total_bills}")

    total_revenue = sum(b['total_bill'] for b in bills)
    print(f" Total Revenue: ₹{total_revenue}")

    dish_count = {}
    for o in orders:
        dish_count[o['dish']] = dish_count.get(o['dish'], 0) + int(o['quantity'])
    if dish_count:
        top_dish = max(dish_count, key=dish_count.get)
        print(f" Top Selling Dish: {top_dish} ({dish_count[top_dish]} orders)")

    print("\nInventory Status:")
    print("{:<6} {:<20} {:<10} {:<10}".format("ID", "Item", "Quantity", "Unit"))
    print("---------------------------------------------------")
    for i in inventory:
        print("{:<6} {:<20} {:<10} {:<10}".format(i['id'], i['item'], i['quantity'], i['unit']))
    print("===================================================\n")
