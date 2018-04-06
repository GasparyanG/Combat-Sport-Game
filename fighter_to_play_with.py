import fighter
import ways_to_choose
import fighting_style
import factory
import options_to_choose
import programm_made_fighters


class FighterToPlayWith:
    def is_used(self, comparable_object):
        raise NotImplementedError()

    def execute(self):
        raise NotImplementedError()     


class CostumeMadeFighter(FighterToPlayWith):
    def is_used(self, comparable_object):
        return comparable_object == "0"

    def execute(self):
        name = input("Give a name to this fighter: ")

        while True:
            choice_type = ways_to_choose.WaysToChoose

            print("How do you want to choose  fighting style.")
            user_choice = options_to_choose.OptionsToChoose().offering_options(choice_type)

            subclasses = self.fighting_style_type_classes()
            fighting_style_of_user_choice = factory.FactoryForAttackMainClass().create(user_choice, choice_type, subclasses)
            print(fighting_style_of_user_choice)
            costume_fighter = fighter.Fighter(name, fighting_style_of_user_choice)
            return costume_fighter

    def fighting_style_type_classes(self):
        base_calss = fighting_style.FightingStyle

        subclasses = base_calss.__subclasses__()

        return subclasses        


class ExistingFighterChoice(FighterToPlayWith):
    def __init__(self):
        self.programm_made_fighters = programm_made_fighters.ProgrammMadeFighters()

    def is_used(self, comparable_object):
        return comparable_object == "1"

    def execute(self):
        list_of_fighters = self.programm_made_fighters.create_fighters()
        info_about_fighters = self.representation_of_fighters()

        while True:
            user_choice = input("Choose fighter by typing correponding number\n{}".format(info_about_fighters))

            if self.is_valid(user_choice, list_of_fighters):
                return list_of_fighters[int(user_choice)]
            else:
                print("Please don't violate the requirements!")
                continue     

    def representation_of_fighters(self):
        list_of_fighters = self.programm_made_fighters.create_fighters()
        
        representation = ""
        for index, regular_fighter in enumerate(list_of_fighters):
            representation += "{} {}\n".format(index, regular_fighter.__str__())

        return representation   

    def is_valid(self, user_choice, list_of_fighters):
        try:
            length_of_list = len(list_of_fighters)
            if int(user_choice) >= 0 and int(user_choice) < length_of_list:
                return True
        except ValueError:
            return False 


user_choice = options_to_choose.OptionsToChoose().offering_options(FighterToPlayWith)

print(factory.Factory().create(user_choice, FighterToPlayWith))            