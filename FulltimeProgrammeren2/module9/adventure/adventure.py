# **************************************************************************************
# adventure.py
#
# Fulltime Programmeren 2
# Robin Laponder
#
# This file contains the Adventure class definition and the “game loop” of the program.
# **************************************************************************************


from room import Room
import sys


class Adventure():

    # Create rooms and items for the appropriate 'game' version.
    def __init__(self, game):

        # Rooms is a dictionary that maps a room number to the corresponding room object.
        self.rooms = {}

        # Parse the rooms from the data file.
        data = self.parse_rooms(f"data/{game}Rooms.txt")

        # Create room structures.
        self.load_rooms(data)

        # Game always starts in room number 1, so this should be the "current" room.
        self.current_room = self.rooms[1]

    # Parse room data line by line.
    def parse_rooms(self, filename):

        # Open an empty list, which will hold lists of room data.
        rooms_data = []

        # Load from datafile.
        with open(filename, "r") as f:
            # Open an empty list to hold the data of one room.
            room_data = []
            for line in f:
                # When there is no blank newline it means there's still data.
                if not line == "\n":
                    room_data.append(line.strip())
                # A blank newline signals all data of a single room is parsed.
                else:
                    rooms_data.append(room_data)
                    room_data = []

        # Append one final time, because the files do not end on a blank newline.
        rooms_data.append(room_data)
        return rooms_data

    # Load rooms from filename in two-step process.
    def load_rooms(self, data):

        # Phase 1: Create room objects for each set of data we just parsed.
        for room_data in data:
            # Create identifier.
            id = int(room_data[0])

            # Create a new room object with id, name and description.
            new_room = Room(id, room_data[1], room_data[2])
            self.rooms[id] = new_room

        # Phase 2: Connect rooms to each other.
        for room_data in data:
            # Create identifier.
            id = int(room_data[0])

            # Retrieve exisiting room object from dictionary.
            room = self.rooms[id]

            # Extract the connection data.
            connections = room_data[4:]

            # Add connections to the room.
            for connection in connections:
                direction, target_room_id = connection.split()
                if target_room_id != '0':
                    room.add_connection(direction, target_room_id)
                else:
                    room.add_connection(direction, target_room_id)
                    room.set_final()

    # Pass along the description of the current room.
    def get_description(self):

        # Return the name if the room has already been visited, else return the discription.
        if self.current_room.get_visited():
            return self.current_room.name
        else:
            return self.current_room.description

    # Move to a different room by changing "current" room, if possible.
    def move(self, direction):

        # Check whether the current room has a connection in the entered direction.
        if self.current_room.has_connection(direction) == False:
            print("Invalid command")
            return False
        else:
            # Set the current room to 'visited' and move to the connected room.
            self.current_room.set_visited()
            self.current_room = self.rooms[int(self.current_room.get_connection(direction))]

            if self.finished():
                print(adventure.current_room.description)
                sys.exit(0)

            # If current room does not have a 'forced' connection, print room information.
            if self.current_room.has_connection("FORCED") == False:
                print(adventure.get_description())

            return True

    # Check whether the current room is the final room.
    def finished(self):
        if self.current_room.is_final():
            return True
        return False

    # Check whether the current room has a forced direction.
    def has_forced(self):
        if self.current_room.has_connection("FORCED"):
            return True
        return False


if __name__ == "__main__":

    # Create a new game.
    adventure = Adventure("Small")

    # Greet the user.
    print("Welcome to Adventure.\n")

    # Print room description of the first room.
    print(adventure.get_description())

    # Prompt the user for commands until they've won the game.
    while True:

        # Prompt for a command and convert to upper.
        command = input("> ").upper()

        # Check whether the user entered a helper command.
        if "HELP" in command:
            print("You can move by typing directions such as EAST/WEST/IN/OUT\n"
                  "QUIT quits the game.\n"
                  "HELP prints instructions for the game.\n"
                  "LOOK lists the complete description of the room and its contents.")
        elif "QUIT" in command:
            print("Thanks for playing!")
            sys.exit(0)
        elif "LOOK" in command:
            print(adventure.current_room.description)

        # Perform move.
        else:
            adventure.move(command)
            if adventure.has_forced():
                print(adventure.current_room.description)
                adventure.move("FORCED")