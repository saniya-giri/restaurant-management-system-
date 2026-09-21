import json,menu_managment
from datetime import datetime
class Order:
    def place_order(self):

        customer_name = input("\nEnter customer name: ")

        order_items = []
        total_amount = 0

        while True:

            choice = int(input("\nEnter product number (0 = finish): "))

            if choice == 0:
                break

            if choice not in self.menu:
                print("Invalid product number!")
                continue

            quantity = int(input("Enter quantity: "))

            product = self.menu[choice]

            amount = product["price"] * quantity

            order_items.append({
                "product": product["name"],
                "price": product["price"],
                "quantity": quantity,

                
                "amount": amount
            })

            total_amount += amount

            print(

                product["name"],
                "added successfully!"
            )

        if len(order_items) == 0:
            print("No product selected.")
            return

        order_id = len(self.orders) + 1

        order = {
            "order_id": order_id,
            "customer_name": customer_name,
            "items": order_items,
            "total_amount": total_amount,
            "date": str(datetime.now())
        }

        self.orders.append(order)

        with open("orders.json", "w") as file:
            json.dump(self.orders, file, indent=4)

        print("\n========== ORDER SUCCESS ==========")
        print("Order ID:", order_id)
        print("Customer:", customer_name)
        print("Total Amount: ₹", total_amount)
        print("Order placed successfully!")

    def show_orders(self):

        if len(self.orders) == 0:
            print("\nNo orders available.")
            return

        print("\n========== ALL ORDERS ==========")

        for order in self.orders:

            print("\nOrder ID:", order["order_id"])
            print("Customer:", order["customer_name"])

            for item in order["items"]:
                print(
                    item["product"],
                    "x",
                    item["quantity"],
                    "=",
                    "₹",
                    item["amount"]
                )

            print("Total: ₹", order["total_amount"])
            print("Date:", order["date"])

    def search_order(self):

        order_id = int(input("\nEnter Order ID: "))

        for order in self.orders:

            if order["order_id"] == order_id:

                print("\n========== ORDER DETAILS ==========")
                print("Order ID:", order["order_id"])
                print("Customer:", order["customer_name"])

                for item in order["items"]:
                    print(
                        item["product"],
                        "x",
                        item["quantity"],
                        "=",
                        "₹",
                        item["amount"]
                    )

                print("Total: ₹", order["total_amount"])
                return

        print("Order not found!")

    def cancel_order(self):

        order_id = int(input("\nEnter Order ID to cancel: "))

        for order in self.orders:

            if order["order_id"] == order_id:

                self.orders.remove(order)

                with open("orders.json", "w") as file:
                    json.dump(self.orders, file, indent=4)

                print("Order cancelled successfully!")
                return

        print("Order not found!")

order_system = Order()

while True:

    print("\n\n========== RESTAURANT ORDER MANAGEMENT ==========")

    print("1. Place Order")
    print("2. Show All Orders")
    print("3. Search Order")
    print("4. Cancel Order")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        order_system.place_order()

    elif choice == 2:
        order_system.show_orders()

    elif choice == 3:
        order_system.search_order()

    elif choice == 4:
        order_system.cancel_order()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")