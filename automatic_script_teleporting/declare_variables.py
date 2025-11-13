declare_variables = r'''int SCRIPT_RUNNING = FALSE;
int category = 0;
int location = 0;
const string locations_by_type[][]={
    {"Set Location:\nCategory: UP/DOWN\nLocation: Left/Right"},
    {"Facilities",
    "Centrico Plaza", "Gare de Lumiose", "Pokemon Research Lab", "Hotel Z", "Racine Construction", "Restaurant Le Nah", "Rust Syndicate Office",
    "Lumiose Sewers (Canal Access)", "Quasartico Inc.", "Lysandre Cafe", "Lumiose Sewers (Main Access)", "Hotel Richissime", "Looker Bureau", "Lumiose Museum",
    "Restaurant Le Yeah", "Sushi High Roller", "Restaurant Le Wow", "Justice Dojo"},
    {"Pokemon Centers",
    "Vert Pokemon Center", "Bleu Pokemon Center", "Vernal Pokemon Center", "Magenta Pokemon Center", "Magenta Plaza Pokemon Center", "Rouge Pokemon Center", "Centrico Pokemon Center",
    "Jaune Pokemon Center", "Hibernal Pokemon Center"},
    {"Cafes",
    "Cafe Cyclone", "Cafe Classe", "Cafe Introversion", "Nouveau Cafe", "Cafe Woof", "Cafe Soleil", "Shutterbug Cafe",
    "Nouveau Cafe Truck No. 2", "Cafe Pokemon-Amie", "Cafe Rouleau", "Cafe Gallant", "Cafe Triste", "Nouveau Cafe Truck No. 3", "Cafe Ultimo",
    "Cafe Action", "Cafe Kizuna", "Cafe Bataille"},
    {"Wild Zones",
    "Wild Zone 1", "Wild Zone 2", "Wild Zone 3", "Wild Zone 4", "Wild Zone 5", "Wild Zone 6", "Wild Zone 7",
    "Wild Zone 8", "Wild Zone 9", "Wild Zone 10", "Wild Zone 11", "Wild Zone 12", "Wild Zone 13", "Wild Zone 14",
    "Wild Zone 15", "Wild Zone 16", "Wild Zone 17", "Wild Zone 18", "Wild Zone 19", "Wild Zone 20"}
};

const int locations_per_catagory[] ={18, 9, 17, 20};''' + '\n\n'