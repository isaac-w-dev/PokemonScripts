# Needs to filter out non-starters before displaying
# Needs clarification on filtered, unfiltered, forward, or backward
# LED Display shows, direction, filtered, number of steps, and location
# Create script to write script with init for filtered
# Script for checking on all alphas in center
# Script for running back and forth
#     Block input from the left stick to avoid drift??
# AFK Money Farm
# Door Exploit Script
# Fossil Exploit
# Failsafe that restarts from absolute beginning
# Learn to automate testing
# Read in information from pikalytics
# Type matchup automation
# Script to measure distance of running
# Document and refactor code
# Save processing with adjusted logic flow

from locations import locations
from locations_by_type import locations_by_type
filter_categories = ["All Locations", "Facilities", "Pokemon Centers", "Cafes", "Wild Zones", "Cancel"]
directions = ["Plus", "Minus", "Y", "x-axis", "y-axis", "A"]

def get_position(location, locations):
    return locations.index(location)


# Gets the category array for filtered retrieval
def get_category(location, locations_by_type, categories = filter_categories):
    for i in range(len(locations_by_type)):
        if location in locations_by_type[i]: return [locations_by_type[i], categories[i]]


# Finds points available from hitting Right on the d-pad
def find_jump_points(array):
    jump_points = []
    clean_jumps = len(array) // 7
    for i in range(clean_jumps):
        jump_length = i * 7
        jump_points.append(jump_length)
    final_jump = len(array) - 7
    jump_points.append(final_jump)
    return jump_points, "Forward"


# Finds points available from hitting Left on the d-pad
def find_backward_jump_points(array):
    jump_points = []
    highest_index = len(array) - 1
    jump_length = -7
    last_backward_index = 7
    for index in range(highest_index, last_backward_index, jump_length):
        jump_points.append(index)
    # Check just in case 
    jump_points.append(6)
    return jump_points, "Backward"


# Finds the closest point to the target location and returns the coordinates in an array, and the steps required to reach it
# def find_closest_point(target_index, jump_points, direction, filter):
#     if direction == "Forward":
#         step = 0
#         step_modifier = 1
#     else:
#         step = -1
#         step_modifier = -1

#     steps = []
#     coordinates = []
    # print(f"***ALL JUMP POINTS FOR {direction.upper()} DIRECTION {filter.upper()}***")
    # for point in jump_points:
    #     y_value = target_index - point
    #     steps.append(abs(step) + abs(y_value))
    #     coordinates.append([step, y_value])
        # print(f'Steps: {steps[-1]}\nCoordinates: {coordinates[-1]}\nDirection: {direction}\n')
        # step += 1 * step_modifier

    # target_index = steps.index(min(steps))
    # print(f'***SHORTEST JUMP POINT FOR {direction.upper()} DIRECTION***\nOF: {steps[target_index]} steps\nAT: {coordinates[target_index]}\n{filter.upper()}\n')
    # return coordinates[target_index], steps[target_index], direction


# def forward_or_backward(f_coordinate, b_coordinate):
#     if f_coordinate[1] > b_coordinate[1]:
#         return [b_coordinate[0], b_coordinate[1],  "Backward"]
#     else: return [f_coordinate[0], f_coordinate[1], "Forward"]


# Compares the steps returned by the forward jump points, and backward, and finds the shortest route to the desired index
# def get_steps(location_name, location_array):
#     filter = "All Locations"
#     backward_allowed = False

    # Probably a better way to check whether this is the filtered array
    # if len(location_array) == 6:
    #     location_array, filter = get_category(location_name, location_array)
    #     # Checks if array is in the 'zone' category
    #     if filter != "Wild Zones": backward_allowed = False
    # index = get_position(location_name, location_array)
    # f_jp, direction = find_jump_points(location_array)
    # NEEDS FILTERING TO PREVENT BACKWARD JUMP POINTS FROM RUNNING
    # b_jp, r_direction = find_backward_jump_points(location_array)
    # shortest_coordinate = find_closest_point(index, f_jp, direction, filter)
    # if backward_allowed:
    #     b_coordinate = find_closest_point(index, b_jp, r_direction, filter)
    #     shortest_coordinate = forward_or_backward(shortest_coordinate, b_coordinate, filter, location_name)
    # return shortest_coordinate
    # Returns Coordinates in an array, Steps, Direction, Filter, Location Name
# Compares the shortest filtered path to the shortest unfiltered path, and returns the shortest route


# def shortest_path(location):
#     unfiltered = get_steps(location, locations)
#     filtered = get_steps(location, locations_by_type)
#     if filtered[1] < unfiltered[1]:
#         print(f'***ABSOLUTE SHORTEST PATH FOR: {location.upper()}***\nFiltered\nSteps: {filtered[1]}\nCoordinates: {filtered[0]}\nDirection: {filtered[2]}\n')
#         return filtered
#     else:
#         print(f'***ABSOLUTE SHORTEST PATH FOR: {location.upper()}***\nUnfiltered\nSteps: {unfiltered[1]}\nCoordinates: {unfiltered[0]}\nDirection: {unfiltered[2]}\n')
#         return unfiltered
# Finds the shortest path for every location


def all_shortest_paths():
    for i in range(len(locations)):
        info_set = shortest_path(locations[i])
all_shortest_paths()