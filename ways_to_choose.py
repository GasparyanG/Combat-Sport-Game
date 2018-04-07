# import options_to_choose
import factory
# import fighting_style

class WaysToChoose:
    def is_used(self, combarable_object):
        raise NotImplementedError()

    def execute(self, iterable):
        raise NotImplementedError()    


class Choosing(WaysToChoose):
    def is_used(self, comparable_object):
        return comparable_object == "0"

    def is_valid(self, user_choice, iterable):
        try:
            length_of_iterable = len(iterable)
            if int(user_choice) >= 0 and int(user_choice) < length_of_iterable:
                return True
        except ValueError:
            return False        
        
    def execute(self, iterable):
        info = self.representation(iterable)
        
        while True:
            user_choice = input("Choose fighting style by typing corresponding number\n{}".format(info))

            if self.is_valid(user_choice, iterable):
                chosen_fighting_style = iterable[int(user_choice)]
                return chosen_fighting_style()
            else:
                continue    

    def representation(self, iterable):
        object_representation = ""
        for index, item in enumerate(iterable):
            object_representation += "{} {}".format(index, item().__str__())

        return object_representation     
        

class IterationOver(WaysToChoose):
    def __init__(self):
        self.command_to_iterator = CommandToIterator

    def is_used(self, combarable_object):
        return combarable_object == "1"

    def execute(self, iterable):
        list_iterator = factory.Factory().create(iterable, type(self))
        while True:
            iteratoion_over_iterable = input("If you want the next fighting style type N\n"
                                             "If you want the previous fighting style type P\n"
                                             "If you want the current fighting style type C: ")
            fighting_style_with_iteration = factory.FactoryForAttackMainClass().create(iteratoion_over_iterable, self.command_to_iterator, list_iterator)
            
            if fighting_style_with_iteration == None:
                continue
            else:
                return fighting_style_with_iteration()


class CommandToIterator:
    def is_used(self, comparable_object):
        raise NotImplementedError()

    def execute(self, iterable):
        raise NotImplementedError()


class Next(CommandToIterator):
    def is_used(self, comparable_object):
        return comparable_object.upper() == "N"

    def execute(self, iterable):
        style = iterable.next()
        print(style())


class Previous(CommandToIterator):
    def is_used(self, comparable_object):
        return comparable_object.upper() == "P"

    def execute(self, iterable):
        style = iterable.previous()
        print(style())


class Current(CommandToIterator):
    def is_used(self, comparable_object):
        return comparable_object.upper() == "C"

    def execute(self, iterable):
        iterable.previous()
        return iterable.next()            


class DictionaryCreator(IterationOver):
    def __init__(self):
        self.iterable = None
        self.iterator_of_dictionary = DictionaryIterator 

    def is_used(self, iterable):
        self.iterable = iterable
        return type(iterable) == dict

    def execute(self, propertie = None):
        return self.iterator_of_dictionary(self.iterable, propertie)


class ListCreator(IterationOver):
    def __init__(self):
        self.iterable = None
        self.iterator_of_list = ListIterator

    def is_used(self, iterable):
        self.iterable = iterable
        return type(iterable) == list

    def execute(self, propertie = None):
        return self.iterator_of_list(self.iterable, propertie)


class Iterator:
    def __init__(self, iterable, propertie):
        self.iterable = iterable
        self.propertie = propertie
        self.next_index = 0

    def has_next(self):
        raise NotImplementedError()

    def next(self):
        raise NotImplementedError()    


class DictionaryIterator(Iterator):
    def next(self):
        dict_converted_to_list = self.objects_to_iterate_over()
        list_of_keys = dict_converted_to_list[0]
        list_of_values = dict_converted_to_list[1]

        # this will point to next item
        key_value = {list_of_keys[self.next_index] : list_of_values[self.next_index]}  

        self.has_next()
        return key_value

    def has_next(self):
        dict_converted_to_list = self.objects_to_iterate_over()
        list_of_keys = dict_converted_to_list[0]
        list_of_values = dict_converted_to_list[1]
        
        if self.propertie != None:
            index = list_of_keys.index(self.propertie)
            self.next_index = index + 1
        else:
            self.next_index += 1     

        if self.next_index > len(list_of_keys) - 1:
                self.next_index -= 1

    def objects_to_iterate_over(self):
        list_of_keys = []
        list_of_values = []

        for item in self.iterable:
            list_of_keys.append(item)
            list_of_values.append(self.iterable[item])

        return [list_of_keys, list_of_values]    


class ListIterator(Iterator):
    def __init__(self, iterable, propertie):
        super().__init__(iterable, propertie)
        self.interface_for_implementation = InterfaceForImplementation
        self.implementation_of_list_iterator = factory.ProductFactory().create(
            self.iterable, self.interface_for_implementation)        

    def next(self):
        return self.implementation_of_list_iterator.next_item()

    def previous(self):
        return self.implementation_of_list_iterator.previous_item()    


class InterfaceForImplementation:
    def __init__(self):
        self.iterable = None

    def is_used(self, iterable):
        raise NotImplementedError() 

    def next_item(self):
        raise NotImplementedError()

    def previous_item(self):
        raise NotImplementedError()

    def base_class_recognition(self, iterable):
        base_class_type = iterable[0]
        base_class = base_class_type.__bases__[0]
        name_of_the_base_class = base_class.__name__

        return name_of_the_base_class


class IterationOverFighters(InterfaceForImplementation):
    def __init__(self):
        super().__init__()
        self.next_index = 0    

    def is_used(self, iterable):
        self.iterable = iterable
        return self.base_class_recognition(iterable) == "Observable"

    def next_item(self):
        if self.has_next():
            return self.iterable[self.next_index]

    def has_next(self):
        if len(iterable) - 1 < self.next_index:
            self.next_index -= 1
            return True
        else:
            self.next_index += 1   
            return True


class IterationOverFightingStyles(InterfaceForImplementation):
    def __init__(self):
        super().__init__()
        self.next_index = 0
        self.previous_index = 0

    def is_used(self, iterable):
        self.iterable = iterable
        return self.base_class_recognition(iterable) == "FightingStyle"

    def next_item(self):
        if self.has_next():
            return self.iterable[self.next_index]

    def has_next(self):
        self.next_index = self.previous_index + 1
        if self.previous_index == len(self.iterable) - 2:
            self.previous_index = -1
            return True
        else:
            self.previous_index += 1    
            return True 
            
    def previous_item(self):
        if self.has_previous():
            return self.iterable[self.previous_index]

    def has_previous(self):
        self.previous_index = self.next_index - 1
        if self.next_index == 0:
            self.next_index = len(self.iterable)
            return True
        else:
            self.next_index -= 1            
            return True