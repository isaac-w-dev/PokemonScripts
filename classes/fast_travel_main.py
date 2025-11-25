from gpc_functions import gpc

class main():
    def __init__(self):
        self.g = gpc(100, "auto_fast_travel.gpc", "Auto Fast Travel", "Set Destination\nCategory: UP/DOWN\nLocation: Left/Right")

    def convert_single_array(converted_array):
        output_array = []
        for array in converted_array:
            for item in array[:]:
                output_array.append(item)
        return output_array
    
    def array_to_string(self, array):
        new_string = '['
        for item in array[:-1]:
            if isinstance(item, list):
                new_string += self.array_to_string(item)
            else: new_string += f'{item}, '
        new_string += str(array[-1])
        new_string += ']'
        return new_string
    
    def handle_var_types(self):
        pass
    
    # def array_to_string(self, array, bracket_type = r'{}', quotations = ''):
    #     new_string = bracket_type[0]
    #     for item in array[:-1]:
    #         if isinstance(item, list):
    #             new_string += self.array_to_string(item)
    #         elif isinstance(item, str):
    #             new_string += f'{quotations}{item}{quotations}, '
    #         else: new_string += f'{item}, '
    #     if isinstance(array[-1], not list):
    #         new_string += f'{array[-1]}'
    #     new_string += bracket_type[1]
    #     return new_string

e = main()



