from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Page(Base):
    """ The SQLAlchemy declarative model class for a Page object. """
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    data = Column(Text)

    def __init__(self, name, data):
        self.name = name
        self.data = data


# Index('my_index', Page.name, unique=True, mysql_length=255)
