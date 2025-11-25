def convert_to_single_array(converted_array):
    output_array = []
    for array in converted_array:
        for item in array[:]:
            output_array.append(item)
    return output_array

def write_array_to_file(array, array_name = "full_coordinate_array"):
    with open("full_coordinates.py", "w") as file:
        file.write(f'{array_name}= [')
        for list in array[:-1]:
            file.write('[')
            for item in list[:-1]:
                file.write(f'{item}, ')
            file.write(f'{list[-1]}], ')
        file.write(f'[{array[-1][0]}, {array[-1][1]}, {array[-1][2]}]]\n')