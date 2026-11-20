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