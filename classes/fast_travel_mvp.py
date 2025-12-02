from gpc_functions import gpc

# Wild zone 16 for mvp

class mvp(gpc):
    inputs = [gpc.du, gpc.dd, gpc.dl, gpc.dr, gpc.plus, gpc.min, gpc.ab, gpc.bb, gpc.xb, gpc.yb]
    button_names = ["press_up", "press_down", "press_left", "press_right", "press_plus", "press_minus", "press_a", "press_b", "press_x", "press_y"]

    def __init__(self, location):
        super().__init__(200, 'fast_travel_mvp.gpc', 'Minimum Viable Product', 'Press ZR and R to Start or Stop the script')
        self.location = location
        self.main()

    def initialize_variables(self):
        print(self.get_fastest_coordinates(self.location))
        self.cat, self.x, self.y = self.get_fastest_coordinates(self.location)
        # display_names = self.convert_single_array(gpc.locations_in_file[1:])
        new_string = self.initialize_int("SCRIPT_RUNNING", "FALSE")
        new_string += self.initialize_int("first_loop", "TRUE")
        # new_string += self.g.initialize_int("coordinate_stage", 1)
        new_string += self.initialize_int("stage", 0)
        new_string += self.initialize_int("menu_stage", 0)
        new_string += self.initialize_int("location_stage", 0)
        new_string += self.initialize_int("category_stage", 0)
        # new_string += self.g.initialize_int("category", "0")
        # new_string += self.g.initialize_int("location", "0")
        new_string += self.initialize_int('category_coordinate', self.cat)
        new_string += self.initialize_int('x_coordinate', self.x)
        new_string += self.initialize_int('y_coordinate', self.y)
        # new_string += self.g.initialize_int('coordinate_position', 0)
        # new_string += self.initialize_int('i', 0)
        # new_string += self.g.initialize_array('num_per_category', gpc.num_per_category)
        # new_string += self.g.initialize_array('full_coordinate_array', gpc.full_coordinate_array)
        new_string += self.initialize_string("program_name", 'ZA MENU TELEPORTATION')
        new_string += self.initialize_string("running", 'Running')
        new_string += self.initialize_string("stopped", 'Stopped')
        new_string += self.initialize_string("instruction_page", self.instruction_page)
        # new_string += self.g.init_strings_from_array(display_names)
        return new_string
    
    def get_index(self, location_name):
        return self.all_location_names.index(location_name)
    
    def get_fastest_coordinates(self, location_name):
        index = self.get_index(location_name)
        return self.full_coordinate_array[index]

    def all_button_combos(self):
        combo = self.combo_block
        input = self.button_input
        new_string = ''
        for i,  button in enumerate(self.inputs):
            new_string += combo(self.button_names[i], input(button))
        return new_string
    
    def selection_options(self):
        reassign = self.reassign_variable

        new_string = self.function_block("selection_options",
                        self.if_block(f'get_val({gpc.zl})',
                            self.if_block(f'event_press({gpc.rb})',
                                    reassign('SCRIPT_RUNNING', '!SCRIPT_RUNNING'), reassign('first_loop', 'TRUE'), self.reassign_variable('stage', 0), self.reassign_variable('menu_stage', 0), self.reassign_variable('category_stage', 0), self.reassign_variable('location_stage', 0), self.call_function('combo_stop_all'))
                            )
                        )
        return new_string
    
    def display_script_state(self):
        new_string = self.function_block('display_script_state',
                        self.if_block('SCRIPT_RUNNING', self.configure_led(3, 1), self.configure_led(2, 0), self.generate_print(10, 20, 'OLED_FONT_MEDIUM', 'OLED_WHITE', 'running')),
                        self.else_block(self.configure_led(2, 1), self.configure_led(3, 0), self.generate_print(10, 20, 'OLED_FONT_MEDIUM', 'OLED_WHITE', 'stopped')))
        return new_string
        
    def open_menu(self):
        new_string = self.function_block('open_menu', self.create_combo_ladder('menu_stage', 'stage', ['press_plus', 'press_y']))
        
        return new_string
    


    def category_select(self):
        array = []
        array.append('press_minus')
        for i in range(self.cat):
            array.append('press_down')
        array.append('press_a')
        return self.function_block('category_select', self.if_block('first_loop', self.create_combo_ladder('category_stage', 'stage', array)))
    # self.create_combo_loop('category_coordinate', 'i', 'press_down', 'stage', self.reassign_variable('first_loop', 'FALSE'))),
    # self.else_block(self.var_plus_equal('stage', 1)))
    
    def location_selection(self):
        array = []
        for i in range(abs(self.x)):
            if self.x < 0:
                array.append('press_left')
            else: array.append('press_right')

        for i in range(abs(self.y)):
            if self.y < 0: array.append('press_up')
            else: array.append('press_down')

        array.append('press_a')

        return self.function_block('location_selection', self.create_combo_ladder('location_stage', 'stage', array))
    
    def reset_function(self):
        return self.function_block('reset_function', self.call_combo('wait_combo'))

    def wait_combo(self):
        return self.combo_block('wait_combo', self.call_function('combo_stop_all'), self.call_function('wait', [6000]), self.reassign_variable('stage', 0))

    def all_combos(self):
        new_string = self.all_button_combos()
        new_string += self.wait_combo()
        return new_string
    
    def all_functions(self):
        new_string = self.selection_options()
        new_string += self.display_script_state()
        new_string += self.open_menu()
        new_string += self.category_select()
        new_string += self.location_selection()
        new_string += self.reset_function()
        return new_string
    
    def write_main(self):
        return self.main_block(self.call_function('selection_options'), self.call_function('display_script_state'), self.if_block('SCRIPT_RUNNING', self.create_function_ladder('stage', 'open_menu', 'category_select', 'location_selection', 'reset_function')))

    def main(self):
        write = self.write_file
        new_string = self.initialize_variables()
        new_string += self.write_main()
        new_string += self.all_combos()
        new_string += self.all_functions()
        new_string = self.insert_tabs(new_string)
        write(new_string)

m = mvp("Wild Zone 16")
