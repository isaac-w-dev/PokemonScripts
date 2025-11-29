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
    num_per_category = [18, 9, 17, 20]
    all_location_names = ['Centrico Plaza', 'Gare de Lumiose', 'Pokemon Research Lab', 'Hotel Z', 'Racine Construction', 'Restaurant Le Nah', 'Rust Syndicate Office', 'Lumiose Sewers (Canal Access)', 'Quasartico Inc.', 'Lysandre Cafe', 'Lumiose Sewers (Main Access)', 'Hotel Richissime', 'Looker Bureau', 'Lumiose Museum', 'Restaurant Le Yeah', 'Sushi High Roller', 'Restaurant Le Wow', 'Justice Dojo', 'Vert Pokemon Center', 'Bleu Pokemon Center', 'Vernal Pokemon Center', 'Magenta Pokemon Center', 'Magenta Plaza Pokemon Center', 'Rouge Pokemon Center', 'Centrico Pokemon Center', 'Jaune Pokemon Center', 'Hibernal Pokemon Center', 'Cafe Cyclone', 'Cafe Classe', 'Cafe Introversion', 'Nouveau Cafe', 'Cafe Woof', 'Cafe Soleil', 'Shutterbug Cafe', 'Nouveau Cafe Truck No. 2', 'Cafe Pokemon-Amie', 'Cafe Rouleau', 'Cafe Gallant', 'Cafe Triste', 'Nouveau Cafe Truck No. 3', 'Cafe Ultimo', 'Cafe Action', 'Cafe Kizuna', 'Cafe Bataille', 'Wild Zone 1', 'Wild Zone 2', 'Wild Zone 3', 'Wild Zone 4', 'Wild Zone 5', 'Wild Zone 6', 'Wild Zone 7', 'Wild Zone 8', 'Wild Zone 9', 'Wild Zone 10', 'Wild Zone 11', 'Wild Zone 12', 'Wild Zone 13', 'Wild Zone 14', 'Wild Zone 15', 'Wild Zone 16', 'Wild Zone 17', 'Wild Zone 18', 'Wild Zone 19', 'Wild Zone 20']
    fastest_category_per_location = ['All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'Facilities', 'Facilities', 'Facilities', 'All travel spots', 'All travel spots', 'All travel spots', 'Facilities', 'Facilities', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones'],
    full_coordinate_array= [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 1, -2], [0, 1, -1], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 1, 0], [1, 2, 0], [1, 2, 1], [0, 2, -1], [0, 2, 0], [0, 2, 1], [1, -1, -1], [1, -1, 0], [2, 0, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, -2, -1], [2, -2, 0], [2, -1, -1], [2, -1, 0], [3, 0, 0], [3, 0, 1], [3, 0, 2], [3, 0, 3], [3, 0, 4], [3, 1, -2], [3, 1, -1], [3, 1, 0], [3, 1, 1], [3, -2, 0], [3, 2, 0], [3, 2, 1], [3, 2, 2], [3, -1, -3], [3, -1, -2], [3, -1, -1], [3, -1, 0], [4, 0, 0], [4, 0, 1], [4, 0, 2], [4, 0, 3], [4, 0, 4], [4, 1, -2], [4, 1, -1], [4, 1, 0], [4, 1, 1], [4, 1, 2], [4, 1, 3], [4, 2, -2], [4, 2, -1], [4, 2, 0], [4, 2, 1], [4, 2, 2], [4, 2, 3], [4, 2, 4], [4, 2, 5], [4, 2, 6]]
    locations_in_file = [
    ["Facilities",
    "Centrico Plaza", "Gare de Lumiose", "Pokemon Research Lab", "Hotel Z", "Racine Construction", "Restaurant Le Nah", "Rust Syndicate Office",
    "Lumiose Sewers (Canal Access)", "Quasartico Inc.", "Lysandre Cafe", "Lumiose Sewers (Main Access)", "Hotel Richissime", "Looker Bureau", "Lumiose Museum",
    "Restaurant Le Yeah", "Sushi High Roller", "Restaurant Le Wow", "Justice Dojo"],
    ["Pokemon Centers",
    "Vert Pokemon Center", "Bleu Pokemon Center", "Vernal Pokemon Center", "Magenta Pokemon Center", "Magenta Plaza Pokemon Center", "Rouge Pokemon Center", "Centrico Pokemon Center",
    "Jaune Pokemon Center", "Hibernal Pokemon Center"],
    ["Cafes",
    "Cafe Cyclone", "Cafe Classe", "Cafe Introversion", "Nouveau Cafe", "Cafe Woof", "Cafe Soleil", "Shutterbug Cafe",
    "Nouveau Cafe Truck No. 2", "Cafe Pokemon-Amie", "Cafe Rouleau", "Cafe Gallant", "Cafe Triste", "Nouveau Cafe Truck No. 3", "Cafe Ultimo",
    "Cafe Action", "Cafe Kizuna", "Cafe Bataille"],
    ["Wild Zones",
    "Wild Zone 1", "Wild Zone 2", "Wild Zone 3", "Wild Zone 4", "Wild Zone 5", "Wild Zone 6", "Wild Zone 7",
    "Wild Zone 8", "Wild Zone 9", "Wild Zone 10", "Wild Zone 11", "Wild Zone 12", "Wild Zone 13", "Wild Zone 14",
    "Wild Zone 15", "Wild Zone 16", "Wild Zone 17", "Wild Zone 18", "Wild Zone 19", "Wild Zone 20"]
    ]

    def __init__(self, wait_time, file_name, program_name, instruction_page):
        self.wait_time = wait_time
        self.file_name = file_name
        self.file = open(file_name, 'w')
        self.program_name = program_name
        self.instruction_page = instruction_page

# ************** VARIABLE FUNCTIONS ***************************
    def initialize_variable(self, var_name, var_type, assignment, spaces = ' '):
        return f'{var_type}{spaces}{var_name}{assignment};\n'
    
    def initialize_int(self, var_name, assignment):
        return self.initialize_variable(var_name, 'int', f' = {assignment}')
    
    def initialize_string(self, var_name, assignment):
        var_name = self.string_to_variable(var_name)
        return self.initialize_variable(var_name, 'const string', f' = "{assignment}"')

    def array_to_string(self, array, wrapper ='{}'):
        new_string = wrapper[0]
        for item in array[:-1]:
            if isinstance(item, list):
                new_string += f'{self.array_to_string(item, wrapper)}, '
            else: new_string += f'{item}, '
        if isinstance(array[-1], list):
            new_string += f'{self.array_to_string(array[-1], wrapper)}'
        else:
            new_string += f'{array[-1]}'
        new_string += wrapper[1]
        return new_string
    
    def declare_strings_from_array(self, string_array):
        new_string = ''
        for item in string_array:
            new_string += self.initialize_string(item, item)
        return new_string

    def get_depth(self, array):
        depth = 1
        for item in array:
            if isinstance(item, list):
                depth += self.get_depth(item)
                break
        return depth

    def initialize_array(self, name, array, var_type ='const int', brackets = '{}'):
        returned_string = f'{var_type} {name}{'[]' * self.get_depth(array)} = '
        returned_string += self.array_to_string(array, brackets)
        return f'{returned_string};\n'

    def define_value(self, var_name, value):
        return self.initialize_variable(var_name, 'define', f' = {value}')
    
    def declare_var(self, var_name, var_type):
        return self.initialize_variable(var_name, var_type, '')
    
    def declare_int(self, var_name):
        return self.declare_var(var_name, 'int')
    
    def reassign_variable(self, var_name, value):
        return self.initialize_variable(var_name, '', f' = {value}', '')
    
    def var_plus_equal(self, var_name, added_value):
        return self.initialize_variable(var_name, '', f' += {added_value}', '')

# ************** CODE BLOCK WRITING SECTION *******************
    def start_code_block(self, type, block_name, space = ' '):
        return f"{type}{space}{block_name}" + '{\n'
    
    def start_function(self, function_name, arg_array):
        arg_string = self.array_to_csv(arg_array)
        return self.start_code_block('function', f'{function_name}({arg_string})')
    
    def start_combo(self, combo_name):
        return self.start_code_block('combo', f'{combo_name}()')
        
    def start_if_block(self, condition):
        return self.start_code_block('if', f'({condition})')
    
    def start_elif(self, condition):
        return self.start_code_block('else if', f'({condition})')
    
    def start_else(self):
        return self.start_code_block('', 'else', space = '')

    def end_block(self):
        return '}\n\n'
    
    def create_full_block(self, firstline, *args):
        new_string = firstline
        for line in args:
            new_string += line
        new_string += self.end_block()
        return new_string
    
# ************** COMMAND WRITING SECTION **********************
    def write_command(self, command_name, input_array):
        new_string = f'{command_name}('
        if len(input_array) > 0:
            for input in input_array[:-1]:
                new_string += f'{input}, '
            new_string += f'{input_array[-1]}'
        new_string += ');\n'
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
    
    def array_to_csv(self, array):
        new_string = ''
        if len(array) < 1: return new_string
        for item in array[:-1]:
            new_string += f'{item}, '
        new_string += array[-1]
        return new_string

    def insert_tabs(self):
        pass
