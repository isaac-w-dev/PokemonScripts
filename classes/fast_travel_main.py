from gpc_functions import gpc

class main():
    def __init__(self):
        self.g = gpc(100, "auto_fast_travel.gpc", "Auto Fast Travel", r"Set Destination\nCategory: UP/DOWN\nLocation: Left/Right")
#         print(self.array_to_string([
# ["Centrico Plaza", "Gare de Lumiose", "Pokemon Research Lab", "Hotel Z", "Racine Construction", "Restaurant Le Nah", "Rust Syndicate Office",
# "Lumiose Sewers (Canal Access)", "Quasartico Inc.", "Lysandre Cafe", "Lumiose Sewers (Main Access)", "Hotel Richissime", "Looker Bureau", "Lumiose Museum",
# "Restaurant Le Yeah", "Sushi High Roller", "Restaurant Le Wow", "Justice Dojo"],
# ["Vert Pokemon Center", "Bleu Pokemon Center", "Vernal Pokemon Center", "Magenta Pokemon Center", "Magenta Plaza Pokemon Center", "Rouge Pokemon Center", "Centrico Pokemon Center",
# "Jaune Pokemon Center", "Hibernal Pokemon Center"],
# ["Cafe Cyclone", "Cafe Classe", "Cafe Introversion", "Nouveau Cafe", "Cafe Woof", "Cafe Soleil", "Shutterbug Cafe",
# "Nouveau Cafe Truck No. 2", "Cafe Pokemon-Amie", "Cafe Rouleau", "Cafe Gallant", "Cafe Triste", "Nouveau Cafe Truck No. 3", "Cafe Ultimo",
# "Cafe Action", "Cafe Kizuna", "Cafe Bataille"],
# ["Wild Zone 1", "Wild Zone 2", "Wild Zone 3", "Wild Zone 4", "Wild Zone 5", "Wild Zone 6", "Wild Zone 7",
# "Wild Zone 8", "Wild Zone 9", "Wild Zone 10", "Wild Zone 11", "Wild Zone 12", "Wild Zone 13", "Wild Zone 14",
# "Wild Zone 15", "Wild Zone 16", "Wild Zone 17", "Wild Zone 18", "Wild Zone 19", "Wild Zone 20"]
# ], '[]'))
        self.initialize_variables()

    def convert_single_array(converted_array):
        output_array = []
        for array in converted_array:
            for item in array[:]:
                output_array.append(item)
        return output_array
    

    
    def handle_var_types(self):
        pass
# ********************************COPY/PASTED FUNCTIONS*******************************
    def assign_variable(name, value, num_tabs = 0):
        file.write(f"{name} = {value};\n")

    def declare_variable(type, name, value):
        file.write(f"{type} ")
        assign_variable(name, value)
    
    def declare_string(var_name, target_string):
        variable_name = string_to_variable(var_name)
        file.write(f'const string {variable_name} = "{target_string}";\n')
    
    def declare_strings_from_array(string_array):
        for item in string_array:
            declare_string(item, item)
    
    def modify_variable_value(current_variable, added_value, num_tabs = 1):
        tab = "\t"
        file.write(f'{tab * num_tabs}{current_variable} = {current_variable} + {added_value};\n')
    
    def generate_if_event_press(button, modified_variable, added_value, num_tabs, file):
        generate_if(f"(event_press({button}))", num_tabs, file)
        num_tabs += 1
        modify_variable_value(modified_variable, added_value, num_tabs)
        num_tabs -= 1
        end_block(num_tabs, file)
    
    def generate_if_reassignment(variable_name, comparison, value_assigned, num_tabs):
        generate_if(f'{variable_name} {comparison}', num_tabs, file)
        assign_variable(variable_name, value_assigned, num_tabs + 1)
        write_command(wait, [100], num_tabs + 1, file)
        end_block(num_tabs, file)

# ********************NEXT STARTING POINT**********************
    def write_selections():
        num_tabs = 1
        file.write("function get_destination()" + r'{' + '\n')
        generate_if(f'get_val({zl})', num_tabs, file)
        num_tabs += 1
        num_tabs += 1
        generate_if_event_press(dd, "category", 1, num_tabs, file)
        generate_if_event_press(du, "category", -1, num_tabs, file)
        generate_if_event_press(dl, "location", -1, num_tabs, file)
        generate_if_event_press(dr, "location", 1, num_tabs, file)
        generate_if_reassignment("category", "< 0", 4, num_tabs)
        generate_if_reassignment("category", "> 4", 0, num_tabs)
        generate_if_reassignment('location', '< 0', 'num_per_category[category - 1]', num_tabs)
        generate_if_reassignment('location', '> num_per_category[category - 1]', 0, num_tabs)
        generate_if(f'event_press({rb})', num_tabs, file)
        assign_variable('SCRIPT_RUNNING', '!SCRIPT_RUNNING', num_tabs)
        end_block(num_tabs, file)
        end_block(num_tabs - 1, file)
        end_block(num_tabs - 2, file)
    
    def generate_print(name, num_tabs, file):
        # write_command(x_value, y_value, font, color, string_address)
        write_command("print", [20, 20, "OLED_FONT_MEDIUM", "OLED_WHITE", name], num_tabs, file)    


    def set_coordinate_position(i, num_tabs, file):
        assign_variable("coordinate_position", i, num_tabs)

    def set_coordinates(i, array, num_tabs, file):
        file.write('function set_coordinates()' + r"{" + "\n")
        num_tabs += 1
        assign_variable("category_coordinate", f"{array}[{i}][0]", num_tabs)
        assign_variable("x_coordinate", f"{array}[{i}][1]", num_tabs)
        assign_variable("y_coordinate", f"{array}[{i}][2]", num_tabs)
        end_block(num_tabs - 1, file)

    def assignment_string(name, value):
        string = f'{name} = {value};\n'
        return string

    def write_function_string(name, statement_array, arguments=''):
        new_string = f'function {name}({arguments})' + r'{' + '\n'

        return new_string

    def generate_statement_array(statement_array, num_tabs):
        for item in statement_array:
            new_string += f'{num_tabs * '\t'}{item}'
            new_string += '\t}\n'
        return new_string

    def display_selection(num_tabs, file):
        file.write('function display_selection()' + r'{' + '\n')
        tab = '\t'
        category = 1
        location_num = 0
        for i, location in enumerate(each_location):
            category_index = category - 1
            if num_per_category[category_index] < location_num:
                category += 1
                location_num = 0
            else:
                location_num += 1
            location_variable = string_to_variable(location)
            file.write(f'{tab * num_tabs}if (category == {category} & location == {location_num})' + r'{' + '\n')
            set_coordinate_position(i, num_tabs + 1, file)
            generate_print(location_variable, num_tabs + 1, file)
            end_block(num_tabs, file)
        end_block(num_tabs - 1, file)

    def initialize_variables(self):
        new_string = ''
        new_string += self.g.initialize_int("SCRIPT_RUNNING", "FALSE")
        new_string += self.g.initialize_int("category", "0")
        new_string += self.g.initialize_int("location", "0")
        new_string += self.g.initialize_int('category_coordinate', 0)
        new_string += self.g.initialize_int('x_coordinate', 0)
        new_string += self.g.initialize_int('y_coordinate', 0)
        new_string += self.g.initialize_int('coordinate_position', 0)
        new_string += self.g.initialize_array('num_per_category', gpc.num_per_category)
        new_string += self.g.initialize_array('full_coordinate_array', gpc.full_coordinate_array)
        new_string += self.g.initialize_string("instruction_page", self.g.instruction_page)
        new_string += self.g.declare_strings_from_array(gpc.all_location_names)
        return new_string

e = main()



