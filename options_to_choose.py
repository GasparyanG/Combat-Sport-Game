class OptionsToChoose:
    def offering_options(self, base_class):
        representation = self.options_representation(base_class)
        user_choice = input("Choose option by typing corresponding number\n{}".format(representation))
        return user_choice

    def options_representation(self, base_class):
        list_of_options = base_class.__subclasses__()
        
        representation = ""
        for index, option in enumerate(list_of_options):
            representation += "{}: {}\n".format(index, option.__name__)
        
        return representation 