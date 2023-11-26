class Ork:
    def __init__(self, *, level: int) -> None:
        self.level = level


ork = Ork(level=1)
print(ork.level)  # Output: 1


class Ork:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 100 * level

    def attack(self):
        print(f"Ork attacks with {self.attack_power} power")

    def __str__(self) -> str:
        return f"Ork (level: {self.level}, hp: {self.health_points})"


ork = Ork(level=2)
print(ork.level)  # Output: 2
print(ork.health_points)  # Output: 200
print(ork.attack_power)  # Output: 200

ork.attack()  # Output: Ork attacks with 200 power

# Ork.attack()  # Output: TypeError: attack() missing 1 required positional argument: 'self'

ork.level += 1
print(ork.level)  # Output: 3
print(ork)  # Output: Ork (level: 3, hp: 300)
