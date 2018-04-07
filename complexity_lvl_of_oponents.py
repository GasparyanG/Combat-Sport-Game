import random
import armour
import weapon
from ways_to_choose import IterationOver
import fighter
import attack_main_module
from factory import FactoryForAttackMainClass


ATTACKS = {
           "Attack to head" : "H",
           "Attack to chest" : "C",
           "Attack to feet" : "F"
          }


class AbstractionOfComplexityLvl:
	def __init__(self, implementation):
        self.implementation = implementation

    def fight(self, sides):
        raise NotImplementedError()


class ConcreteComplexityLvl(AbstractionOfComplexityLvl):
    def fight(self, sides):
        return self.implementation.execute(sides)


class InterfaceOfImplementaion:
    def __init__(self):
    	self.sides = None

    def add_oponent(self, user_fighter, oponent):
    	user_fighter.set_oponent(oponent)
    	oponent.set_oponent(user_fighter)

    def remove_oponent(self, user_fighter, oponent):	
        user_fighter.set_oponent(None)
    	oponent.set_oponent(None)

    def prompt_to_user(self):
    	prompt = ""
    	for attack_description in ATTACKS:
    		prompt += "{}: {}\n".format(attack_description, ATTACKS[attack_description])
    	return prompt

    def list_of_attacks(self):
        attack_list = []
        for attack_key in ATTACKS:
        	attack_list.append(ATTACKS[attack_key])
        return attack_list

    def end_of_battle(self, user_fighter, oponent):
        if user_fighter.health_points <= 0:
            return False
        elif oponent.health_points <= 0:
            return True           
    
    def next_properties(self, current_propertie = None):
        armour_list = armour.Armour.__subclasses__()
        weapon_list = weapon.Weapon.__subclasses__()
        
        dictoinary_of_armour_and_weapon = {} 
        for index, item in armour_list:
            dictoinary_of_armour_and_weapon[item] = weapon_list[index]
        
        dictionary_itearator = FactoryForAttackMainClass().create(dictoinary_of_armour_and_weapon, IterationOver, current_propertie)
        
        properties = dictionary_itearator.next()

        return properties

    def set_properties(self, user_fighter, dictionary):
        for item in dictionary:
        	user_fighter.set_armour(item)
        	user_fighter.set_weapon(dictionary[item])

                	 
    def is_used(self, comparable_object):
        raise NotImplementedError()

    def execute(self, sides):
        raise NotImplementedError()


class ImplementionOfArcadeGameComplexityLvl(InterfaceOfImplementaion):
    pass


class ImplementationOfFighterVsFighterComplexityLvl(InterfaceOfImplementaion):
    pass


class Easy(ImplementionOfArcadeGameComplexityLvl):
    def is_used(self, comparable_object):
        return comparable_object.upper() == "0"

    def execute(self, sides):
        self.sides = sides 
        user_fighter = self.sides[0]
        list_of_oponents = self.sides[1]
        
        cycle = 0   
        for oponent in list_of_oponents:
        	while True:
        		self.add_oponent(user_fighter, oponent)
                
                user_attack = input(self.prompt_to_user())
                
                if cycle % 3 == 0:
                	# False don't let to change fighting style 
                	oponent.attack(self.oponent_movement(), False)
                    user_fighter.attack(user_attack)
                else:
                	user_fighter.attack(user_attack)
 
                cycle += 1
               
                if self.end_of_battle(user_fighter, oponent) == False:
                    user_fighter.health_points = fighter.HEALTH_POINTS
                    oponent.health_points = fighter.HEALTH_POINTS 
                    continue	
                elif self.end_of_battle(user_fighter, oponent):
                	user_fighter.health_points = fighter.HEALTH_POINTS
                	break
            cycle = 0 
                           
            ditionary_of_next_properties = self.next_properties(user_fighter.armour)
            self.set_properties(user_fighter, ditionary_of_next_properties)


    def oponent_movement(self, user_fighter):
        if len(user_fighter.armour_properties) > 0:
            list_of_armour = []
            for fighter_armour in user_fighter.armour_properties:
                list_of_armour.append(fighter_armour.areas_to_defend)

            oponent_attack = random.choice(list_of_armour)
            return oponent_attack    
        else:
            oponent_attack = random.choice(self.list_of_attacks())
            return oponent_attack