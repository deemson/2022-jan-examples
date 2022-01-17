from typing import Generic, TypeVar, List

from e09covariance.common import Animal, Cat, Dog

T = TypeVar("T", bound=Animal)


def animal_names(animals: List[T]) -> List[str]:
    return [animal.name for animal in animals]


cats: List[Cat] = [Cat("Rocky"), Cat("Teddy")]
animal_names(cats)
