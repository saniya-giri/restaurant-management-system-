import json
import uuid
import datetime

booking = []

VIP_CAPACITY = 20
MEDIUM_CAPACITY = 20
SHORT_CAPACITY = 20


class Table:

    def __init__(self, table_size, table_time, table_duration, number_of_people):
        self.table_size = table_size
        self.table_time = table_time
        self.table_duration = table_duration
        self.number_of_people = number_of_people

    def book_table(self):

        customer_name = input("Enter Customer Name: ")
        phone = input("Enter Phone Nucmber: ")

        data = {
            "booking_id": str(uuid.uuid4()),
            "customer_name": customer_name,
            "phone": phone,
            "number_of_people": self.number_of_people,
            "table_size": self.table_size,
            "table_time": self.table_time,
            "table_duration": self.table_duration,
            "booking_date": str(datetime.date.today())
        }

        booking.append(data)

        with open("booking.json", "w") as file:
            json.dump(booking, file, indent=4)

        print("\nTable Booked Successfully!")


class Restaurant:

    def table_booking(self):

        print("\n-------- Table Booking --------")

        number_of_people = int(input("Enter Number of People: "))

        vip_booked = sum(
            b["number_of_people"]
            for b in booking
            if b["table_size"] == "VIP"
        )

        medium_booked = sum(
            b["number_of_people"]
            for b in booking
            if b["table_size"] == "Medium"
        )

        short_booked = sum(
            b["number_of_people"]
            for b in booking
            if b["table_size"] == "Short"
        )

        total_booked = vip_booked + medium_booked + short_booked

        if total_booked + number_of_people > 60:

            print("\nSorry! Only", 60 - total_booked,
                  "seats are available.")

            return

        vip_available = VIP_CAPACITY - vip_booked
        medium_available = MEDIUM_CAPACITY - medium_booked
        short_available = SHORT_CAPACITY - short_booked

        remaining_people = number_of_people

        vip_people = 0
        medium_people = 0
        short_people = 0

        if remaining_people > 0:

            vip_people = min(remaining_people, vip_available)
            remaining_people = remaining_people - vip_people

        if remaining_people > 0:

            medium_people = min(remaining_people, medium_available)
            remaining_people = remaining_people - medium_people


        if remaining_people > 0:

            short_people = min(remaining_people, short_available)
            remaining_people = remaining_people - short_people

        table_time = input("Enter Booking Time: ")
        table_duration = input("Enter Duration: ")

        customer_name = input("Enter Customer Name: ")
        phone = input("Enter Phone Number: ")

        booking_id = str(uuid.uuid4())
        booking_date = str(datetime.date.today())

  
        data = {
            "booking_id": booking_id,
            "customer_name": customer_name,
            "phone": phone,
            "number_of_people": number_of_people,
            "VIP": vip_people,
            "Medium": medium_people,
            "Short": short_people,
            "table_time": table_time,
            "table_duration": table_duration,
            "booking_date": booking_date
        }

        booking.append(data)

        with open("booking.json", "w") as file:
            json.dump(booking, file, indent=4)

        print("\n-------- Booking Successful --------")

        if vip_people > 0:
            print("VIP    :", vip_people)

        if medium_people > 0:
            print("Medium :", medium_people)

        if short_people > 0:
            print("Short  :", short_people)

        print("Total  :", number_of_people)

        print("------------------------------------")


    def show_all_bookings(self):

        print("\n-------- All Bookings --------")

        if not booking:

            print("No bookings yet.")

        else:

            for b in booking:

                print("\n-----------------------------")
                print("Booking ID:", b["booking_id"])
                print("Customer:", b["customer_name"])
                print("Phone:", b["phone"])
                print("Total People:", b["number_of_people"])

                print("VIP:", b["VIP"])
                print("Medium:", b["Medium"])
                print("Short:", b["Short"])

                print("Time:", b["table_time"])
                print("Duration:", b["table_duration"])
                print("Date:", b["booking_date"])

                print("-----------------------------")


    def show_capacity(self):

        vip_booked = sum(b["VIP"] for b in booking)
        medium_booked = sum(b["Medium"] for b in booking)
        short_booked = sum(b["Short"] for b in booking)

        total_booked = vip_booked + medium_booked + short_booked 

        print("\n-------- Restaurant Capacity --------")

        print("VIP    :", vip_booked, "/", VIP_CAPACITY)
        print("Medium :", medium_booked, "/", MEDIUM_CAPACITY)  
        print("Short  :", short_booked, "/", SHORT_CAPACITY)

        print("-------------------------------------")
        print("Total Booked:", total_booked)
        print("Total Capacity:", 60)
        print("Remaining:", 60 - total_booked)
        print("-------------------------------------")


    def show_menu(self):

        while True:

            print("\n-------- Booking Menu --------")
            print("1. Table Booking")
            print("2. Show All Bookings")
            print("3. Show Capacity")
            print("4. Exit")
            print("------------------------------")

            choice = input("Enter your choice: ")

            if choice == "1":

                self.table_booking()

            elif choice == "2":

                self.show_all_bookings()

            elif choice == "3":

                self.show_capacity()

            elif choice == "4":

                print("Thank you.")
                break

            else:

                print("Invalid Choice.")


restaurant = Restaurant()
restaurant.show_menu()
