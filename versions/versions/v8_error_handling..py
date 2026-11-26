import json

DATA_FILE = "hotel_data.json"


def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump({"rooms": rooms, "bookings": bookings}, f, indent=4)


def load_data():
    global rooms, bookings
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        rooms = data["rooms"]
        bookings = data["bookings"]

        def get_int(prompt, minimum=1, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if value < minimum or (maximum is not None and value > maximum):
                print("Value out of range. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty.")
        print("Saved data loaded.")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")