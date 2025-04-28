class basic_unit_stats:
    __slots__ = [
        'name', 
        'health', 
        'armor', 
        'attack', 
        'attack_speed',

        'img'
        'atk_type'
        ]

    def __init__(self, 
                 
                 name : str,
                 health : int,
                 attack : int,
                 attack_speed : int,
                 
                 img : str,
                 atk_type : dict
                 ):
        self.name = name
        self.health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.img = img
        self.atk_type = atk_type

class CallChar(basic_unit_stats):
    pass


