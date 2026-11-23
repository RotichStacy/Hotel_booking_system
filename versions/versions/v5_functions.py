HOTEL_NAME = "Starshine Hotel"
TAX_RATE = 0.16
ROOM_NAMES = ["Standard Room", "Deluxe Room", "Executive Suite"]
ROOM_RATES = [5500.00, 7500.00, 12000.00]


def display_menu():
    print("\n1. Book Room")
    print("2. View Rooms")
    print("3. Exit")


def show_rooms():
    for i in range(len(ROOM_NAMES)):
        print(f"{i + 1}. {ROOM_NAMES[i]} (Ksh {ROOM_RATES[i]:.2f}/night)")


def get_discount_rate(nights):
    if nights >= 7:
        return 0.15
    elif nights >= 4:
        return 0.05
    return 0.0


def calculate_bill(rate, nights):
    subtotal = rate * nights
    discount = subtotal * get_discount_rate(nights)
    taxable = subtotal - discount
    tax = taxable * TAX_RATE
    return subtotal, discount, tax, taxable + tax


def print_receipt(guest, room, nights, subtotal, discount, tax, total):
    print("\n" + "=" * 40)
    print("          BOOKING CONFIRMATION")
    print("=" * 40)
    print(f"Guest Name:  {guest}")
    print(f"Room:        {room}")
    print(f"Duration:    {nights} night(s)")
    print("-" * 40)
    print(f"Base Cost:   Ksh{subtotal:10.2f}")
    if discount > 0:
        print(f"Discount:   -Ksh{discount:10.2f}")
    print(f"Tax (16%):   Ksh{tax:10.2f}")
    print(f"Final Total: Ksh{total:10.2f}")
    print("=" * 40)


def book_room():
    guest = input("Enter guest full name: ")
    show_rooms()
    choice = input("Enter room choice (1, 2 or 3): ")
    if choice not in ("1", "2", "3"):
        print("Invalid room choice.")
        return
    index = int(choice) - 1
    nights = int(input("Enter number of nights: "))
    if nights <= 0:
        print("Error: stay must be at least 1 night.")
        return
    subtotal, discount, tax, total = calculate_bill(ROOM_RATES[index], nights)
    print_receipt(guest, ROOM_NAMES[index], nights, subtotal, discount, tax, total)


def main():
    print(f"=== WELCOME TO {HOTEL_NAME.upper()} ===")
    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            book_room()
        elif choice == "2":
            show_rooms()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()