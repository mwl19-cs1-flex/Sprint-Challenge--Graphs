from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# So I need a while loop that tracks a stack or a queue to the length of the room
# length of room minus 1 because we will already have the first room
# add the current room if it isn't in the visited stack with all of the exits
# remove the exits from the stack and add them to a path to make the player move in reverse
# once that stack is empty, add them to the traversal path
# Fill this out with directions to walk
# traversal_path = ['n', 'n']

# Setup
traversal_path = []
# Create a reverse path
reversal_path = []
# Track which rooms I've been in (id, plus exits of room)
visited = dict() # it's our hybrid slack/set, we have lengths but we use its items as a stack
reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# # start in room 0 and return exits

# visited gets treated like a stack, but also a set - we need to populate it first
visited[0] = player.current_room.get_exits() # sets the first item in the visited dict to the current exits

# we need visited to be the length of our room graph
while len(visited) < len(room_graph) - 1:
    # if current room hasn't been visited, add it
    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits() 
        last_room = reversal_path[-1] 
        visited[player.current_room.id].remove(last_room) 

    # this is what populates our traversal path, once its 0 we can utilize it
    while len(visited[player.current_room.id]) < 1:
        reverse = reversal_path.pop()
        traversal_path.append(reverse)
        player.travel(reverse)

    next_direction = visited[player.current_room.id].pop()
    traversal_path.append(next_direction)
    reversal_path.append(reverse_direction[next_direction])
    player.travel(next_direction)

# # Import Stack
# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)

# # Import Queue
# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

# # Import Graph
# class Graph:
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         self.vertices[vertex_id] = set() 

#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         elif v1 not in self.vertices:
#             self.add_vertex(v1)
#             self.vertices[v1].add(v2)
#         elif v2 not in self.vertices:
#             self.add_vertex(v2)
#             self.vertices[v1].add(v2)

#     def get_neighbors(self, vertex_id):
#         if vertex_id not in self.vertices:
#             raise IndexError("Vertex does not exist in graph!")
#         return self.vertices[vertex_id]

#     def bft(self, starting_vertex):
#         qq = Queue()
#         qq.enqueue(starting_vertex)
#         visited = set()
#         while qq.size() > 0:
#             vert = qq.dequeue()
#             if vert not in visited:
#                 visited.add(vert)
#                 for next_vert in self.get_neighbors(vert):
#                     qq.enqueue(next_vert)

#     def dft(self, starting_vertex):
#         st = Stack()
#         st.push(starting_vertex)
#         visited = set()
#         while st.size() > 0:
#             vert = st.pop()
#             if vert not in visited:
#                 print(vert)
#                 visited.add(vert)
#                 for next_vert in self.get_neighbors(vert):
#                     st.push(next_vert)

# # a traversal path
# # a reversal path (empty list)
# # visited was empty dictionary
# # inverse direction (n to s, e to w)
# # length of room graph and length of visited
# # current room get exits, pass that into visited dictionary of current room id
# visited_path = set()
# st = Stack()
# # st.push(player.current_room)
# qt = Queue()
# qt.enqueue(player.current_room)
# reversal_path = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# gg = Graph()
# for item in room_graph:
#     gg.add_vertex(item)
#     for room in room_graph[item][1]:
#         gg.add_edge(item, room_graph[item][1][room])

# gg.dft(player.current_room.id)


# for item in room_graph:
#     gg.add_edge(room_graph[item][1], room_graph)
# for item in room_graph[0][1]:
#     print(room_graph[0][1][item])
# while len(visited_path) < len(room_graph):
#     while qt.size() > 0:
#         cell = qt.dequeue()  
#         if cell not in visited_path:
#             visited_path.add(cell)
#             for item in cell.get_exits():
#                 next_room = cell.get_room_in_direction(item)
#                 if next_room is not None:
#                     player.travel(item)
#                     traversal_path.append(item)
#                     qt.enqueue(player.current_room)  
#                 else:
#                     pass
#     st.push(player.current_room)
#     while st.size() > 0:
#         area = st.pop()
#         if area not in visited_path:
#             visited_path.add(area)
#             for item in area.get_exits():
#                 next_room = area.get_room_in_direction(item)
#                 if next_room is not None:
#                     player.travel(item)
#                     traversal_path.append(item)
#                     st.push(player.current_room)
#                 else:
#                     pass

# for item in ['n', 's', 'e', 'w']:
#     traversal_path.append(reversal_path[item])
    
# while len(visited_path) < len(room_graph):
#     cell = qt.dequeue() # st.pop()
#     if cell not in visited_path:
#         visited_path.add(cell)
#         for item in cell.get_exits():
#             if cell.get_room_in_direction(item) not in visited_path:
#                 traversal_path.append(item)
#                 traversal_path.append(item)
#                 traversal_path.append(item)
#                 qt.enqueue(cell.get_room_in_direction(item))# st.push(cell.get_room_in_direction(item))
        


# for item in visited_path:
#     print(item.id)

# for item in traversal_path:    
#     traversal_path.append(reversal_path[item])


# while st.size() > 0:
#     cell = st.pop()
#     if cell not in visited_path:
#         visited_path.add(cell)
#     for i in cell.get_exits():
#         next_cell = cell.get_room_in_direction(i)
#         if next_cell not in visited_path and next_cell is not None:
#             traversal_path.append(i)
#             traversal_path.append(i)
#             st.push(next_cell)

# while st.size() > 0:
#     if player.current_room not in visited:
#         visited.add(player.current_room)
#     exits = player.current_room.get_exits()
#     for next_room in exits:
#         travel = player.current_room.get_room_in_direction(next_room)
#         if travel == True and travel not in visited:
#             player.travel(next_room)
#             traversal_path.append(next_room)
#             st.push(player.current_room)

# def map_recursive(starting_room, visited=None, traversal=None):
#     if visited is None:
#         visited = set()
#     if traversal is None:
#         traversal = list()
#     if starting_room in visited:
#         return
#     if starting_room not in visited:
#         visited.add(starting_room)
#         for (direction, next_room) in starting_room.get_connected_rooms():
#             traversal = traversal + [direction] + [direction]
#             map_recursive(next_room, visited, traversal)
    
#     return traversal 

# while st.size() > 0:
#     cell = st.pop()
#     if cell not in visited:
#         visited.add(cell)
#         for i in cell.get_connected_rooms():
#             player.travel(i[0])
#             traversal_path.append(i[0])
#             st.push(player.current_room)


        # if next_cell not in visited_path:
        #     traversal_path.append(i)
        #     traversal_path.append(i)
        #     traversal_path.append(i)
        #     st.push(next_cell)

    # for i in cell.get_exits():
    #     next_cell = cell.get_room_in_direction(i)
    #     if next_cell not in visited_path:
    #         traversal_path.append(i)
    #         st.push(next_cell)

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

# while qt.size() > 0:
#     cell = qt.dequeue()
#     if cell not in visited_path:
#         visited_path.add(cell)
#     while st.size() > 0:
#         cell = st.pop()
#         if cell not in visited_path:
#             visited_path.add(cell)
#         for i in cell.get_exits():
#             next_cell = cell.get_room_in_direction(i)
#             if next_cell not in visited_path:
#                 traversal_path.append(i)
#                 qt.enqueue(next_cell)
#                 st.push(next_cell)

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
    # print(f"MOVE: {move}")
    # print(f"ID:{player.current_room.id}")

print(f"MOVES: {len(traversal_path)}")

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

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

