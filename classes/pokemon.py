class pokemon():
    def __init__(self, tier, name, types, abilities, HP, Atk, Def, SpAtk, SpDef, Spd, BST):
        self.tier = tier
        self.name = name
        self.types = types
        self.abilities = abilities
        self.HP = HP
        self.Atk = Atk
        self.Def = Def
        self.SpAtk = SpAtk
        self.SpDef = SpDef
        self.Spd = Spd
        self.BST = BST

    def add_moves(self):
        self.moves = []
        