from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connect with data base
engine = create_engine('sqlite://///home/karin/Documents/overlap/LiteToAlchemy.db', echo = True)

# manage tables
base = declarative_base()


class tododb (base):
    __tablename__ = 'tododb'
    NoteNum = Column(Integer, primary_key = True)
    Time = Column(Integer)
    Text = Column(Text) 

    def __init__(self, NoteNum, Time, Text):
        self.NoteNum = NoteNum
        self.Time = Time
        self.Text = Text

base.metadata.create_all(engine)




##PUSH THE PROJECT TO GITHUB