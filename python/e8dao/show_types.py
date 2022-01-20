from sqlalchemy.orm import Session
from e8dao.dao import DataAccessObject
from e8dao.test_dao import MockModel

dao = DataAccessObject(MockModel)
m = dao.read(Session(), 1)
# Will be catched by type checker
m.non_existent_field