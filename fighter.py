import factory
import attack_main_module
import options_to_choose
import ways_to_choose

HEALTH_POINTS = 200

class Observable:
    def __init__(self):
        self.oponent = None

    def set_oponent(self, oponent):
        self.oponent = oponent


class Fighter(Observable):
    # Passed in atributes will be of their types not objects 
    def __init__(self, name, fighting_style, armour = None, weapon = None):
        super().__init__()
        self.name = name
        self.fighting_style = fighting_style
        self.armour = armour
        self.weapon = weapon
        self.health_points = HEALTH_POINTS

        self.armour_properties = []
        if self.armour != None:
            self.armour_properties.append(self.armour)
        
    def attack(self, movement, fighting_style_state = True):
        fighting_style = None
        if weapon == None:
            fighting_style = self.fighting_style 
        else:
            fighting_style = self.weapon(self.fighting_style)

        injury = factory.FactoryForAttackMainClass().create(
            movement, attack_main_module.AttackMainClass, fighting_style)
        
        if len(self.armour_properties) > 0:
            for armour in self.armour_properties:
                if movement == self.oponent.armour().areas_to_defend:
                    after_defese = armour().defense()
                    injury = injury - after_defese 
        
        self.update(injury)

        if fighting_style_state:
            self.set_fighting_style()     
    
    def set_fighting_style(self):
        while True:
            user_decision = input(options_to_choose.OptionsToChoose().
                offering_options(ways_to_choose.WaysToChoose))
            
            subclasses = self.fighting_style_type_classes()

            fighting_style = factory.FactoryForAttackMainClass().create(user_choice, ways_to_choose.WaysToChoose, subclasses)

            if fighting_style != None:
                self.fighting_style = fighting_style
            else:
                continue    

    def fighting_style_type_classes(self):
        tuple_of_bases = type(self.fighting_style).__bases__
        base_calss = tuple_of_bases[0]

        subclasses = base_calss.__subclasses__()

        return subclasses

    def update(self, injury):
        self.oponent.health_points = self.oponent.health_points - injury

        print("Health points of {} is {}".format(self.oponent.name, self.oponent.health_points))

    def __str__(self):
        representation = "{}\n".format(self.name)
        representation += "{}\n".format(self.fighting_style.__str__())
        return representation
