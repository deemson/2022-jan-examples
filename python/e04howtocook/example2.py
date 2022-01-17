from typing import Generic, TypeVar

T1 = TypeVar("T1")
T2 = TypeVar("T2")


# If generic types are used in __init__ Python is able to "auto-detect" them
class MyGenericClass(Generic[T1, T2]):
    def __init__(self, value1: T1, value2: T2):
        self.value1, self.value2 = value1, value2

    def check_if_equal(self, value1: T1, value2: T2):
        return self.value1 == value1 and self.value2 == value2


MyGenericClass("hello", 42).check_if_equal(42, "hello")
