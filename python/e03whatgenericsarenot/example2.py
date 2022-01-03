from typing import TypeVar, Generic


class User:
    def do_a_user_thing(self):
        print("doing a user thing")


class Product:
    def do_a_product_thing(self):
        print("doing a product thing")


T = TypeVar("T")


class Repository(Generic[T]):
    def get_entity_from_somewhere(self) -> T:
        # assuming we obtain both users and products with very similar code
        ...


def user_endpoint():
    # we obtain repository for users specifically
    repository = Repository[User]()
    # that's why we can be sure our entity is a user
    user = repository.get_entity_from_somewhere()
    # and it's safe to call this method
    user.do_a_user_thing()


def product_endpoint():
    # we obtain repository for products specifically
    repository = Repository[Product]()
    # that's why we can be sure our entity is a product
    product = repository.get_entity_from_somewhere()
    # and it's safe to call this method
    product.do_a_product_thing()
