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
        print("Saved data loaded.")
    except FileNotFoundError:
        print("No saved data found. Starting fresh.")