import random

class Weapons_attack:
    def __init__(self, attack_types, damage_values):
        self.attack_types = attack_types
        self.damage_values = damage_values
    def perform_attack(self, attack_choice=None):
        if attack_choice is None:  # Random attack if no choice is given
            attack_index = random.randint(0, len(self.attack_types) - 1)
        else:# if user inputs a choice of characters that they choos of special attacks with dmages.
            attack_index = self.attack_types.index(attack_choice)
        attack_type = self.attack_types[attack_index]
        damage = self.damage_values[attack_index]
        print(f"Attack: {attack_type}, Damage: {damage}")
        return damage