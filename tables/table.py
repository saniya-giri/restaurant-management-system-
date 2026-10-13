import json
import os
import random
import datetime

TABLE_FILE = "database/tables.json"

TABLE_RATES = {
    "VIP": 1000,
    "Medium": 500,
    "Short": 250
}

TABLE_CAPACITY = {
    "VIP": 8,
    "Medium": 4,
    "Short": 2
}


def load_tables():
    if not os.path.exists(TABLE_FILE):
        return []

    with open(TABLE_FILE, "r") as file:
        return json.load(file)

def save_tables(tables):
    os.makedirs("database", exist_ok=True)

    with open(TABLE_FILE, "w") as file:
        json.dump(tables, file, indent=4)

def generate_table_id(tables):
    while True:
        table_id = str(random.randint(10000, 99999))

        if not any(table["id"] == table_id for table in tables):
            return table_id

def create_default_tables():
    tables = load_tables()


    if tables:
        return

    for category in ["VIP", "Medium", "Short"]:
        for i in range(10):
            tables.append({
                "id": generate_table_id(tables),
                "capacity": TABLE_CAPACITY[category],
                "charge": TABLE_RATES[category],
                "category": category,
                "status": "Available",
                "booking_time": None
            })

    save_tables(tables)


# Automatically free tables after 2 hours
def auto_update_status(tables):
    current_time = datetime.datetime.now()

    for table in tables:
        if table["status"] == "Booked" and table["booking_time"]:
            booking_time = datetime.datetime.fromisoformat(
                table["booking_time"]
            )

            if current_time - booking_time >= datetime.timedelta(hours=2):
                table["status"] = "Available"
                table["booking_time"] = None

    save_tables(tables)

def print_table(tables, category_name):
    category_tables = [
        table for table in tables
        if table["category"] == category_name
    ]

    print(f"\n{'=' * 65}")
    print(f"{category_name.upper()} TABLES")
    print("=" * 65)

    print(f"{'Table ID':<15}{'Capacity':<15}{'Rate (Rs.)':<15}{'Status'}")
    print("-" * 65)

    for table in category_tables:
        print(
            f"{table['id']:<15}"
            f"{str(table['capacity']) + ' People':<15}"
            f"{table['charge']:<15}"
            f"{table['status']}"
        )

    available = sum(
        1 for table in category_tables
        if table["status"] == "Available"
    )

    booked = sum(
        1 for table in category_tables
        if table["status"] == "Booked"
    )

    print("-" * 65)
    print(f"Total Tables : {len(category_tables)}")
    print(f"Available    : {available}")
    print(f"Booked       : {booked}")


def view_tables():
    tables = load_tables()
    auto_update_status(tables)

    for category in ["VIP", "Medium", "Short"]:
        print_table(tables, category)

    print("\n" + "=" * 65)
    print(f"TOTAL TABLES: {len(tables)}")
    print("=" * 65)

def add_table():
    tables = load_tables()

    print("\n========== ADD TABLE ==========")
    print("1. VIP     - Rs. 1000")
    print("2. Medium  - Rs. 500")
    print("3. Short   - Rs. 250")

    choice = input("Select category: ").strip()

    categories = {
        "1": "VIP",
        "2": "Medium",
        "3": "Short"
    }

    if choice not in categories:
        print("Invalid category!")
        return

    category = categories[choice]

    table = {
        "id": generate_table_id(tables),
        "capacity": TABLE_CAPACITY[category],
        "charge": TABLE_RATES[category],
        "category": category,
        "status": "Available",
        "booking_time": None
    }

    tables.append(table)
    save_tables(tables)

    print("\nTable added successfully!")
    print(f"Table ID : {table['id']}")
    print(f"Category : {category}")
    print(f"Capacity : {table['capacity']} People")
    print(f"Rate     : Rs. {table['charge']}")

def update_table():
    tables = load_tables()
    auto_update_status(tables)

    table_id = input("Enter 5-digit Table ID: ").strip()

    for table in tables:
        if table["id"] == table_id:
            if table["status"] == "Booked":
                print("Booked table cannot be updated!")
                return

            print("\n1. VIP")
            print("2. Medium")
            print("3. Short")

            choice = input("Select new category: ").strip()

            categories = {
                "1": "VIP",
                "2": "Medium",
                "3": "Short"
            }

            if choice not in categories:
                print("Invalid category!")
                return

            category = categories[choice]

            table["category"] = category
            table["capacity"] = TABLE_CAPACITY[category]
            table["charge"] = TABLE_RATES[category]

            save_tables(tables)
            print("Table updated successfully!")
            return

    print("Table ID not found!")

def book_table():
    tables = load_tables()
    auto_update_status(tables)

    table_id = input("Enter 5-digit Table ID: ").strip()

    for table in tables:
        if table["id"] == table_id:
            if table["status"] == "Booked":
                print("This table is already booked!")
                return

            print("\n========== TABLE DETAILS ==========")
            print(f"Table ID : {table['id']}")
            print(f"Category : {table['category']}")
            print(f"Capacity : {table['capacity']} People")
            print(f"Rate     : Rs. {table['charge']}")

            confirm = input("Confirm booking? (yes/no): ").strip().lower()

            if confirm == "yes":
                table["status"] = "Booked"
                table["booking_time"] = datetime.datetime.now().isoformat()

                save_tables(tables)
                print("Table booked successfully!")
            else:
                print("Booking cancelled.")

            return

    print("Table ID not found!")


def delete_table():
    tables = load_tables()

    table_id = input("Enter 5-digit Table ID: ").strip()

    for table in tables:
        if table["id"] == table_id:
            if table["status"] == "Booked":
                print("Booked table cannot be deleted!")
                return

            tables.remove(table)
            save_tables(tables)
            print("Table deleted successfully!")
            return

    print("Table ID not found!")


def table_management():
    create_default_tables()

    while True:
        print("\n========================================")
        print("          TABLE MANAGEMENT")
        print("========================================")
        print("1. View Tables")
        print("2. Add Table")
        print("3. Update Table")
        print("4. Book Table")
        print("5. Delete Table")
        print("6. Back")
        print("========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tables()

        elif choice == "2":
            add_table()

        elif choice == "3":
            update_table()

        elif choice == "4":
            book_table()

        elif choice == "5":
            delete_table()

        elif choice == "6":
            break

        else:
            print("Invalid choice! Please try again.")

