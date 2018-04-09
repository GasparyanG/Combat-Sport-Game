import armour
import weapon
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


class Oponents(ProgrammMadeFighters):
    def create_oponents(self):
        list_of_awesome_fighters = []

        list_of_regular_fighters = self.create_fighters()
        for index, regular_fighter in enumerate(list_of_regular_fighters):
            if index < len(list_of_regular_fighters) / 2:
                regular_fighter.set_armour(self.armour_generator())
                regular_fighter.set_weapon(self.weapon_genrator())
            else:
                armour_list = armour.Armour.__subclasses__()
                
                for every_armour in armour_list:
                    regular_fighter.set_armour(every_armour) 
            
            list_of_awesome_fighters.append(regular_fighter)

        return list_of_awesome_fighters    
                

    def armour_generator(self):
        armour_list = armour.Armour.__subclasses__()
        random_armour = random.choice(armour_list)
        return random_armour 
        
    def weapon_genrator(self):
        weapon_list = weapon.Weapon.__subclasses__()
        random_weapon = random.choice(weapon_list)
        return random_weapon  