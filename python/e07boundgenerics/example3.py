from typing import TypeVar, Generic, Type

T = TypeVar("T", bound="Deserializable")


class Deserializable(Generic[T]):
    @classmethod
    def deserialize(cls: Type[T]) -> T:
        return cls()


class User(Deserializable["User"]):
    def do_a_user_thing(self):
        print("doing a user thing")


class Product(Deserializable["Product"]):
    def do_a_product_thing(self):
        print("doing a product thing")


user = User.deserialize()
user.do_a_user_thing()
product = Product.deserialize()
product.do_a_product_thing()
