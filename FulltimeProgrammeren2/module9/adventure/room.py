# **************************************************************************************
# room.py
#
# Fulltime Programmeren 2
# Robin Laponder
#
# This file contains the Room class definition.
# **************************************************************************************


class Room(object):

    # Initializes a Room.
    def __init__(self, id, name, description):

        # Dictionary that maps directions like "EAST" to other room objects.
        self.connections = {}

        # Room properties.
        self.id = id
        self.name = name
        self.description = description
        self.visited = False
        self.final = False

    # Adds rooms to connections dictionary, with the direction as key and room id as value.
    def add_connection(self, direction, room):
        self.connections[direction] = room

    # Checks whether the given direction has a connection from this room.
    def has_connection(self, direction):
        if direction in self.connections:
            return True
        return False

    # Retrieves room connected to this room.
    def get_connection(self, direction):
        return self.connections[direction]

    # Sets the current room to 'visited'.
    def set_visited(self):
        self.visited = True

    # Checks whether the current room has already been visited.
    def get_visited(self):
        return self.visited

    # Sets a specific room to 'final'.
    def set_final(self):
        self.final = True

    # Checks whether the current room is the final room.
    def is_final(self):
        return self.final