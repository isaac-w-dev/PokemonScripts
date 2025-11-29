from gpc_functions import gpc

class main():
    def __init__(self):
        self.g = gpc(100, "auto_fast_travel.gpc", "Auto Fast Travel", r"Set Destination\nCategory: UP/DOWN\nLocation: Left/Right")
        self.main()
        # self.g.file.write(self.initialize_variables())

    def convert_single_array(self, converted_array):
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
    def write_selections(self):
        if_block = self.g.create_full_block
        start_block = self.g.start_if_block
        plus_equal = self.g.var_plus_equal
        reassign = self.g.reassign_variable
        new_string = if_block(self.g.start_function("get_destination", []),
                        if_block(start_block(f'get_val({gpc.zl})'),
                            if_block(start_block(f'event_press({gpc.dd})'),
                                plus_equal('category', 1)),
                            if_block(start_block(f'event_press({gpc.du})'),
                                plus_equal('category', -1)),
                            if_block(start_block(f'event_press({gpc.dr})'),
                                plus_equal('location', 1)),
                            if_block(start_block(f'event_press({gpc.dl})'),
                                plus_equal('location', -1)),
                            if_block(start_block(f'category < 0'),
                                reassign('category', 4)),
                            if_block(start_block(f'category < 4'),
                                reassign('category', 0)),
                            if_block(start_block(f'location < 0'),
                                reassign('location', 'num_per_category[category - 1]')),
                            if_block(start_block(f'location > num_per_category[category - 1]'),
                                reassign('location', '0')),
                            if_block(start_block(f'event_press({gpc.rb})'),
                                reassign('SCRIPT_RUNNING', '!SCRIPT_RUNNING')
                                )
                            )
                        )
        return new_string
    
    def generate_print(self, name):
        # write_command(x_value, y_value, font, color, string_address)
        return self.g.write_command("print", [20, 20, "OLED_FONT_MEDIUM", "OLED_WHITE", name])    


    def set_coordinate_position(self, i):
        return self.g.reassign_variable("coordinate_position", i)

    def set_coordinates(self):
        new_string = self.g.create_full_block(self.g.start_function('set_coordinates', []),
                                            self.g.reassign_variable('category_coordinate', f'full_coordinate_array[coordinate_position][0]'),
                                            self.g.reassign_variable('x_coordinate', f'full_coordinate_array[coordinate_position][1]'),
                                            self.g.reassign_variable('y_coordinate', f'full_coordinate_array[coordinate_position][2]'))
        return new_string

    def assignment_string(name, value):
        string = f'{name} = {value};\n'
        return string

    def write_function_string(name, statement_array, arguments=''):
        new_string = f'function {name}({arguments})' + r'{' + '\n'

        return new_string

    def generate_statement_array(self, statement_array):
        for item in statement_array:
            new_string += f'{item}'
            new_string += '}\n'
        return new_string

    def display_selections(self):
        function = self.g.start_function
        if_block = self.g.create_full_block
        start_if = self.g.start_if_block
        new_string = function('display_selections', [])
        category = 0
        location_num = 0
        single_array = self.convert_single_array(gpc.locations_in_file)
        # **************ONLY ASSIGNS 62 OUT OF 65 COORDINATES LIKELY OFFSET*********************
        for location in single_array:
            location = self.g.string_to_variable(location)
            new_string += start_if(f'category == {category} || location == {location_num}')
            new_string += self.g.write_command('print', [20, 20, 'OLED_FONT_MEDIUM', 'OLED_WHITE', f'{location}[0]'])
            
            if location_num == 0 or category == 0:
                new_string += self.g.end_block()

            else:
                index = self.get_index_location(category, location_num)
                new_string += self.set_coordinate_position(index)
                new_string += self.g.end_block()
            category, location_num = self.return_next_location(category, location_num)
        new_string += self.g.write_command('set_coordinates', [])
        new_string += self.g.end_block()
        return new_string

    def return_next_location(self, category, location):
        if category == 0:
            return 1, 0
        category_index = category - 1

        if (gpc.num_per_category[category_index]) <= location:
            category += 1
            location = 0
        else:
            location += 1

        return category, location

    def get_index_location(self, category, location):
        if category == 0 or location == 0: print("Error occured either location or category is 0")
        index = -1
        for i in range(category - 1, 0, -1):
            index += gpc.num_per_category[i - 1]
        index += location
        return index
        


    def initialize_variables(self):
        display_names = self.convert_single_array(gpc.locations_in_file)
        new_string = self.g.initialize_int("SCRIPT_RUNNING", "FALSE")
        new_string += self.g.initialize_int("category", "0")
        new_string += self.g.initialize_int("location", "0")
        new_string += self.g.initialize_int('category_coordinate', 0)
        new_string += self.g.initialize_int('x_coordinate', 0)
        new_string += self.g.initialize_int('y_coordinate', 0)
        new_string += self.g.initialize_int('coordinate_position', 0)
        new_string += self.g.initialize_array('num_per_category', gpc.num_per_category)
        new_string += self.g.initialize_array('full_coordinate_array', gpc.full_coordinate_array)
        new_string += self.g.initialize_string("instruction_page", self.g.instruction_page)
        new_string += self.g.declare_strings_from_array(display_names)
        return new_string
    
    def insert_tabs(self, new_string):
        code_array = new_string.split('\n')
        modified_array = []
        num_tabs = 0
        for line in code_array:
            if (r'{' in line):
                num_tabs += 1
            if (r'}' in line):
                num_tabs -= 1
            print(line)
            modified_array.append(line + '\n' + f'{num_tabs * '\t'}')
        new_string = ''.join(modified_array)
        return new_string
            
    def main(self):
        new_string = self.initialize_variables()
        new_string += self.write_selections()
        new_string += self.set_coordinates()
        new_string += self.display_selections()
        new_string = self.insert_tabs(new_string)
        self.g.file.write(new_string)

e = main()



