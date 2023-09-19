class Ork:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 10 * level

    def attack(self):
        print(f"Ork attacks with {self.attack_power} power")

    def __str__(self) -> str:
        return f"Ork (level: {self.level}, hp: {self.health_points})"


ork = Ork(level=1)
print(ork.level)
print(ork.health_points)
print(ork.attack_power)
ork.attack()
# Ork.attack()  # This will raise an error

ork.level += 1
ork.health_points += 100
print(ork)
