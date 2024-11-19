from character import Character # This imports character.py in Character class.
from weapons import Weapons_attack # This imports weapons.py in Weapons_attack class.

class Evil_Wizard(Character):
     def __init__(self):
        super().__init__("Dark Wizrd", 150)# Call for the class Parent (Character)
        self.attack = Weapons_attack(# self.attack uses class (child) Weapons_attack
          ["Scythe Strike", "Soul Drain", "Summon Undead"], [30, 20, 35]# using miltiple arrays that use 2 arguments.  
        )
           