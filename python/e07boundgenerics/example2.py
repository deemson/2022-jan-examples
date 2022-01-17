class User:
    @classmethod
    def deserialize(cls) -> "User":
        return cls()

    def do_a_user_thing(self):
        print("doing a user thing")


user = User.deserialize()
user.do_a_user_thing()


class Product:
    @classmethod
    def deserialize(cls) -> "Product":
        return cls()

    def do_a_product_thing(self):
        print("doing a product thing")


product = Product.deserialize()
product.do_a_product_thing()
