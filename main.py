from hereos import Lycan_Knight, Pheonix, Soul_Reaper# This imports classes from hereos.py
from villain import Evil_Wizard # This imports class from villain.py

# User chooses a Hero Selection
print("Choose a character:")
print("1. Lycan Knight")
print("2. Pheonix")
print("3. Soul Reaper")
user_choice = int(input("Enter the number of your choice: "))
if user_choice == 1:
    hero = Lycan_Knight()
elif user_choice == 2:
    hero = Pheonix()
elif user_choice == 3:
    hero = Soul_Reaper()
else:
    print("Invalid choice! Defaulting to Lycan Knight.")
    hero = Lycan_Knight()

villain = Evil_Wizard()

print(f"\nYour hero: {hero.name} (Health: {hero.health})")
print(f"Your first battle is against: {villain.name} (Health: {villain.health})")

# Battle Loop
while hero.is_alive() and villain.is_alive():
    # Hero's Turn
    print("\nHero's Turn:")
    hero.display_status()
    villain.display_status()

    print("Choose an attack:")
    for i, attack_name in enumerate(hero.attack.attack_types, start=1):
        print(f"{i}. {attack_name}")

    try:
        attack_choice = int(input("Enter the number of your choice: ")) - 1
        if 0 <= attack_choice < len(hero.attack.attack_types):
            damage = hero.attack.damage_values[attack_choice]
            if damage < 0:
                hero.health = min(hero.health - damage, 100)
                print(f"{hero.name} heals for {-damage} health!")
            else:
                villain.take_damage(damage)
        else:
            print("Invalid choice! Performing a random attack.")
            damage = hero.attack.perform_attack()
            if damage < 0:
                hero.health = min(hero.health - damage, 100)
                print(f"{hero.name} heals for {-damage} health!")
            else:
                villain.take_damage(damage)
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
    damage = villain.attack.perform_attack()
    hero.take_damage(damage)
    if not hero.is_alive():
        print(f"\n{hero.name} has been defeated! The villain wins!")
        break

# Final Status
print("\n--- Final Status ---")
hero.display_status()
villain.display_status()
if hero.is_alive():
    print(f"\nVictory! {hero.name} has triumphed over {villain.name}!")
else:
    print(f"\nDefeat! {villain.name} has vanquished {hero.name}!")
                                