class FightingStyle:
    def __init__(self):
        self.name = type(self).__name__

    def attack_to_head(self):
        raise NotImplementedError()

    def attack_to_chest(self):
        raise NotImplementedError()

    def attack_to_feet(self):
        raise NotImplementedError()

    def __str__(self):
        prompt_about_attacks = ["Attack to head", "Attack to chest", "Attack to feet"]
        prompt_about_injury = [self.attack_to_head(), self.attack_to_chest(), self.attack_to_feet()] 

        information_about_fighting_style = "{}\n".format(self.name)
        information_about_fighting_style += "Attacks to metioned areas have corresponding injuries\n"
        
        for index, prompt in enumerate(prompt_about_attacks):
               information_about_fighting_style += "{}: {}\n".format(prompt, prompt_about_injury[index])
        return information_about_fighting_style


class KungFu(FightingStyle):
    def attack_to_head(self):
        return 35

    def attack_to_chest(self):
        return 25

    def attack_to_feet(self):
        return 20       


class KickBox(FightingStyle):
    def attack_to_head(self):
        return 25

    def attack_to_chest(self):
        return 20

    def attack_to_feet(self):
        return 15

         
class Karate(FightingStyle):
    def attack_to_head(self):
        return 20

    def attack_to_chest(self):
        return 15

    def attack_to_feet(self):
        return 10