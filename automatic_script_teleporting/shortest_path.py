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
    # print(jump_points)
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