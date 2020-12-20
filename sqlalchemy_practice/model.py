from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger(__name__)

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

logger = logging.getLogger(__name__)


class Number(Base):
    __tablename__ = "numbers"
    main_number = Column(Integer, primary_key=True, autoincrement=True)
    random_number = Column(Integer())


Base.metadata.create_all(engine)
SessionClass = sessionmaker(engine)
session = SessionClass()


# put Tuple in DB
def save_number(random_4number):
    t = Number(random_number=random_4number)
    session.add(t)
    session.commit()


# take out data in DB
def getDB():
    results = session.query(Number)
    list = []
    for result in results:
        list.append(result.random_number)

    d = dict(enumerate(list))
    return d
