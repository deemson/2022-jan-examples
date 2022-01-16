from typing import Type, TypeVar, Generic

T = TypeVar("T")


class Query(Generic[T]):
    def __init__(self, obj: T):
        self.obj = obj

    def get(self, obj_id: int) -> T:
        return self.obj


def query_factory(klass: Type[T]) -> Query[T]:
    return Query(klass())


class User:
    def do_a_user_thing(self):
        print("doing a user thing")


class Product:
    def do_a_product_thing(self):
        print("doing a product thing")


def user_endpoint(user_id: int):
    user_query = query_factory(User)
    user = user_query.get(user_id)
    user.do_a_user_thing()


def product_endpoint(product_id: int):
    product_query = query_factory(Product)
    product = product_query.get(product_id)
    product.do_a_product_thing()


def get_object_by_id(klass: Type[T], object_id: int) -> T:
    query = query_factory(klass)
    return query.get(object_id)


def user_endpoint_refactored(user_id: int):
    user = get_object_by_id(User, user_id)
    user.do_a_user_thing()


def product_endpoint_refactored(product_id: int):
    product = get_object_by_id(Product, product_id)
    product.do_a_product_thing()
