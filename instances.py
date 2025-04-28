class basic_unit_stats:
    __slots__ = [
        'name', 
        'health', 
        'armor', 
        'attack', 
        'attack_speed',

        'img'
        ]

    def __init__(self, 
                 
                 name : str,
                 health : int,
                 attack : int,
                 attack_speed : int,
                 
                 img : str
                 ):
        self.name = name
        self.health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.img = img

class CallHero(basic_unit_stats):
    pass