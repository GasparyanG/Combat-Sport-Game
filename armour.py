class Armour:
    def defense(self):
        raise NotImplementedError()

    def __str__(self):
        representation = type(self).__name__
        representation += "ability of defense is"
        representation += "{}".format(self.defense())
        

class Helmet(Armour):
    def __init__(self):
        self.areas_to_defend = "H"

    def defense(self):
        return 5
    

class Shield(Armour):
    def __init__(self):
        self.areas_to_defend = "C"

    def defense(self):
        return 7


class ArmourBoot(Armour):
    def __init__(self):
        self.areas_to_defend = "F"

    def defense(self):
        return 10