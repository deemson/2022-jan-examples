class Animal:
    def do_animal_thing(self):
        ...


class Cat(Animal):
    def do_animal_thing(self):
        print("doing a cat thing")


class Dog(Animal):
    def do_animal_thing(self):
        print("doing a dog thing")


def not_a_generic_function(animal: Animal):
    animal.do_animal_thing()


not_a_generic_function(Cat())
not_a_generic_function(Dog())
