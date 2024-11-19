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