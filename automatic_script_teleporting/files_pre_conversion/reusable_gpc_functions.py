from files_pre_conversion.reuseable_gpc_variables import dr, dl, du, dd, plus, min, ab, yb, bb, xb, zr, zl, rb, lb, tab, get_val, set_val, wait, combo_stop, combo_run, set_led, prnt, event_press

file = open("auto_teleport_loop.gpc", "w")

wait_time = [100]

program_name = r"Menu Fast Travel\nAll Locations"

instruction_page = r"Set Destination\nCategory: UP/DOWN\nLocation: Left/Right"

# Good for combos, if/elses, for, while

def function_firstline(function_name, function_type = 'combo', num_tabs = 0, num_spaces = 1, file = file):
    file.write(f"{tab*num_tabs}{function_type}{' '*num_spaces}{function_name}" + r' {' + '\n')
def generate_if(condition, num_tabs, file, if_type = 'if'):
    function_firstline(f'({condition})', if_type, num_tabs, file=file)

def generate_else(num_tabs, file):
    function_firstline('', function_type = 'else', num_tabs=num_tabs, file=file)
    

def end_block(num_tabs = 0, file = file):
    tab = '\t'
    file.write(f'{tab * num_tabs}' + '}\n\n')

def write_command(command_name, input_array, num_tabs = 1, file = file):
    tab = '\t'
    file.write(f'{tab * num_tabs}{command_name}(')
    for input in input_array[:-1]:
        file.write(f'{input}, ')
    file.write(f'{input_array[-1]});\n')

def cluster_commands(command_array, array_of_array_input):
    for i, command in enumerate(command_array):
        write_command(command, array_of_array_input[i])

def button_input(button):
    cluster_commands([set_val, wait, set_val, wait], [[button, 100], wait_time, [button, 0], wait_time])

def button_sequence(button_array):
    for button in button_array:
        button_input(button)

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
    
    return dpad_array

def map_to_menu():
    function_firstline("map_to_menu")
    button_sequence([plus, yb, min])
    end_block()

def string_to_variable(target_string):
    variable_name = ''
    for char in target_string.lower():
        if char in ' -':
            variable_name += '_'
        elif char in '().': continue
        else:
            variable_name += char
    return variable_name