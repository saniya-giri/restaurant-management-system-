import json
import os
import random
import uuid
import datetime


TABLE_FILE = "database/tables.json"
BOOKING_FILE = "database/booking.json"


def load_tables():

    if not os.path.exists(TABLE_FILE):
        return []

    with open(TABLE_FILE, "r") as f:
        return json.load(f)


def generate_table_id(tables):

    while True:

        table_id = str(random.randint(10000, 99999))

        if all(
            table.get("table_id") != table_id
            for table in tables
        ):
            return table_id


def save_tables(data):

    folder = os.path.dirname(TABLE_FILE)

    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(TABLE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_bookings():

    if not os.path.exists(BOOKING_FILE):
        return []

    with open(BOOKING_FILE, "r") as f:
        return json.load(f)


def save_bookings(data):

    folder = os.path.dirname(BOOKING_FILE)

    if not os.path.exists(folder):
        os.makedirs(folder)

    with open(BOOKING_FILE, "w") as f:
        json.dump(data, f, indent=4)


def initialize_tables():

    tables = []

    # 20 VIP
    for i in range(1, 21):

        table_id = generate_table_id(tables)

        tables.append({
            "table_id": table_id,
            "size": "VIP",
            "capacity": 20,
            "booked": 0
        })

    for i in range(21, 41):

        table_id = generate_table_id(tables)

        tables.append({
            "table_id": table_id,
            "size": "Medium",
            "capacity": 20,
            "booked": 0
        })

    for i in range(41, 61):

        table_id = generate_table_id(tables)

        tables.append({
            "table_id": table_id,
            "size": "Short",
            "capacity": 20,
            "booked": 0
        })


    save_tables(tables)

    print("Tables initialized successfully!")

def view_tables():

    tables = load_tables()

    print("\n")
    print("=" * 80)
    print(" " * 27 + "TABLE MANAGEMENT")
    print("=" * 80)

    print("==================================================================" )

    print("| No.   | Table ID| Table Type   | Capacity | Booked | Available |" )

    print( "==================================================================")
    if not tables:
        print("|                     No tables available                         |")
    else:

        for index, table in enumerate(tables, start=1):

            table_id = table["table_id"]
            table_type = table["size"]
            capacity = table["capacity"]
            booked = table["booked"]

            available = capacity - booked

            print(
                f"| {index:<5} "
                f"| {table_id:<7} "
                f"| {table_type:<12} "
                f"| {capacity:<8} "
                f"| {booked:<6} "
                f"| {available:<9} |"
            )
    print("==================================================================")

def add_table(table_type, capacity):

    tables = load_tables()

    table_id = generate_table_id(tables)

    table = {
        "table_id": table_id,
        "size": table_type,
        "capacity": capacity,
        "booked": 0
    }

    tables.append(table)

    save_tables(tables)

    print("\n==========================================")
    print("Table added successfully")
    print("Table ID:", table_id)
    print("==========================================")


def update_table():

    tables = load_tables()

    view_tables()

    table_id = input("Enter Table ID to update: ")

    for t in tables:

        if t["table_id"] == table_id:

            t["size"] = input("Enter New Size: ")

            t["capacity"] = int(
                input("Enter New Capacity: ")
            )

            save_tables(tables)

            print("Table updated successfully!")

            return

    print("Table not found!")


def delete_table():

    tables = load_tables()

    view_tables()

    table_id = input("Enter Table ID to delete: ")

    for t in tables:

        if t["table_id"] == table_id:

            tables.remove(t)

            save_tables(tables)

            print("Table deleted successfully!")

            return

    print("Table not found!")


def book_table(staff_name):

    tables = load_tables()

    bookings = load_bookings()

    customer = input("Enter Customer Name: ")

    phone = input("Enter Phone Number: ")

    number_of_people = int(
        input("Enter Number of People: ")
    )

    table_size = input(
        "Enter Table Size (VIP/Medium/Short): "
    )


    for t in tables:

        if t["size"].lower() == table_size.lower():

            if t["booked"] + number_of_people <= t["capacity"]:

                t["booked"] += number_of_people

                booking_id = str(uuid.uuid4())

                booking = {
                    "booking_id": booking_id,
                    "customer": customer,
                    "phone": phone,
                    "size": table_size,
                    "people": number_of_people,
                    "staff": staff_name,
                    "time": str(datetime.datetime.now())
                }

                bookings.append(booking)

                save_tables(tables)

                save_bookings(bookings)

                print("Table booked successfully!")

                return

            else:

                print(
                    "Not enough seats available in",
                    table_size
                )

                return

    print("Table size not found!")