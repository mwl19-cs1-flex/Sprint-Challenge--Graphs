from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Import Stack
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Import Queue
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited_path = set()
st = Stack()
qt = Queue()

st.push(player.current_room)
qt.enqueue(player.current_room)
print(world.starting_room)

# while visited_path != room_graph:
#     cell = qt.dequeue()
#     print(cell)
#     if cell not in visited_path:
#         visited_path.add(cell)
#     for i in cell.get_exits():
#         next_cell = cell.get_room_in_direction(i)
#         if next_cell not in visited_path:
#             traversal_path.append(i)
#             qt.enqueue(next_cell)

while st.size() > 0:
    cell = st.pop()
    if cell not in visited_path:
        visited_path.add(cell)
    for i in cell.get_exits():
        next_cell = cell.get_room_in_direction(i)
        if next_cell not in visited_path:
            traversal_path.append(i)
            st.push(next_cell)

# print(room_graph)
# print('current amount of rooms in map', len(room_graph))
# print(f'Current rooms visited: {len(visited_path)}')
# print(player.current_room.get_exits())
# for i in player.current_room.get_exits():
#     print(f'current room id:{player.current_room.id}')
#     print(f'next rooms: {player.current_room.get_room_in_direction(i)}')

# Understand
# Current room is an instance of a Room class which has
# # ID
# # Room in direction 
# # Possible exits of that room

# Plan
# Have a stack
# Append the first room to the stack
# While the stack is not zero
# # Take off the item of the stack
# # Add the room id to the visited path set
# # For each exit in the rooms
# # Get the room in the direction
# # If that room's id is NOT in visited
# # # Add the room to the stack
# # # Add the direction (i) to the traversal path

# Legacy Code
# while room_graph != visited_path:
#     for i in player.current_room.get_exits():
#         player.travel(i)
#         visited_path.add(player.current_room)
#         traversal_path.append(i)
#         if player.travel(i) == "You cannot move in that direction.":
#             pass

# NOTES FROM BEEJ
# Walk in a stack (go backwards!)
# DFT then BFT (look at the hints)
# Get NEIGHBORS!!!
# DFT and backtracking is enough for MVP
# While loop of DFT
# Then loop of BFT
# Understanding and Planning is HUGE part of this!!!
# This is the Travelling Salesman problem
# Learning framework Beej uses to be better teacher: UPER! 

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

for i in visited_rooms:
    print(i.id)

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#         visited_rooms.add(player.current_room)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

