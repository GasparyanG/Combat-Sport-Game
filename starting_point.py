import options_to_choose
import factory
import fighting_game_types


def start_game():
    while True:
        user_choice = options_to_choose.OptionsToChoose().offering_options(fighting_game_types.FightingGames)
        game = factory.Factory().create(user_choice, fighting_game_types.FightingGames)
         
        if game == None:
        	continue
        elif game == False:
            print("Goodby!")
            break 

start_game()