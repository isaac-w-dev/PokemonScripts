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
        new_string += self.g.initialize_int("first_loop", "TRUE")
        new_string += self.g.initialize_int("coordinate_stage", 1)
        new_string += self.g.initialize_int("stage", 0)
        new_string += self.g.initialize_int("category", "0")
        new_string += self.g.initialize_int("location", "0")
        new_string += self.g.initialize_int('category_coordinate', 0)
        new_string += self.g.initialize_int('x_coordinate', 0)
        new_string += self.g.initialize_int('y_coordinate', 0)
        new_string += self.g.initialize_int('coordinate_position', 0)
        new_string += self.g.initialize_int('i', 0)
        new_string += self.g.initialize_array('num_per_category', gpc.num_per_category)
        new_string += self.g.initialize_array('full_coordinate_array', gpc.full_coordinate_array)
        new_string += self.g.initialize_string("program_name", 'ZA MENU TELEPORTATION')
        new_string += self.g.initialize_string("instruction_page", self.g.instruction_page)
        new_string += self.g.init_strings_from_array(display_names)
        return new_string
    
    def write_init(self):
        block = self.g.create_full_block
        init = self.g.start_code_block
        new_string = block(init('', 'init', ''),
                        self.g.generate_print(20, 20, 'OLED_FONT_MEDIUM', 'OLED_WHITE', 'program_name'),
                        self.g.call_function('set_ledx', ['LED_1', 1]),
                        self.g.call_function('set_ledx', ['LED_2', 2]),
                        self.g.call_function('set_ledx', ['LED_3', 3]),
                        self.g.call_function('set_ledx', ['LED_4', 4]))
        return new_string
    
    def write_wait_combo(self):
        call = self.g.call_function
        new_string = self.g.combo_block('wait_combo', call("wait", [6000]), self.g.reassign_variable("stage", 0), call('combo_stop_all'))
        return new_string

    def write_selections(self):
        if_block = self.g.create_full_block
        start_block = self.g.start_if
        plus_equal = self.g.var_plus_equal
        reassign = self.g.reassign_variable

        new_string = if_block(self.g.start_function("get_destination", []),
                        if_block(start_block(f'get_val({gpc.zl})'),
                            if_block(start_block(f'event_press({gpc.dd})'), plus_equal('category', 1), reassign('SCRIPT_RUNNING', 'FALSE')),
                            if_block(start_block(f'event_press({gpc.du})'), plus_equal('category', -1), reassign('SCRIPT_RUNNING', 'FALSE')),
                            if_block(start_block(f'event_press({gpc.dr})'), plus_equal('location', 1), reassign('SCRIPT_RUNNING', 'FALSE')),
                            if_block(start_block(f'event_press({gpc.dl})'), plus_equal('location', -1), reassign('SCRIPT_RUNNING', 'FALSE')),
                            if_block(start_block(f'category < 0'), reassign('category', 4)),
                            if_block(start_block(f'category > 4'), reassign('category', 0)),
                            if_block(start_block(f'category != 0 && location < 0'), reassign('location', 'num_per_category[category - 1] - 1')),
                            if_block(start_block(f'category != 0 && location >= num_per_category[category - 1]'), reassign('location', '0')),
                            if_block(start_block(f'event_press({gpc.rb})'), reassign('SCRIPT_RUNNING', '!SCRIPT_RUNNING'), reassign('first_loop', 'TRUE'))
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
    
    def set_coordinate_position(self, i):
        return self.g.reassign_variable("coordinate_position", i)
    
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
        new_string = self.g.create_full_block(self.g.start_function('set_coordinates'),
                                            self.g.reassign_variable('category_coordinate', f'full_coordinate_array[coordinate_position][0]'),
                                            self.g.reassign_variable('x_coordinate', f'full_coordinate_array[coordinate_position][1]'),
                                            self.g.reassign_variable('y_coordinate', f'full_coordinate_array[coordinate_position][2]'),
                                            self.g.reassign_variable('stage', 1))
        return new_string
    
    def display_selections(self):
        function = self.g.start_function
        if_block = self.g.create_full_block
        start_if = self.g.start_if
        new_string = function('display_selections', [])
        category = 0
        location_num = 0
        single_array = self.convert_single_array(gpc.locations_in_file)
        new_string += if_block(start_if(f'category == {category}'), self.g.generate_print(20, 20, 'OLED_FONT_MEDIUM', 'OLED_WHITE', 'instruction_page'))
        category = 1
        for location in single_array[1:]:
            location = self.g.string_to_variable(location)
            new_string += start_if(f'category == {category} && location == {location_num}')
            new_string += self.g.generate_print(20, 20, 'OLED_FONT_MEDIUM', 'OLED_WHITE', f'{location}')
            
            if location_num == 0:
                new_string += self.g.end_block()

            else:
                index = self.get_index_location(category, location_num)
                new_string += self.set_coordinate_position(index)
                new_string += self.g.end_block()
            category, location_num = self.return_next_location(category, location_num)
        new_string += self.g.end_block()
        return new_string
    
    def write_input_combos(self):
        assign = self.g.var_plus_equal
        add_if = self.g.start_if
        block = self.g.create_full_block
        new_string = self.g.combo_block('down_input_loop',
                            block(add_if('!combo_running(down_input_loop)'),
                                            self.g.button_input(gpc.dd),
                                            assign('i', 1)))
        new_string += self.g.combo_block('up_input_loop',
                            block(add_if('!combo_running(up_input_loop)'),
                                            self.g.button_input(gpc.du),
                                            assign('i', 1)))
        new_string += self.g.combo_block('left_input_loop',
                            block(add_if('!combo_running(left_input_loop)'),
                                            self.g.button_input(gpc.dl),
                                            assign('i', 1)))
        new_string += self.g.combo_block('right_input_loop',
                            block(add_if('!combo_running(right_input_loop)'),
                                            self.g.button_input(gpc.dr),
                                            assign('i', 1)))
        return new_string
        
    def write_menu_select(self):
        new_string = self.g.combo_block('menu_select', self.g.button_sequence(gpc.plus, gpc.yb))
        return new_string

    def write_select_category(self):
        combo = self.g.call_combo
        build_if = self.g.start_if
        assign = self.g.reassign_variable
        new_string = self.g.combo_block('select_category',
                                            self.g.create_full_block(build_if("i == 0"), self.g.button_input(gpc.min)),
                                                self.g.create_full_block(build_if('i < category_coordinate && first_loop == TRUE'), combo('down_input_loop')),
                                                self.g.create_full_block(self.g.start_else(),
                                                    assign('first_loop', 'FALSE'),
                                                    self.g.button_input(gpc.ab),
                                                    assign('stage', 3),
                                                    assign('i', 0)))
        return new_string
    # START HERE
    def write_coordinate_navigation(self):
        block = self.g.create_full_block
        loop = self.g.start_for_loop
        combo = self.g.call_combo
        start_if = self.g.start_if
        start_else = self.g.start_else
        call = self.g.call_function
        new_string = self.g.combo_block('coordinate_navigation',
                        block(start_if('coordinate_stage == 1'),
                            block(start_if('x_coordinate < 0'),
                                block(start_if('i < (x_coordinate * -1)'), combo('left_input_loop')),
                                block(start_else(), self.g.reassign_variable('coordinate_stage', 2), call("wait", [10]), self.g.reassign_variable('i', 0))),
                        block(start_else(),
                            block(start_if('i < x_coordinate '), combo('right_input_loop')),
                                block(start_else(), self.g.reassign_variable('coordinate_stage', 2), call("wait", [10]), self.g.reassign_variable('i', 0)))),
                        block(start_if("coordinate_stage == 2"),
                            block(start_if('y_coordinate < 0'),
                                block(start_if('i < (y_coordinate * -1)'), combo('up_input_loop')),
                            block(start_else(), self.g.reassign_variable('coordinate_stage', 3), call("wait", [10]), self.g.reassign_variable('i', 0))),
                            block(start_else(),
                                block(start_if('i < y_coordinate'), combo('down_input_loop')),
                                block(start_else(), self.g.reassign_variable('coordinate_stage', 3), call("wait", [10]), self.g.reassign_variable('i', 0)))),
                        block(start_if("coordinate_stage == 3"), self.g.reassign_variable('stage', 4), call("wait", [10]), self.g.reassign_variable('coordinate_stage', 1), self.g.reassign_variable('i', 0)))
        return new_string

    def write_main(self):
        block = self.g.create_full_block
        start_main = self.g.start_code_block
        start_if = self.g.start_if
        start_else = self.g.start_else
        combo = self.g.call_combo
        call = self.g.call_function
        assign = self.g.reassign_variable
        new_string = block(start_main('', 'main', ''),
                        call("get_destination"),
                        call("display_selections"),
                        block(start_if("SCRIPT_RUNNING"),
                            block(start_if('stage == 0 && !combo_running(wait_combo)'),
                                block(start_if('first_loop'), call('set_coordinates')), assign('stage', 1)),
                            block(start_if('stage == 1'), combo('menu_select'), assign('stage', 2)),
                            block(start_if('stage == 2 && !combo_running(menu_select)'),
                                block(start_if('first_loop'), combo("select_category"), assign("first_loop", "FALSE"))),
                            block(start_if('stage == 3 && !combo_running(select_category)'), combo("coordinate_navigation")),
                            block(start_if('stage == 4 && !combo_running(coordinate_navigation)'), combo('wait_combo'))),
                        block(start_else(), call('combo_stop_all')))
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
    
    def write_all_combos(self):
        new_string = self.write_wait_combo()
        new_string += self.write_input_combos()
        new_string += self.write_menu_select()
        new_string += self.write_select_category()
        new_string += self.write_coordinate_navigation()
        return new_string
    
    def main(self):
        new_string = self.initialize_variables()
        new_string += self.write_init()
        new_string += self.write_main()
        new_string += self.write_all_combos()
        new_string += self.write_selections()
        new_string += self.set_coordinates()
        new_string += self.display_selections()
        new_string = self.insert_tabs(new_string)
        self.g.file.write(new_string)

e = main()



