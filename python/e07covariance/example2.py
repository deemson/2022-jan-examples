from typing import List
from e07covariance.common import Cat, Animal, Dog

cats: List[Cat] = [Cat("Rocky"), Cat("Teddy")]


def add_a_dog(animals: List[Animal]):
    animals.append(Dog("Bolt"))


add_a_dog(cats)
print(type(cats[2]))  # Dog
