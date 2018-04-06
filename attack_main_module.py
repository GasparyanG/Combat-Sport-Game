class AttackMainClass:
    def is_used(self, comparable_object):
        raise NotImplementedError()

    def execution(self, fighting_style):
        raise NotImplementedError()


class AttackToHead(AttackMainClass):
    def is_used(self, comparable_object):
        return comparable_object.upper() == "H"

    def execution(self, fighting_style):
        return fighting_style.attack_to_head()


class AttackToChest(AttackMainClass):
    def is_used(self, comparable_object):
        return comparable_object.upper() == "C"

    def execution(self, fighting_style):
        return fighting_style.attack_to_chest()


class AttackToFeet(AttackMainClass):
    def is_used(self, comparable_object):
        return comparable_object.upper() == "F"

    def execution(self, fighting_style):
        return fighting_style.attack_to_feet()