from typing import List

from e07covariance.common import Animal, Cat


def animal_names(animals: List[Animal]) -> List[str]:
    return [animal.name for animal in animals]


cats: List[Cat] = [Cat("Rocky"), Cat("Teddy")]
animal_names(cats)
