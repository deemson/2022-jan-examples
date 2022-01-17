from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

from e8dao.dao import DataAccessObject
from e8dao.models import Model, User, Product


class MockModel(Model):
    __tablename__ = "mock_models"

    field1 = Column(String)
    field2 = Column(Integer)


class TestDAO:
    def setup_method(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        self.Session = sessionmaker()
        self.Session.configure(bind=self.engine)

    def test_mock_model(self):
        MockModel.__table__.create(bind=self.engine)
        dao = DataAccessObject(MockModel)

        m1 = MockModel(field1="hello", field2=42)
        session = self.Session()
        dao.create(session, m1)
        m2 = dao.read(session, m1.id)
        assert m1.id == m2.id
        assert m1.field1 == m2.field1
        assert m1.field2 == m2.field2

        session = self.Session()
        dao.delete(session, m2.id)
        assert dao.read(session, m1.id) is None

    def test_user(self):
        User.__table__.create(bind=self.engine)
        dao = DataAccessObject(User)

        u1 = User(first_name="Joe", last_name="Doe")
        session = self.Session()
        dao.create(session, u1)
        u2 = dao.read(session, u1.id)
        assert u1.first_name == u2.first_name
        assert u1.last_name == u2.last_name

        session = self.Session()
        dao.delete(session, u2.id)
        assert dao.read(session, u2.id) is None

    def test_product(self):
        Product.__table__.create(bind=self.engine)
        dao = DataAccessObject(Product)

        p1 = Product(title="iPhone", price=999.99)
        session = self.Session()
        dao.create(session, p1)
        p2 = dao.read(session, p1.id)
        assert p1.title == p2.title
        assert p1.price == p2.price

        session = self.Session()
        dao.delete(session, p2.id)
        assert dao.read(session, p2.id) is None
