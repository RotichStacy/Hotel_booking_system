HOTEL_NAME = "Starshine Hotel"
TAX_RATE = 0.16
room_names = ["Standard Room", "Deluxe Room", "Executive Suite"]
room_rates = [5500.00, 7500.00, 12000.00]

total_revenue = 0
bookings_made = 0

print(f"=== WELCOME TO {HOTEL_NAME.upper()} ===")

while True:
    print("\n1. Book Room")
    print("2. View Rooms")
    print("3. Exit")
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        guest_name = input("Enter guest full name: ")

        for i in range(3):
            print(f"{i + 1}. {room_names[i]} (Ksh {room_rates[i]:.2f}/night)")

        room_choice = input("Enter room choice (1, 2 or 3): ")
        if room_choice in ("1", "2", "3"):
            index = int(room_choice) - 1
            nights = int(input("Enter number of nights: "))

            if nights <= 0:
                print("Error: stay must be at least 1 night.")
            else:
                subtotal = room_rates[index] * nights
                if nights >= 7:
                    discount_rate = 0.15
                elif nights >= 4:
                    discount_rate = 0.05
                else:
                    discount_rate = 0.0

                discount_amount = subtotal * discount_rate
                taxable = subtotal - discount_amount
                tax = taxable * TAX_RATE
                total_bill = taxable + tax

                print(f"\nGuest: {guest_name}")
                print(f"Room: {room_names[index]}")
                print(f"Total bill: Ksh {total_bill:.2f}")

                total_revenue += total_bill
                bookings_made += 1
        else:
            print("Invalid room choice.")

    elif choice == "2":
        for i in range(3):
            print(f"{room_names[i]}: Ksh {room_rates[i]:.2f}/night")

    elif choice == "3":
        print(f"Bookings made: {bookings_made}, revenue: Ksh {total_revenue:.2f}")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")