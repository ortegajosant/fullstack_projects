hotel = {}

# Ask the user for the hotel name and the number of stars
hotel["name"] = input("Enter the hotel name: ")

try:
    hotel["number_of_stars"] = int(input("Enter the number of stars: "))
except ValueError:
    print("Please enter an integer.")
    hotel["number_of_stars"] = 0

# Ask the user for the information of the rooms in the hotel
rooms = []
number_of_rooms = int(input("Enter the number of rooms: "))

for i in range(number_of_rooms):
    room = {}
    room_index = i + 1
    room["number"] = input(f"Enter the number for room {room_index}: ")
    room["floor"] = input(f"Enter the floor for room {room_index}: ")
    try:
        room["price_per_nigth"] = float(
            input(f"Enter the price per night for room {room_index}: ")
        )
    except ValueError:
        print("Please enter a valid number. Setting default price to 0.")
        room["price_per_nigth"] = 0.0
    rooms.append(room)

hotel["rooms"] = rooms

print(hotel)
