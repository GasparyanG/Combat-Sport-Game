import fighter
import random
import fighting_style

class ProgrammMadeFighters:
    def create_fighters(self):
        list_of_fighters_name = [
                   "Goro", "Quan Chi", "Scorpion",
                   "Ermac", "Sub-Zero", "Nub"
                                ]

        list_of_fighters = []
        for name in list_of_fighters_name:
            list_of_fighters.append(fighter.Fighter(name, self.fighting_style_generator()))

        return list_of_fighters                            

    def fighting_style_generator(self):
        subclasses_of_fighting_style = fighting_style.FightingStyle.__subclasses__()                            
        
        random_fighting_style = random.choice(subclasses_of_fighting_style)

        return random_fighting_style()