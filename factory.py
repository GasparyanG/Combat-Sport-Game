class PointerToFactoryProducts:
    def pointer_to_subclasses(self, base_class):
        list_of_subclasses = base_class.__subclasses__()
        return list_of_subclasses


class Factory(PointerToFactoryProducts):
    def create(self, comparable_object, base_class):
        list_of_subclasses = self.pointer_to_subclasses(base_class)
        for subclass in list_of_subclasses:
            base_class_type_object = subclass()
            if base_class_type_object.is_used(comparable_object):
                return base_class_type_object.execute()

        
class FactoryForAttackMainClass(PointerToFactoryProducts):
    def create(self, comparable_object, base_class, fighting_style):
        print(comparable_object)
        list_of_subclasses = self.pointer_to_subclasses(base_class)
        for subclass in list_of_subclasses:
            base_class_type_object = subclass()
            if base_class_type_object.is_used(comparable_object):
                return base_class_type_object.execute(fighting_style)


class ProductFactory(PointerToFactoryProducts):
    def create(self, comparable_object, base_class):
        list_of_subclasses = self.pointer_to_subclasses(base_class)
        for subclass in list_of_subclasses:
            base_class_type_object = subclass()
            if base_class_type_object.is_used(comparable_object):
                return base_class_type_object                               