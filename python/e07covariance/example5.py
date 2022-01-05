from typing import Generic, TypeVar

from e07covariance.common import Animal, Cat, Dog

T = TypeVar("T", covariant=True)


class Pen(Generic[T]):
    def __init__(self, animal: T):
        self._animal = animal

    def get(self) -> T:
        return self._animal


def show_who_is_in_the_pen(pen: Pen[Animal]):
    animal = pen.get()
    print(f"we have a {animal.__class__.__name__} called '{animal.name}'")


cat_pen = Pen(Cat("Fluffy"))
dog_pen = Pen(Dog("Bolt"))
show_who_is_in_the_pen(cat_pen)
show_who_is_in_the_pen(dog_pen)
