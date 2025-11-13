from shortest_path import get_position, find_jump_points, find_backward_jump_points, locations, locations_by_type, get_category

# Finds the closest point to the target location and returns the coordinates in an array, and the steps required to reach it
def find_closest_point(target_index, jump_points, direction, filter):

    if direction == "Forward":
        step = 0
        step_modifier = 1

    else:
        step = -1
        step_modifier = -1

    steps = []
    coordinates = []
    # print(f"***ALL JUMP POINTS FOR {direction.upper()} DIRECTION {filter.upper()}***")

    for point in jump_points:
        y_value = target_index - point
        steps.append(abs(step) + abs(y_value))
        coordinates.append([step, y_value])
        # print(f'Steps: {steps[-1]}\nCoordinates: {coordinates[-1]}\nDirection: {direction}\n')
        step += 1 * step_modifier

    target_index = steps.index(min(steps))
    # print(f'***SHORTEST JUMP POINT FOR {direction.upper()} DIRECTION***\nOF: {steps[target_index]} steps\nAT: {coordinates[target_index]}\n{filter.upper()}\n')
    return coordinates[target_index], steps[target_index], direction

# Probably can be optimized
def forward_or_backward(f_coordinate, b_coordinate):
    # print("Forward Coordinate:", f_coordinate)
    # print("Reverse Coordinate:", b_coordinate)
    if f_coordinate[1] > b_coordinate[1]:
        return b_coordinate[0], b_coordinate[1],  "Backward"
    
    else: return f_coordinate[0], f_coordinate[1], "Forward"


# Compares the steps returned by the forward jump points, and backward, and finds the shortest route to the desired index
# Probably can be optimized
def get_steps(location_name, location_array):
    filter = "All Locations"
    backward_allowed = True

    # Probably a better way to check whether this is the filtered array
    if len(location_array) == 6:
        location_array, filter = get_category(location_name, location_array)
    
    if filter == "Wild Zones" or filter == "All Locations": backward_allowed = False

    index = get_position(location_name, location_array)
    f_jp, direction = find_jump_points(location_array)
    # NEEDS FILTERING TO PREVENT BACKWARD JUMP POINTS FROM RUNNING
    b_jp, r_direction = find_backward_jump_points(location_array)
    shortest_coordinates, steps, direction = find_closest_point(index, f_jp, direction, filter)

    if backward_allowed:
        b_coordinates, bsteps, direction = find_closest_point(index, b_jp, r_direction, filter)
        shortest_coordinates, steps, direction = forward_or_backward([shortest_coordinates, steps], [b_coordinates, bsteps])

    return shortest_coordinates, steps, location_name, filter
    # Returns Coordinates in an array, Steps, Direction, Filter, Location Name
# Compares the shortest filtered path to the shortest unfiltered path, and returns the shortest route


def shortest_path(location):
    unfiltered_coordinates, usteps, location_name, ufilter = get_steps(location, locations)
    filtered_coordinates, fsteps, location_name, filter  = get_steps(location, locations_by_type)
    if fsteps < usteps:
        # print(f'***ABSOLUTE SHORTEST PATH FOR: {location.upper()}***\n{filter}\nSteps: {fsteps}\nCoordinates: {filtered_coordinates}\n')
        return filtered_coordinates, location_name, filter
    
    else:
        # print(f'***ABSOLUTE SHORTEST PATH FOR: {location.upper()}***\n{ufilter}\nSteps: {usteps}\nCoordinates: {unfiltered_coordinates}\n')
        return unfiltered_coordinates, location_name, ufilter

# Finds the shortest path for every location
def all_shortest_paths():

    for i in range(len(locations)):
        info_set = shortest_path(locations[i])


if '__name__' == '__main__': all_shortest_paths()