location_data = [
['Centrico Plaza', 'Gare de Lumiose', 'Pokemon Research Lab', 'Hotel Z', 'Racine Construction', 'Restaurant Le Nah', 'Rust Syndicate Office', 'Lumiose Sewers (Canal Access)', 'Quasartico Inc.', 'Lysandre Cafe', 'Lumiose Sewers (Main Access)', 'Hotel Richissime', 'Looker Bureau', 'Lumiose Museum', 'Restaurant Le Yeah', 'Sushi High Roller', 'Restaurant Le Wow', 'Justice Dojo', 'Vert Pokemon Center', 'Bleu Pokemon Center', 'Vernal Pokemon Center', 'Magenta Pokemon Center', 'Magenta Plaza Pokemon Center', 'Rouge Pokemon Center', 'Centrico Pokemon Center', 'Jaune Pokemon Center', 'Hibernal Pokemon Center', 'Cafe Cyclone', 'Cafe Classe', 'Cafe Introversion', 'Nouveau Cafe', 'Cafe Woof', 'Cafe Soleil', 'Shutterbug Cafe', 'Nouveau Cafe Truck No. 2', 'Cafe Pokemon-Amie', 'Cafe Rouleau', 'Cafe Gallant', 'Cafe Triste', 'Nouveau Cafe Truck No. 3', 'Cafe Ultimo', 'Cafe Action', 'Cafe Kizuna', 'Cafe Bataille', 'Wild Zone 1', 'Wild Zone 2', 'Wild Zone 3', 'Wild Zone 4', 'Wild Zone 5', 'Wild Zone 6', 'Wild Zone 7', 'Wild Zone 8', 'Wild Zone 9', 'Wild Zone 10', 'Wild Zone 11', 'Wild Zone 12', 'Wild Zone 13', 'Wild Zone 14', 'Wild Zone 15', 'Wild Zone 16', 'Wild Zone 17', 'Wild Zone 18', 'Wild Zone 19', 'Wild Zone 20'],
['All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'All travel spots', 'Facilities', 'Facilities', 'Facilities', 'All travel spots', 'All travel spots', 'All travel spots', 'Facilities', 'Facilities', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Pokemon Centers', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Cafes', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones', 'Wild Zones'],
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, -2], [1, -1], [1, 0], [1, 1], [1, 2], [1, 0], [2, 0], [2, 1], [2, -1], [2, 0], [2, 1], [-1, -1], [-1, 0], [0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [-2, -1], [-2, 0], [-1, -1], [-1, 0], [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, -2], [1, -1], [1, 0], [1, 1], [-2, 0], [2, 0], [2, 1], [2, 2], [-1, -3], [-1, -2], [-1, -1], [-1, 0], [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, -2], [1, -1], [1, 0], [1, 1], [1, 2], [1, 3], [2, -2], [2, -1], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]]
]
categories = ["All travel spots", "Facilities", "Pokemon Centers", "Cafes", "Wild Zones"]
locations_in_file = [
["Centrico Plaza", "Gare de Lumiose", "Pokemon Research Lab", "Hotel Z", "Racine Construction", "Restaurant Le Nah", "Rust Syndicate Office",
"Lumiose Sewers (Canal Access)", "Quasartico Inc.", "Lysandre Cafe", "Lumiose Sewers (Main Access)", "Hotel Richissime", "Looker Bureau", "Lumiose Museum",
"Restaurant Le Yeah", "Sushi High Roller", "Restaurant Le Wow", "Justice Dojo"],
["Vert Pokemon Center", "Bleu Pokemon Center", "Vernal Pokemon Center", "Magenta Pokemon Center", "Magenta Plaza Pokemon Center", "Rouge Pokemon Center", "Centrico Pokemon Center",
"Jaune Pokemon Center", "Hibernal Pokemon Center"],
["Cafe Cyclone", "Cafe Classe", "Cafe Introversion", "Nouveau Cafe", "Cafe Woof", "Cafe Soleil", "Shutterbug Cafe",
"Nouveau Cafe Truck No. 2", "Cafe Pokemon-Amie", "Cafe Rouleau", "Cafe Gallant", "Cafe Triste", "Nouveau Cafe Truck No. 3", "Cafe Ultimo",
"Cafe Action", "Cafe Kizuna", "Cafe Bataille"],
["Wild Zone 1", "Wild Zone 2", "Wild Zone 3", "Wild Zone 4", "Wild Zone 5", "Wild Zone 6", "Wild Zone 7",
"Wild Zone 8", "Wild Zone 9", "Wild Zone 10", "Wild Zone 11", "Wild Zone 12", "Wild Zone 13", "Wild Zone 14",
"Wild Zone 15", "Wild Zone 16", "Wild Zone 17", "Wild Zone 18", "Wild Zone 19", "Wild Zone 20"]
]
each_location = location_data[0]
fastest_categories = location_data[1]
fastest_coordinates = location_data[2]
full_coordinate_array= [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 1, -2], [0, 1, -1], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 1, 0], [1, 2, 0], [1, 2, 1], [0, 2, -1], [0, 2, 0], [0, 2, 1], [1, -1, -1], [1, -1, 0], [2, 0, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, -2, -1], [2, -2, 0], [2, -1, -1], [2, -1, 0], [3, 0, 0], [3, 0, 1], [3, 0, 2], [3, 0, 3], [3, 0, 4], [3, 1, -2], [3, 1, -1], [3, 1, 0], [3, 1, 1], [3, -2, 0], [3, 2, 0], [3, 2, 1], [3, 2, 2], [3, -1, -3], [3, -1, -2], [3, -1, -1], [3, -1, 0], [4, 0, 0], [4, 0, 1], [4, 0, 2], [4, 0, 3], [4, 0, 4], [4, 1, -2], [4, 1, -1], [4, 1, 0], [4, 1, 1], [4, 1, 2], [4, 1, 3], [4, 2, -2], [4, 2, -1], [4, 2, 0], [4, 2, 1], [4, 2, 2], [4, 2, 3], [4, 2, 4], [4, 2, 5], [4, 2, 6]]
num_per_category = [17, 8, 16, 19]

