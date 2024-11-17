# Name: Leonardo L. Rapanan
# Project: Defeat The Evil Wizard

'''Delivarables:'''
# A Python script containing:
# Four character classes (including two new ones).
# Two unique abilities for each character.
# A working turn-based battle system.
# Display victory or defeat messages at the end.
'''Bonus Ooption'''
# Create additional character classes with more complex mechanics.
# Add random elements to the wizard’s attacks or advanced abilities (e.g., summoning minions).
import random

# Base Character Class (Parent Class)
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        self.health = max(self.health, 0)  # Prevent negative health

    def is_alive(self):# function returns character/Villans health if greater than zero.
        return self.health > 0

    def display_status(self):# function displays character/villans name and health.
        print(f"{self.name}: Health = {self.health}")


# Weapons Attack Class for attacks and damages both characters/villain.
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
           
        
# User chooses a Hero Selection
print("Choose a character:")
print("1. Lycan Knight")
print("2. Phoenix")
print("3. Soul Reaper")
user_choice = int(input("Enter the number of your choice: "))

if user_choice == 1:# When user chooses 1
    hero = Lycan_Knight()
    
elif user_choice == 2:# When user chooses 2
    hero = Pheonix()
     
elif user_choice == 3:# When user chooses 3
    hero = Soul_Reaper()
   
else:# if user inputs a number besides 1, 2, 3. It will defaulkt to hero1.
    print("Invalid choice! Defaulting to Knight Seeker.")
    hero = Lycan_Knight()
# Evil wizzard character is iunder villain to avoid confusion.
villain = Evil_Wizard() 
# Program output name and start health of the character that the user chose.
print(f"\nYour hero: {hero.name} (Health: {hero.health})")
# Program outputs Villains name and health.
print(f"Your first battle is against: {villain.name} (Health: {villain.health})")
# using a while loop to start match of character and villan health is greater than 0 remains True.
while hero.is_alive() and villain.is_alive():
    # Hero's Turn
    print("\nHero's Turn:")
    # Shows status of both characters user picked of health and main opppnents health.
    hero.display_status()
    villain.display_status()
    # Program asks user to choose an attack from 1 - 3 different special attacks of each character.
    print("Choose an attack:")
    # for loop for attack and damage.
    for i, attack_name in enumerate(hero.attack.attack_types, start=1):
        print(f"{i}. {attack_name}")# Program outputs 1 - 3 specail attacks for character chosen by the user.
    try:# using try method if user inputs invalid number. Loses a turnwhile villan doesnt take damage
        attack_choice = int(input("Enter the number of your choice: ")) - 1 # user inputs choice.
        if 0 <= attack_choice < len(hero.attack.attack_types):# if the player chose an attack within the characters list.
            if damage < 0:  # if the damages was less than zero or is a negative, then charachter gets healed.
                hero.health = min(hero.health - damage, 100) # hero health is result of damages from villain.
                print(f"{hero.name} heals for {-damage} health!")# Prgoram prints the remainder from character and health left over.
            else:
                villain.take_damage(damage)# villains health is reduced.
        else:
            print("Invalid choice! Performing a random attack.")# if player inputs any integer other than 1, 2, 3 program out puts random character attack.
            damage = hero.attack.perform_attack()
            if damage < 0:  # if the damages was less than zero or is a negative, then charachter gets healed.
                hero.health = min(hero.health - damage, 100)# hero health is result of damages from villain.
                print(f"{hero.name} heals for {-damage} health!")# Prgoram prints the remainder from character and health left over.
            else:
                villain.take_damage(damage)# villains health is reduced.
    except ValueError:
        print("Invalid input! Performing a random attack.")
        damage = hero.attack.perform_attack()
        if damage < 0:  
            hero.health = min(hero.health - damage, 100)
            print(f"{hero.name} heals for {-damage} health!")
        else:
            villain.take_damage(damage)

    if not villain.is_alive():
        print(f"\n{villain.name} has been defeated! You win!")
        break

    # Villain's Turn
    print("\nVillain's Turn:")
    damage = villain.attack.perform_attack()# damages from list of weapons that villain has.
    hero.take_damage(damage)# Charactewrs health declines.
    if not hero.is_alive():# if villainn still has health and character's health is zero then villain wins.
        print(f"\n{hero.name} has been defeated! The villain wins!")
        break

# Final Status
print("\n--- Final Status ---")
hero.display_status()
villain.display_status()

if hero.is_alive():# if character still has health nad villain health is zero, then character wins.
    print(f"\nVictory! {hero.name} has triumphed over {villain.name}!")
else:
    print(f"\nDefeat! {villain.name} has vanquished {hero.name}!")