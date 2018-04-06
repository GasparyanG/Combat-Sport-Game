class Weapon:
    def __init__(self, fighting_style):
        self.fighting_style = fighting_style
        self.name = type(self).__name__

    def attack_to_head(self):
        raise NotImplementedError()

    def attack_to_chest(self):
        raise NotImplementedError()

    def attack_to_feet(self):
        raise NotImplementedError()


class Nunchaku(Weapon):
    def attack_to_head(self):
        return self.fighting_style.attack_to_head + 8

    def attack_to_chest(self):
        return self.fighting_style.attack_to_chest + 5

    def attack_to_feet(self):
        return self.fighting_style.attack_to_feet + 3      


class Sword(Weapon):
    def attack_to_head(self):
        return self.fighting_style.attack_to_head + 11

    def attack_to_chest(self):
        return self.fighting_style.attack_to_chest + 8

    def attack_to_feet(self):
        return self.fighting_style.attack_to_feet + 6


class BattleAxe(Weapon):
    def attack_to_head(self):
        return self.fighting_style.attack_to_head + 15

    def attack_to_chest(self):
        return self.fighting_style.attack_to_chest + 12

    def attack_to_feet(self):
        return self.fighting_style.attack_to_feet + 8