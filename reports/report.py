import json, os

ORDERS_FILE = "database/orders.json"
TABLES_FILE = "database/tables.json"
MENU_FILE = "database/menu.json"

def load_json(file):
    if not os.path.exists(file):
        return []
    with open(file, "r") as f:
        return json.load(f)

def show_report():
    orders = load_json(ORDERS_FILE)
    tables = load_json(TABLES_FILE)
    menu = load_json(MENU_FILE)

    total_orders = len(orders)
    total_revenue = sum(order["total_amount"] for order in orders) if orders else 0
    total_tables = len(tables)
    booked_tables = sum(t["booked"] for t in tables) if tables else 0
    total_menu_items = len(menu)

    print("\n=== REPORT SUMMARY ===")
    print(f"Total Orders: {total_orders}")
    print(f"Total Revenue: ₹{total_revenue}")
    print(f"Total Tables: {total_tables} | Booked Seats: {booked_tables}")
    print(f"Total Menu Items: {total_menu_items}")
