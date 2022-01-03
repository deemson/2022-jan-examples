# step 1: imports
from typing import Generic, TypeVar

# step 2: define generic types to be specified later
T1 = TypeVar("T1")
T2 = TypeVar("T2")


# step 3: define generic class
class MyGenericClass(Generic[T1, T2]):
    def do_something(self, value1: T1, value2: T2):
        print(f"doing something with {value1} and {value2}")


# step 4: specify generic types and use the class!
o = MyGenericClass[str, int]()
# will print "doing something with hello and 42"
o.do_something("hello", 42)
# will print "doing something with 42 and hello" but type checker will fail: your code is safe with type checker
o.do_something(42, "hello")
