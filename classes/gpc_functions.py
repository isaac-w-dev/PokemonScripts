class gpc():
    # Reusable variables
    tab = '\t'
    dr = "SWI_RIGHT"
    dl = "SWI_LEFT"
    du = "SWI_UP"
    dd = "SWI_DOWN"
    plus = "SWI_PLUS"
    min = "SWI_MINUS"
    ab = "SWI_A"
    yb = "SWI_Y"
    bb = "SWI_B"
    xb = "SWI_X"
    zr = "SWI_ZR"
    zl = "SWI_ZL"
    rb = "SWI_R"
    lb = "SWI_L"
    get_val = "get_val"
    set_val = "set_val"
    wait = "wait"
    combo_stop = "combo_stop"
    combo_run = "combo_run"
    set_led = "set_led"
    prnt = "print"
    event_press = "event_press"

    def __init__(self, wait_time, file_name, program_name, instruction_page):
        self.wait_time = wait_time
        self.file_name = file_name
        self.program_name = program_name
        self.instruction_page = instruction_page

# ************** VARIABLE FUNCTIONS ***************************
    def initialize_variable(self, var_name, var_type, assignment):
        return f'{var_type} {var_name}{assignment};\n'
    
    def initialize_int(self, var_name, assignment):
        return self.initialize_variable(var_name, 'int', f' = {assignment}')
    
    def initialize_string(self, var_name, assignment):
        return self.initialize_variable(var_name, 'const string', f' = "{assignment}"')

    def initialize_array(self, depth = 1, *args):
        pass

    def create_define(self, var_name, value):
        return self.initialize_variable(var_name, 'define', f' = {value}')
    
    def declare_var(self, var_name, var_type):
        return self.initialize_variable(var_name, var_type, '')
    
    def declare_int(self, var_name):
        return self.declare_var(var_name, 'int')

# ************** CODE BLOCK WRITING SECTION *******************
    def start_code_block(self, type, block_name, space = ' '):
        return f"{gpc.tab * self.num_tabs}{type}{space}{block_name}" + '{\n'
    
    def start_function(self, function_name, arg_array):
        arg_string = self.array_to_string(arg_array)
        return self.start_code_block('function', f'{function_name}({arg_string})')
    
    def start_combo(self, combo_name):
        return self.start_code_block('combo', f'{combo_name}()')
        
    def start_if_block(self, condition):
        return self.start_code_block('if', f'({condition})')
    
    def start_elif(self, condition):
        return self.start_code_block('else if', f'({condition})')
    
    def start_else(self):
        return self.start_code_block('', 'else', space = '')

    def end_block(num_tabs):
        return f'{gpc.tab * num_tabs}' + '}\n\n'
    
# ************** COMMAND WRITING SECTION **********************
    def write_command(self, command_name, input_array):
        new_string = f'{self.tab * self.num_tabs}{command_name}('
        for input in input_array[:-1]:
            new_string += f'{input}, '
        new_string += f'{input_array[-1]});\n'
        return new_string

    def cluster_commands(self, command_array, array_of_array_input):
        new_string = ''
        for i, command in enumerate(command_array):
            new_string += self.write_command(command, array_of_array_input[i])
        return new_string
    
    def button_input(self, button):
        return self.cluster_commands([gpc.set_val, gpc.wait, gpc.set_val, gpc.wait], [[button, 100], gpc.wait_time, [button, 0], gpc.wait_time])

    def button_sequence(self, button_array):
        new_string = ''
        for button in button_array:
            new_string += self.button_input(button)
        return new_string

    def coordinates_to_dpad(coordinates):
        x_coordinate_button = gpc.dr
        y_coordinate_button = gpc.dd
        dpad_array = []

        if coordinates[0] < 0: x_coordinate_button = gpc.dl

        if coordinates[1] < 0: y_coordinate_button = gpc.du

        if coordinates[0] != 0:
            for i in range(abs(coordinates[0])):
                dpad_array.append(x_coordinate_button)

        if coordinates[1] != 0:
            for i in range(abs(coordinates[1])):
                dpad_array.append(y_coordinate_button)

        dpad_array.append(gpc.ab)

        return dpad_array

# ************** GENERAL STRING CONVERSION FUNCTIONS ***************
    def string_to_variable(self, target_string):
        variable_name = ''
        for char in target_string.lower():

            if char in ' -': variable_name += '_'

            elif char in '().': continue

            else: variable_name += char

        return variable_name
    
    def array_to_string(self, array):
        new_string = ''
        for item in array[:-1]:
            new_string += f'{item}, '
        new_string += array[-1]
        return new_string

    def insert_tabs(self):
        pass
