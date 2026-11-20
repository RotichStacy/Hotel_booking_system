#hotel metadata
hotel_name = "Starshine Hotel"
standard_room_price = 5500.00 #ksh per night
deluxe_room_price = 7500.00 #ksh per night
tax_rate = 0.16 #16% tax rate

#Hard-coded room Reservation
guest_name = "Hamfrey Kimeli"
room_type = "Deluxe Room"
nights_stayed = 3

#Calculation
subtotal = deluxe_room_price * nights_stayed
tax_amount = subtotal * tax_rate
total_amount = subtotal + tax_amount

# Output
print("=== " + hotel_name + " ===")
print("Guest Name:", guest_name)
print("Room Type:", room_type)
print("Nights:", nights_stayed)
print("Subtotal: ksh", subtotal)
print("Tax: ksh", tax_amount)
print("Total Bill: ksh", total_amount)

# Interactive User Input and Formatted Output

hotel_name = "Starshine Hotel"
standard_rate = 5500.00
deluxe_rate = 7500.00
suite_rate = 12000.00
tax_rate = 0.16

print(f"====================================")
print(f"   WELCOME TO {hotel_name.upper()}   ")
print(f"====================================\n")

# Capture Guest Information
guest_name = input("Enter Guest Full Name: ")
phone_number = input("Enter Contact Phone Number: ")

print("\nAvailable Room Types:")
print(f"1. Standard (Ksh {standard_rate:.2f}/night)")
print(f"2. Deluxe   (Ksh {deluxe_rate:.2f}/night)")
print(f"3. Suite    (Ksh {suite_rate:.2f}/night)")

# For Stage 2, user inputs exact rate based on choice above
nightly_rate = float(input("\nEnter the nightly rate for chosen room (Ksh): "))
nights_stayed = int(input("Enter number of nights: "))

# Calculations
subtotal = nightly_rate * nights_stayed
tax = subtotal * tax_rate
total = subtotal + tax

# Formatted Invoice Output
print("\n" + "="*35)
print("          BOOKING RECEIPT          ")
print("="*35)
print(f"Guest Name:    {guest_name}")
print(f"Contact:       {phone_number}")
print(f"Nights Reserved: {nights_stayed}")
print("-" * 35)
print(f"Subtotal:      Ksh{subtotal:8.2f}")
print(f"Tax (16%):     Ksh{tax:8.2f}")
print(f"Total Amount:  Ksh{total:8.2f}")
print("="*35)

# Decision-Making with Conditional Statements

hotel_name = "Starshine Hotel"

# Room Rates per Night
RATE_STANDARD = 5500.00
RATE_DELUXE = 7500.00
RATE_SUITE = 12000.00
TAX_RATE = 0.16  # 16% tax rate

print("====================================")
print(f"   WELCOME TO {hotel_name.upper()}   ")
print("====================================\n")

guest_name = input("Enter Guest Full Name: ")

print("\n--- Select Room Category ---")
print("1. Standard Room (Ksh 5500.00/night)")
print("2. Deluxe Room   (Ksh 7500.00/night)")
print("3. Executive Suite (Ksh 12000.00/night)")

room_choice = input("Enter room choice (1, 2, or 3): ")

# Determine rate using conditional statements
if room_choice == "1":
    selected_room = "Standard Room"
    nightly_rate = RATE_STANDARD
elif room_choice == "2":
    selected_room = "Deluxe Room"
    nightly_rate = RATE_DELUXE
elif room_choice == "3":
    selected_room = "Executive Suite"
    nightly_rate = RATE_SUITE
else:
    selected_room = "Unknown"
    nightly_rate = 0.00

# Proceed only if room choice was valid
if nightly_rate > 0:
    nights_stayed = int(input("Enter number of nights to stay: "))

    if nights_stayed <= 0:
        print("\nError: Stay duration must be at least 1 night.")
    else:
        subtotal = nightly_rate * nights_stayed

        # Apply Discount for longer stays (Logical/Conditional check)
        discount_rate = 0.0
        if nights_stayed >= 7:
            discount_rate = 0.15  # 15% discount for 7+ nights
            print("\n>> Long-stay discount applied (15%)!")
        elif nights_stayed >= 4:
            discount_rate = 0.05  # 5% discount for 4-6 nights
            print("\n>> Extended-stay discount applied (5%)!")

        discount_amount = subtotal * discount_rate
        taxable_amount = subtotal - discount_amount
        tax = taxable_amount * TAX_RATE
        total_bill = taxable_amount + tax

        # Display Final Summary
        print("\n" + "="*40)
        print("          BOOKING CONFIRMATION          ")
        print("="*40)
        print(f"Guest Name:     {guest_name}")
        print(f"Room Selected:  {selected_room}")
        print(f"Rate per Night: Ksh{nightly_rate:8.2f}")
        print(f"Duration:       {nights_stayed} night(s)")
        print("-" * 40)
        print(f"Base Cost:      Ksh{subtotal:8.2f}")
        if discount_amount > 0:
            print(f"Discount:      -Ksh{discount_amount:8.2f}")
        print(f"Tax (16%):      Ksh{tax:8.2f}")
        print(f"Final Total:    Ksh{total_bill:8.2f}")
        print("="*40)
else:
    print("\nInvalid choice selected. Please restart and select 1, 2, or 3.")