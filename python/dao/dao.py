from typing import TypeVar, Type, Generic, Optional
from sqlalchemy.orm import Session
from dao.models import Model

ModelT = TypeVar("ModelT", bound=Model)



class DataAccessObject(Generic[ModelT]):
    def __init__(self, model_class: Type[ModelT]):
        self.model_class = model_class

    def create(self, session: Session, model: ModelT):
        if not isinstance(model, self.model_class):
            raise TypeError(f"{type(model)} is not an instance of {self.model_class.__name__}")
        session.add(model)
        session.commit()

    def read(self, session: Session, model_id: int) -> Optional[ModelT]:
        return session.query(self.model_class).get(model_id)

    def delete(self, session: Session, model_id: int):
        session.delete(session.query(self.model_class).get(model_id))
        session.commit()
