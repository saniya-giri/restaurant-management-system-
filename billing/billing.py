import json
import os
import uuid
import datetime

ORDERS_FILE = "database/orders.json"
MENU_FILE = "database/menu.json"
BILLS_FILE = "database/bills.json"
PAYMENTS_FILE = "database/payments.json"

def load_data(file_name):
    if not os.path.exists(file_name):
        return []

    try:
        with open(file_name, "r") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data

            return []

    except (json.JSONDecodeError, OSError):
        print(f"Unable to read {file_name}!")
        return []


# Save JSON data
def save_data(file_name, data):
    os.makedirs("database", exist_ok=True)

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


# Generate bill
def generate_bill(order_id, gst_rate=0.10, discount=0):
    orders = load_data(ORDERS_FILE)
    bills = load_data(BILLS_FILE)
    payments = load_data(PAYMENTS_FILE)

    # Find order
    order = None

    for item in orders:
        if str(item.get("order_id")) == str(order_id):
            order = item
            break

    if order is None:
        print("Order ID not found!")
        return

    # Check whether bill already exists
    for bill in bills:
        if str(bill.get("order_id")) == str(order_id):
            print("Bill already generated!")
            print_bill(bill)

            payment_done = any(
                str(payment.get("bill_id")) == str(bill.get("bill_id"))
                for payment in payments
            )

            if not payment_done:
                payment_option(bill)

            return

    try:
        subtotal = float(order.get("total_amount", 0))
        discount = float(discount)
    except (ValueError, TypeError):
        print("Invalid order amount or discount!")
        return

    if subtotal <= 0:
        print("Order amount is invalid!")
        return

    if discount < 0 or discount > subtotal:
        print("Invalid discount! Discount cannot exceed the order amount.")
        return

    gst_amount = (subtotal - discount) * gst_rate
    total = subtotal - discount + gst_amount

    bill = {
        "bill_id": str(uuid.uuid4()),
        "order_id": order_id,
        "date": str(datetime.date.today()),
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "gst": round(gst_amount, 2),
        "total": round(total, 2)
    }

    bills.append(bill)
    save_data(BILLS_FILE, bills)

    print_bill(bill)

    payment_option(bill)

def print_bill(bill):
    print("\n" + "=" * 45)
    print("             RESTAURANT BILL")
    print("=" * 45)

    print(f"Bill ID  : {bill['bill_id']}")
    print(f"Order ID : {bill['order_id']}")
    print(f"Date     : {bill['date']}")

    print("-" * 45)
    print(f"{'Subtotal':<25} Rs. {bill['subtotal']:.2f}")
    print(f"{'Discount':<25} Rs. {bill['discount']:.2f}")
    print(f"{'GST (10%)':<25} Rs. {bill['gst']:.2f}")

    print("-" * 45)
    print(f"{'TOTAL AMOUNT':<25} Rs. {bill['total']:.2f}")
    print("=" * 45)


def payment_option(bill):
    payments = load_data(PAYMENTS_FILE)

    for payment in payments:
        if str(payment.get("bill_id")) == str(bill["bill_id"]):
            print("Payment already completed for this bill!")
            print(f"Payment Method: {payment['method']}")
            print(f"Payment Status: {payment['status']}")
            return

    print("\n========== PAYMENT ==========")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")
    print("4. Cancel Payment")

    choice = input("Select payment method: ").strip()

    methods = {
        "1": "Cash",
        "2": "UPI",
        "3": "Card"
    }

    if choice == "4":
        print("Payment cancelled. You can pay later.")
        return

    if choice not in methods:
        print("Invalid payment option!")
        return

    payment = {
        "payment_id": str(uuid.uuid4()),
        "bill_id": bill["bill_id"],
        "order_id": bill["order_id"],
        "amount": bill["total"],
        "method": methods[choice],
        "status": "Paid",
        "date": str(datetime.date.today())
    }

    payments.append(payment)
    save_data(PAYMENTS_FILE, payments)

    print("\nPayment successful!")
    print(f"Amount: Rs. {payment['amount']:.2f}")
    print(f"Method: {payment['method']}")
    print(f"Status: {payment['status']}")



def view_bills():
    bills = load_data(BILLS_FILE)
    payments = load_data(PAYMENTS_FILE)

    if not bills:
        print("No bills found!")
        return

    print("\n" + "=" * 75)
    print("                         ALL BILLS")
    print("=" * 75)

    print(
        f"{'Order ID':<15}{'Subtotal':<12}"
        f"{'GST':<10}{'Total':<12}{'Payment Status'}"
    )

    print("-" * 75)

    for bill in bills:
        paid = any(
            str(payment.get("bill_id")) == str(bill.get("bill_id"))
            for payment in payments
        )

        status = "Paid" if paid else "Pending"

        print(
            f"{str(bill['order_id']):<15}"
            f"{bill['subtotal']:<12.2f}"
            f"{bill['gst']:<10.2f}"
            f"{bill['total']:<12.2f}"
            f"{status}"
        )

    print("=" * 75)

def billing():
    while True:
        print("\n========== BILL MANAGEMENT ==========")
        print("1. Generate Bill")
        print("2. View All Bills")
        print("3. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            orders = load_data(ORDERS_FILE)

            if not orders:
                print("No orders found! Please place an order first.")
                continue

        
            order_id = input("Enter Order ID: ").strip()

            order_exists = any(
                str(order.get("order_id")) == order_id
                for order in orders
            )

            if not order_exists:
                print("Order ID not found! Please enter a valid Order ID.")
                continue

        
            discount_input = input(
                "Enter discount amount (0 if none): "
            ).strip()

            try:
                discount = float(discount_input)

                if discount < 0:
                    print("Discount cannot be negative!")
                    continue

                generate_bill(order_id, discount=discount)

            except ValueError:
                print("Please enter a valid discount amount!")

        elif choice == "2":
            view_bills()

        elif choice == "3":
            break

        else:
            print("Invalid choice!")

