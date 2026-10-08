import json
import os
ORDERS_FILE = "database/orders.json"
MENU_FILE = "database/menu.json"
def load_orders():
    if not os.path.exists(ORDERS_FILE):
        return []

    with open(ORDERS_FILE, "r") as f:
        return json.load(f)

def save_orders(data):
    with open(ORDERS_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_menu():
    if not os.path.exists(MENU_FILE):
        return []

    with open(MENU_FILE, "r") as f:
        return json.load(f)

def payment(order, total):
    if order.get("payment_status") == "Paid":

        print("\n==============================================")
        print("       Payment already completed")
        print("==============================================")
        print("Order ID:", order["id"])
        print("Payment ID:", order.get("payment_id", "N/A"))
        print("Payment Method:", order.get("payment_method", "N/A"))
        print("==============================================")
        return False
    while True:
        print("\n")
        print("==============================================")
        print("                 PAYMENT")
        print("==============================================")
        print("Amount to Pay: ₹{:.2f}".format(total))
        print("----------------------------------------------")
        print("1. Cash")
        print("2. Card")
        print("3. UPI")
        print("4. Cancel")
        print("\n==============================================")
        choice = input("Enter payment choice: ")
        print("==============================================")
        if choice == "1":
            payment_method = "Cash"
            break

        elif choice == "2":
            payment_method = "Card"
            break

        elif choice == "3":
            payment_method = "UPI"
            break

        elif choice == "4":
            print("\nPayment cancelled.")
            return False
        else:
            print("----------- Invalid payment choice ------------")


    order["payment_status"] = "Paid"

    order["payment_method"] = payment_method

    order["payment_amount"] = total

    import uuid
    order["payment_id"] = str(uuid.uuid4())

    order["status"] = "Completed"
    orders = load_orders()

    for item in orders:
        if str(item["id"]) == str(order["id"]):
            item.update(order)
            break
    save_orders(orders)
    
    print("\n==============================================")
    print("          PAYMENT SUCCESSFUL")
    print("==============================================")
    print("Order ID      :", order["id"])
    print("Payment ID    :", order["payment_id"])
    print("Payment Method:", order["payment_method"])
    print("Amount Paid   : ₹{:.2f}".format(total))
    print("Payment Status: Paid")
    print("==============================================")
    return True

def generate_bill(order_id, gst_rate=0.10, discount=0):
    orders = load_orders()
    menu = load_menu()

    order = None
    for o in orders:
        if str(o["id"]) == str(order_id):
            order = o
            break
    if order is None:
        print("\n======================================")
        print("          Order not found")
        print("======================================")
        return

    if order.get("payment_status") == "Paid":
        print("\n==============================================")
        print("       Payment already completed")
        print("==============================================")
        print("Order ID:", order["id"])
        print("Payment ID:", order.get("payment_id", "N/A"))
        print("Payment Method:", order.get("payment_method", "N/A"))
        print("==============================================")
        return

    dish_price = None
    for item in menu:
        if item["name"].lower() == order["dish"].lower():
            dish_price = float(item["price"])
            break

    if dish_price is None:
        print("\n======================================")
        print("         Dish not found in menu")
        print("======================================")
        return
    
    quantity = int(order["quantity"])
    subtotal = dish_price * quantity
    gst = subtotal * gst_rate
    total = subtotal + gst - discount

    print("\n==================================================")
    print("                    BILL")
    print("==================================================")
    print("Order ID       :", order["id"])
    print("Dish           :", order["dish"])
    print("Quantity       :", quantity)
    print("Price per Item : ₹{:.2f}".format(dish_price))
    print("--------------------------------------------------")
    print("Subtotal       : ₹{:.2f}".format(subtotal))
    print(
        "GST ({}%)      : ₹{:.2f}".format(
            int(gst_rate * 100),
            gst
        )
    )
    print("Discount       : ₹{:.2f}".format(discount))
    print("--------------------------------------------------")
    print("TOTAL AMOUNT   : ₹{:.2f}".format(total))
    print("==================================================")
    print("-------- Bill generated successfully -------")
    payment(order, total)

def sales_report(gst_rate=0.10):
    orders = load_orders()
    menu = load_menu()

    if not orders:
        print("\n======================================")
        print("          No sales yet")
        print("======================================")
        return

    total_sales = 0
    print("\n==================================================")
    print("                  SALES REPORT")
    print("==================================================")
    for order in orders:
        if order.get("payment_status") != "Paid":
            continue
        for item in menu:
            if item["name"].lower() == order["dish"].lower():
                price = float(item["price"])
                quantity = int(order["quantity"])
                subtotal = price * quantity
                gst = subtotal * gst_rate
                total = subtotal + gst
                total_sales += total
                break
    print("Total Sales (with GST): ₹{:.2f}".format(total_sales))
    print("==================================================")