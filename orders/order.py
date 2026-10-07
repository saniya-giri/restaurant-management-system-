import json
import os
from inventory import inventory  
ORDERS_FILE = "database/orders.json"

def load_orders():
    if not os.path.exists(ORDERS_FILE):
        return []
    with open(ORDERS_FILE, "r") as f:
        return json.load(f)

def save_orders(data):
    with open(ORDERS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def take_order(staff_name):
    orders = load_orders()
    order_id = max([o["id"] for o in orders], default=100) + 1

    dish_name = input("Enter dish name: ")
    quantity = int(input("Enter quantity: "))

    new_order = {
        "id": order_id,
        "dish": dish_name,
        "quantity": quantity,
        "staff": staff_name,
        "status": "Pending"
    }
    orders.append(new_order)
    save_orders(orders)

    for _ in range(quantity):
        inventory.reduce_inventory(dish_name)

    print(f" Order {order_id} placed for {dish_name} x{quantity} by {staff_name}")

def view_orders():
    orders = load_orders()
    if not orders:
        print("\n------ No orders found ------")
    else:
        print("\n================ ORDERS ================")
        for o in orders:
            print(f"ID: {o['id']} | Dish: {o['dish']} | Qty: {o['quantity']} | Staff: {o['staff']} | Status: {o['status']}")
