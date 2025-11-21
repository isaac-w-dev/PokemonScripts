from reuseable_gpc_variables import dr, dl, du, dd, plus, min, ab, yb, bb, xb, zr, zl, rb, lb, tab, get_val, set_val, wait, combo_stop, combo_run, set_led, prnt, event_press

file = open("auto_teleport_loop.gpc", "w")

wait_time = [100]

program_name = r"Menu Fast Travel\nAll Locations"

instruction_page = r"Set Destination\nCategory: UP/DOWN\nLocation: Left/Right"

# Good for combos, if/elses, for, while

def function_firstline(function_name, function_type = 'combo', num_tabs = 0, num_spaces = 1, file = file):
    print("Is called", function_name, function_type, num_spaces, num_tabs)
    file.write(f"{tab*num_tabs}{function_type}{' '*num_spaces}{function_name}" + r' {' + '\n')

def end_block(tab_num = 0):
    file.write(f'{tab * tab_num}' + '}\n\n')

def write_command(command_name, input_array, tab_num = 1, file = file):
    tab = '\t'
    file.write(f'{tab * tab_num + command_name}(')
    for input in input_array[:-1]:
        file.write(f'{input}, ')
    file.write(f'{input_array[-1]});\n')

def cluster_commands(command_array, array_of_array_input):
    for i, command in enumerate(command_array):
        write_command(command, array_of_array_input[i])

def button_sequence(button_array):
    for button in button_array:
        button_input(button)

def button_input(button):
    cluster_commands([set_val, wait, set_val, wait], [[button, 100], wait_time, [button, 0], wait_time])

def coordinates_to_dpad(coordinates):

    x_coordinate_button = dr
    y_coordinate_button = dd
    dpad_array = []

    if coordinates[0] < 0: x_coordinate_button = dl

    if coordinates[1] < 0: y_coordinate_button = du
    
    if coordinates[0] != 0:
        for i in range(abs(coordinates[0])):
            dpad_array.append(x_coordinate_button)

    if coordinates[1] != 0:
        for i in range(abs(coordinates[1])):
            dpad_array.append(y_coordinate_button)
    
    dpad_array.append(ab)
    
    # print(dpad_array)
    # print('\n\n')
    return dpad_array

def map_to_menu():
    function_firstline("map_to_menu")
    button_sequence([plus, yb, min])
    end_block()

# def menu_selection(category):
#     category_index = get_position(category, filter_categories)
#     category = string_to_variable(category)
#     function_firstline(f'{category}_map_to_menu')
#     write_command(combo_run, ["map_to_menu"])
#     dpad_inputs = []
#     for i in range(category_index):
#         dpad_inputs.append(dd)
#     dpad_inputs.append(ab)
#     button_sequence(dpad_inputs)
#     end_block()

# def create_reused_combos(filter_categories):
#     map_to_menu()
#     for category in filter_categories[:-1]:
#         menu_selection(category)

def string_to_variable(target_string):
    variable_name = ''
    for char in target_string.lower():
        if char in ' -':
            variable_name += '_'
        elif char in '().': continue
        else:
            variable_name += char
    return variable_name