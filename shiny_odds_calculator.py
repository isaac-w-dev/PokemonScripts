import math
vanilla_roll = 1/4096
shiny_charm_roll = 1/1024.4

def get_info():
    reset_time = int(input("Approximate time between resets in seconds: "))
    num_pokemon_range = (int(input("Minimum non-shiny pokemon Spawned: ")), int(input("Maximum non-shiny Pokemon Spawned: ")))
    return reset_time, num_pokemon_range
#
def display_menu():
    print("What are you looking to do today?\n1- Calculate odds for a single shiny over a given length of time\n2- Calculate the length of time to get certain odds of getting a shiny\n3- Calculate the length of time to get a given number of shinies\n4- Exit")
#
def input_selection():
    while True:
        try:
            selection = int(input("Enter selection here: "))
            if selection in range(1, 5): return selection
            print("Integer is out of bounds. Enter an integer between 1 and 4")
        except:
            print("An error occurred, enter an integer between 1 and 4")
        
def main():
    selection = -1
    while True:
        display_menu()
        selection = input_selection()
        reset_time, num_pokemon_range = get_info()
        if (selection == 1 or selection == 2):
            time_hunting = get_time_hunting
            if (selection == 1):
                calc_odds(time_hunting, reset_time, num_pokemon_range)
                # Single shiny over time

            elif (selection == 2):
                pass
        if (selection == 3):
            pass
        if (selection == 4):
            break


        
        

main()
