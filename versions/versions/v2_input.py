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