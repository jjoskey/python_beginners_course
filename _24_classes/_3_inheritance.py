# class Ork:
#     def __init__(self, *, level: int) -> None:
#         self.level = level
#         self.health_points = 100 * level
#         self.attack_power = 10 * level
#
#     def attack(self):
#         print(f"Ork attacks with {self.attack_power} power")
#
#     def __str__(self) -> str:
#         return f"Ork (level: {self.level}, hp: {self.health_points})"
#
#
# class Elf:
#     def __init__(self, *, level: int) -> None:
#         self.level = level
#         self.hp = 50 * level
#         self.attack_power = 15 * level
#
#     def attack(self):
#         print(f"Elf attacks with {self.attack_power} power")
#
#     def __str__(self) -> str:
#         return f"Elf (level: {self.level}, hp: {self.hp})"


class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def __str__(self) -> str:
        return f"{self.character_name} (name: {self.name}, level: {self.level}, hp: {self.health_points})"

    def attack(self):
        print(f"{self.character_name} attacks with {self.attack_power} power")


class Ork(Character):
    character_name = "Ork"
    base_health_points = 100
    base_attack_power = 10


ork_1 = Ork(level=1)
print(ork_1.attack())  # Output: Ork attacks with 10 power
print(ork_1)  # Output: Ork (level: 1, hp: 100)


class Elf(Character):
    character_name = "Elf"
    base_health_points = 70
    base_attack_power = 15

    def attack(self):
        print("This method is from class-inheritor")


elf_1 = Elf(level=1)
print(elf_1.attack())  # Output: This method is from class-inheritor


class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def __str__(self) -> str:
        return f"{self.character_name} (level: {self.level}, hp: {self.health_points})"

    def attack(self, *, target: "Character") -> None:
        print(
            f"{self.character_name} attacks {target.character_name} ({target.health_points} health_points) "
            f"with {self.attack_power} power."
        )
        target.health_points -= self.attack_power
        print(f"After attack {target.character_name} hp has {target.health_points}")

    def is_alive(self) -> bool:
        return self.health_points > 0


class Ork(Character):
    character_name = "Ork"
    base_health_points = 100
    base_attack_power = 10


class Elf(Character):
    character_name = "Elf"
    base_health_points = 70
    base_attack_power = 15


def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)

    print(f"Character 1: {character_1}, is alive: {character_1.is_alive()}")
    print(f"Character 2: {character_2}, is alive: {character_2.is_alive()}")


ork = Ork(level=1)
elf = Elf(level=1)
fight(character_1=ork, character_2=elf)
