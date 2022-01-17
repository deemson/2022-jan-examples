from typing import TypeVar, Generic
from e09covariance.common import Animal, Cat, Dog

InvariantT = TypeVar("InvariantT")


class InvariantPen(Generic[InvariantT]):
    def __init__(self, animal: InvariantT):
        self._animal = animal

    def get(self) -> InvariantT:
        return self._animal

    def put(self, animal: InvariantT):
        self._animal = animal


# InvariantPen[Cat] is not an instance of InvariantPen[Animal] because we can put a dog there

BoundT = TypeVar("BoundT", bound=Animal)


class BoundPen(Generic[BoundT]):
    def __init__(self, animal: BoundT):
        self._animal = animal

    def get(self) -> BoundT:
        print(f"you're getting a '{self._animal.__class__.__name__}' named '{self._animal.name}'")
        return self._animal

    def put(self, animal: BoundT):
        print(f"you're putting a '{animal.__class__.__name__}' named '{animal.name}'")
        self._animal = animal


# BoundPen[Cat] is still not an instance of BoundPen[Animal] because we can put a dog there
# But we can use animal attributes in get or put because we know that it's definitely an animal in the pen

CovariantT = TypeVar("CovariantT")


class CovariantPen(Generic[CovariantT]):
    def __init__(self, animal: CovariantT):
        self._animal = animal

    def get(self) -> CovariantT:
        return self._animal


# Now CovariantPen[Cat] IS an instance of CovariantPen[Animal]
# But we cannot add a put method to the Pen


BoundCovariantT = TypeVar("BoundCovariantT", bound=Animal)


class BoundCovariantPen(Generic[BoundCovariantT]):
    def __init__(self, animal: BoundCovariantT):
        self._animal = animal

    def get(self) -> BoundCovariantT:
        print(f"you're getting a '{self._animal.__class__.__name__}' named '{self._animal.name}'")
        return self._animal

# BoundCovariantPen[Cat] IS an instance of BoundCovariantPen[Animal]
# We can use animal attributes in get because we know that it's definitely an animal in the pen
