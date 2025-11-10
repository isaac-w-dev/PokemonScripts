import math
class Main():
    def __init__(self):
        self.shiny_charm_roll = 1/1024.38
        self.vanilla_roll = 1/4096
        self.get_info()
        # print(self.calc_odds(self.reset_time, self.acceptable_species_avg))
        self.calc_time_w_chance(self.reset_time, self.acceptable_species_avg)

    def get_info(self):
        self.reset_time = float(input("Approximate time between resets in seconds: "))
        self.acceptable_species_avg = (float(input("Minimum species of interest Spawned: ")) + float(input("Maximum species of interest Spawned: ")))//2
    
    def calc_time(self, reset_time, pkmn_avg, current_percent, shiny_odds = 1/1024.38):
        current_percent /= 100
        time_to_result = reset_time / pkmn_avg * math.log(1 - current_percent, 1 - shiny_odds)
        return f'\nPercentage of {current_percent * 100}% at:\nNumber of Hours: {time_to_result // 3600}\nNumber of Minutes: {(time_to_result % 3600)//60}\nNumber of Seconds: {time_to_result % 60 // 1}'
        
    def calc_odds(self, reset_time, avg_mons, modifier = 1, odds = 1/1024.38):
        time_elapsed = float(input("Enter the time you plan to hunt in seconds: "))
        odds_over_time = 1 - (1 - odds * modifier) ** (avg_mons * time_elapsed / reset_time)
        return f'{odds_over_time * 100}%'
    
    def calc_shiny_alpha_time(self, num_spawns, reset_time):
        for i in range(num_spawns):
            alpha_chance = input(int("Percentage chance of alpha spawn: "))
            spawn_chance = input(int("Percentage chance of pokemon spawn: "))

    def calc_time_w_chance(self, reset_time, pkmn_avg):
        while True:
            desired_chance = int(input(f"What is the minimum percentage you want to calculate for?\nPercentage chance will be calculated every 5% after up to and including 99.5% (100% is impractical): "))
            if 0 < desired_chance < 100:
                break
            print("Percentage was out of range, reprompting...")

        print(self.calc_time(reset_time, pkmn_avg, desired_chance))

        for i in range(desired_chance + 5 - desired_chance % 5, 100, 5):
            if i == 100:
                i -= .5
            print(self.calc_time(reset_time, pkmn_avg, i))

main = Main()