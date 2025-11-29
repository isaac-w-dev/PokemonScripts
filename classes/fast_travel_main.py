from gpc_functions import gpc

class main():
    def __init__(self):
        self.g = gpc(100, "auto_fast_travel.gpc", "Auto Fast Travel", r"Set Destination\nCategory: UP/DOWN\nLocation: Left/Right")
        self.main()

    def convert_single_array(self, converted_array):
        output_array = []
        for array in converted_array:
            for item in array[:]:
                output_array.append(item)
        return output_array   

    def initialize_variables(self):
        display_names = self.convert_single_array(gpc.locations_in_file[1:])
        new_string = self.g.initialize_int("SCRIPT_RUNNING", "FALSE")
        new_string += self.g.declare_int("first_loop")
        new_string += self.g.initialize_int("category", "0")
        new_string += self.g.initialize_int("location", "0")
        new_string += self.g.initialize_int('category_coordinate', 0)
        new_string += self.g.initialize_int('x_coordinate', 0)
        new_string += self.g.initialize_int('y_coordinate', 0)
        new_string += self.g.initialize_int('coordinate_position', 0)
        new_string += self.g.initialize_int('i', 0)
        new_string += self.g.initialize_array('num_per_category', gpc.num_per_category)
        new_string += self.g.initialize_array('full_coordinate_array', gpc.full_coordinate_array)
        new_string += self.g.initialize_string("instruction_page", self.g.instruction_page)
        new_string += self.g.declare_strings_from_array(display_names)
        return new_string
    
    def write_selections(self):
        if_block = self.g.create_full_block
        start_block = self.g.start_if_block
        plus_equal = self.g.var_plus_equal
        reassign = self.g.reassign_variable

        new_string = if_block(self.g.start_function("get_destination", []),
                        if_block(start_block(f'get_val({gpc.zl})'),
                            if_block(start_block(f'event_press({gpc.dd})'),
                                plus_equal('category', 1),
                                self.g.reassign_variable('first_loop', 'TRUE')),
                            if_block(start_block(f'event_press({gpc.du})'),
                                plus_equal('category', -1),
                                self.g.reassign_variable('first_loop', 'TRUE')),
                            if_block(start_block(f'event_press({gpc.dr})'),
                                plus_equal('location', 1)),
                            if_block(start_block(f'event_press({gpc.dl})'),
                                plus_equal('location', -1)),
                            if_block(start_block(f'category < 0'),
                                reassign('category', 4)),
                            if_block(start_block(f'category < 4'),
                                reassign('category', 0)),
                            if_block(start_block(f'category != 0 && location < 0'),
                                reassign('location', 'num_per_category[category - 1]')),
                            if_block(start_block(f'category != 0 && location > num_per_category[category - 1]'),
                                reassign('location', '0')),
                            if_block(start_block(f'event_press({gpc.rb})'),
                                reassign('SCRIPT_RUNNING', '!SCRIPT_RUNNING')
                                )
                            )
                        )
        return new_string
    
    def get_index_location(self, category, location):
        if category == 0 or location == 0: print("Error occured either location or category is 0")
        index = -1
        for i in range(category - 1, 0, -1):
            index += gpc.num_per_category[i - 1]
        index += location
        return index
    
    def set_coordinate_position(self, i): return self.g.reassign_variable("coordinate_position", i)
    
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
    
    def set_coordinates(self):
        new_string = self.g.create_full_block(self.g.start_function('set_coordinates', []),
                                            self.g.reassign_variable('category_coordinate', f'full_coordinate_array[coordinate_position][0]'),
                                            self.g.reassign_variable('x_coordinate', f'full_coordinate_array[coordinate_position][1]'),
                                            self.g.reassign_variable('y_coordinate', f'full_coordinate_array[coordinate_position][2]'))
        return new_string
    
    def display_selections(self):
        function = self.g.start_function
        if_block = self.g.create_full_block
        start_if = self.g.start_if_block
        new_string = function('display_selections', [])
        category = 0
        location_num = 0
        single_array = self.convert_single_array(gpc.locations_in_file)
        new_string += if_block(start_if(f'category == {category}'), self.g.generate_print(20, 20, 'OLED_FONT_MEDIUM', 'OLED_WHITE', 'instruction_page[0]'))
        category = 1
        for location in single_array[1:]:
            location = self.g.string_to_variable(location)
            new_string += start_if(f'category == {category} && location == {location_num}')
            new_string += self.g.generate_print(20, 20, 'OLED_FONT_MEDIUM', 'OLED_WHITE', f'{location}[0]')
            
            if location_num == 0:
                new_string += self.g.end_block()

            else:
                index = self.get_index_location(category, location_num)
                new_string += self.set_coordinate_position(index)
                new_string += self.g.end_block()
            category, location_num = self.return_next_location(category, location_num)
        new_string += self.g.write_command('set_coordinates', [])
        new_string += self.g.end_block()
        return new_string
    #*********************ADD INITIAL MENU BUTTON PRESSES*********************
    def write_category_navigation(self):
        new_string = self.g.create_full_block(self.g.start_function('map_to_menu', []),
                                            self.g.start_code_block('for', '(i = 0; i < category_coordinate; i++)'),
                                            self.g.button_input(gpc.dd),
                                            self.g.end_block(),
                                            self.g.button_input(gpc.ab))
        return new_string
    
    def write_coordinate_navigation(self):
        block = self.g.create_full_block
        loop = self.g.start_for_loop
        funct = self.g.start_function
        start_if = self.g.start_if_block
        start_else = self.g.start_else
        input = self.g.button_input
        new_string = block(funct('write_coordinate_navigation', []),
                        block(start_if('x_coordinate < 0'),
                            block(loop('i = 0', 'i < (x_coordinate * -1)', 'i++'),
                                input(gpc.dl))),
                        block(start_else(),
                            block(loop('i = 0', 'i < x_coordinate', 'i++'),
                                input(gpc.dr))),
                        block(start_if('y_coordinate < 0'),
                            block(loop('i = 0', 'i < (y_coordinate * -1)', 'i++'),
                                input(gpc.du))),
                        block(start_else(),
                            block(loop('i = 0', 'i < y_coordinate', 'i++'),
                                input(gpc.dd)))
                                    )
        return new_string

    def write_main(self):
        block = self.g.create_full_block
        start_main = self.g.start_code_block
        start_if = self.g.start_if_block
        call = self.g.call_function
        funct = self.g.start_function
        assign = self.g.reassign_variable
        new_string = block(start_main('', 'main', ''),
                        call("get_destination"), call("display_selections"),
                        block(start_if("SCRIPT_RUNNING"),
                            block(start_if('first_loop'),
                                call("map_to_menu"), assign("first_loop", "FALSE")),
                            call("write_coordinate_navigation")))
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
            modified_array.append(line + '\n' + f'{num_tabs * '\t'}')
        new_string = ''.join(modified_array)
        return new_string
            
    def main(self):
        new_string = self.initialize_variables()
        new_string += self.write_selections()
        new_string += self.set_coordinates()
        new_string += self.display_selections()
        new_string += self.write_category_navigation()
        new_string += self.write_coordinate_navigation()
        new_string += self.write_main()
        new_string = self.insert_tabs(new_string)
        self.g.file.write(new_string)

e = main()



