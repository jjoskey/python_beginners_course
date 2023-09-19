class Character:
    max_defence = 100

    def __init__(self, *, level: int) -> None:
        self._level = level
        self._health_points = self.max_health_points

    def __str__(self) -> str:
        return f"{self.character_name} (level: {self._level}, hp: {self.health_points})"

    def attack(self, *, target: "Character") -> None:
        target.got_damage(damage=self.attack_power)

    def is_alive(self) -> bool:
        return self._health_points > 0

    def got_damage(self, damage: int) -> None:
        damage = damage * (1 - self.defence_coefficient)
        damage = round(damage)
        self._health_points = self.health_points - damage

    @property
    def health_points(self) -> int:
        if self._health_points < 0:
            self._health_points = 0
        elif self._health_points > self.max_health_points:
            self._health_points = self.max_health_points
        return self._health_points

    @property
    def max_health_points(self) -> int:
        return self.base_health_points * self._level

    @property
    def attack_power(self) -> int:
        return self.base_attack_power * self._level

    @property
    def defence_coefficient(self) -> float:
        defence = self.base_defence * self._level
        if defence > self.max_defence:
            defence = self.max_defence
        return defence / self.max_defence

    @property
    def health_points_percent(self):
        return 100 * self._health_points / self.max_health_points


class Ork(Character):
    character_name = "Ork"
    base_health_points = 100
    base_attack_power = 10
    base_defence = 10

    @property
    def defence_coefficient(self) -> float:
        defence = self.base_defence * self._level
        if self._health_points < 50:
            defence *= 3
        if defence > self.max_defence:
            defence = self.max_defence

        return defence / self.max_defence


class Elf(Character):
    character_name = "Elf"
    base_health_points = 70
    base_attack_power = 15
    base_defence = 7

    def attack(self, *, target: "Character") -> None:
        attack_power = self.attack_power
        if target.health_points_percent < 30:
            attack_power *= 2
        target.got_damage(damage=attack_power)


ork = Ork(level=1)
elf = Elf(level=1)


def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)

    print(f"{character_1.character_name} is {'alive' if character_1.is_alive() else 'dead'}")
    print(f"{character_1}")
    print(f"{character_2.character_name} is {'alive' if character_2.is_alive() else 'dead'}")
    print(f"{character_2}")


fight(character_1=ork, character_2=elf)
