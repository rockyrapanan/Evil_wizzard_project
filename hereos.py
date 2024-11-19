from character import Character # This imports character.py in Character class.
from weapons import Weapons_attack # This imports weapons.py in Weapons_attack class.

# 4 class characters:
class Lycan_Knight(Character):# 1 of 4 characters to face Evil Wizard.
    def __init__(self):
        super().__init__("Lycan Knight", 100)# Call for the class Parent (Character)
        self.attack = Weapons_attack( # self.attack uses class (child) Weapons_attack
            ["Sword Slash", "Shield Bash", "Lightning Strike"], [15, 20, 25]# using miltiple arrays that use 2 arguments.
        )
        
class Pheonix(Character):
    def __init__(self):
        super().__init__("Pheonix", 100)# Call for the class Parent (Character)
        self.attack = Weapons_attack(# self.attack uses class (child) Weapons_attack
            ["Flame Burst", "Healing Flames", "Phoenix Dive"], [25, -20, 30]# using miltiple arrays that use 2 arguments.
        )
           
class Soul_Reaper(Character):
    def __init__(self):
        super().__init__("Soul Reaper", 100)# Call for the class Parent (Character)
        self.attack = Weapons_attack(# self.attack uses class (child) Weapons_attack
           ["Scythe Strike", "Soul Drain", "Summon Undead"], [30, 20, 35]# using miltiple arrays that use 2 arguments. 
        )
class Evil_Wizard(Character):
     def __init__(self):
        super().__init__("Dark Wizrd", 150)# Call for the class Parent (Character)
        self.attack = Weapons_attack(# self.attack uses class (child) Weapons_attack
          ["Scythe Strike", "Soul Drain", "Summon Undead"], [30, 20, 35]# using miltiple arrays that use 2 arguments.  
        )
           