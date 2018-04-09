from factory import Factory, FactoryForAttackMainClass
from complexity_lvl_of_oponents import ImplementationOfFighterVsFighterComplexityLvl, ImplementionOfArcadeGameComplexityLvl
import fighter_to_play_with
import options_to_choose
import programm_made_fighters


class FightingGames:
    def create_fighter(self):
        while True:
            choice = options_to_choose.OptionsToChoose().offering_options(fighter_to_play_with.FighterToPlayWith)

            fighter = Factory().create(choice, fighter_to_play_with.FighterToPlayWith)

            if choice == None:
                continue
            else:
                return fighter

    def cxlvl_choice(self, base_class, sides):
        while True:
            user_choice = options_to_choose.OptionsToChoose().offering_options(base_class)

            cxlvl = FactoryForAttackMainClass().create(user_choice, base_class, sides)

            if cxlvl == True:
                print("You win the game!")
                break
            else:
                print("You lost!")
                break


    def is_used(self, comparable_object):
        raise NotImplementedError()

    def execute(self):
        raise NotImplementedError()


class ArcadeGame(FightingGames):
    def __init__(self):
        self.arcade_game_cxlvl = ImplementionOfArcadeGameComplexityLvl

    def is_used(self, comparable_object):
        return comparable_object == "0"

    def execute(self):
        self.create_fighter()

        list_of_oponents = programm_made_fighters.Oponents().create_oponents()
        
        sides = [user_fighter, list_of_oponents]

        print("Coplexity lvl of game")
        
        self.cxlvl_choice(self.arcade_game_cxlvl, sides)


class FighterVsFighterGame(FightingGames):
    def __init__(self):
        self.oponent_cxlvl = ImplementationOfFighterVsFighterComplexityLvl

    def is_used(self, comparable_object):
        return comparable_object == "1"

    def execute(self):
        sides = []

        for times in range(2):
            fighter = self.create_fighter()
            sides.append(fighter) 

        print("Oponent Complexity lvl")
        
        self.cxlvl_choice(self.oponent_cxlvl, sides)


user_choice = options_to_choose.OptionsToChoose().offering_options(FightingGames)

Factory().create(user_choice, FightingGames)