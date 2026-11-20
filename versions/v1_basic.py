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