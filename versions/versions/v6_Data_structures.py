rooms = [
    {"number": 101, "type": "Standard Room", "rate": 5500.00, "available": True},
    {"number": 102, "type": "Deluxe Room", "rate": 7500.00, "available": True},
    {"number": 103, "type": "Executive Suite", "rate": 12000.00, "available": True},
]
bookings = []


def display_menu():
    print("\n1. Book Room")
    print("2. View Rooms")
    print("3. View Bookings")
    print("4. Search Booking")
    print("5. Check Out")
    print("6. Exit")


def show_rooms(only_available=False):
    for room in rooms:
        if only_available and not room["available"]:
            continue
        status = "Available" if room["available"] else "Booked"
        print(f"Room {room['number']} | {room['type']} | "
              f"Ksh {room['rate']:.2f}/night | {status}")


def find_room(number):
    for room in rooms:
        if room["number"] == number:
            return room
    return None


def book_room():
    show_rooms(only_available=True)
    guest = input("Enter guest full name: ")
    number = int(input("Enter room number: "))
    room = find_room(number)

    if room is None:
        print("Room not found.")
        return
    if not room["available"]:
        print("That room is already booked.")
        return

    nights = int(input("Enter number of nights: "))
    if nights <= 0:
        print("Error: stay must be at least 1 night.")
        return

    subtotal, discount, tax, total = calculate_bill(room["rate"], nights)
    room["available"] = False
    bookings.append({"guest": guest, "room": number, "nights": nights,
                     "total": total, "status": "active"})
    print_receipt(guest, room["type"], nights, subtotal, discount, tax, total)


def view_bookings():
    if not bookings:
        print("No bookings yet.")
        return
    for b in bookings:
        print(f"Room {b['room']} | {b['guest']} | {b['nights']} night(s) | "
              f"Ksh {b['total']:.2f} | {b['status']}")


def search_booking():
    term = input("Enter guest name: ").lower()
    found = False
    for b in bookings:
        if term in b["guest"].lower():
            print(f"Room {b['room']} | {b['guest']} | {b['status']}")
            found = True
    if not found:
        print("No matching booking.")


def check_out():
    number = int(input("Enter room number: "))
    for b in bookings:
        if b["room"] == number and b["status"] == "active":
            b["status"] = "completed"
            find_room(number)["available"] = True
            print(f"{b['guest']} checked out. Room {number} is now available.")
            return
    print("No active booking for that room.")


def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            book_room()
        elif choice == "2":
            show_rooms()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            search_booking()
        elif choice == "5":
            check_out()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()