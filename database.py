from sqlalchemy import create_engine, Column, Integer, String, DateTime, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.orm import sessionmaker, relationship
import uuid

#TODO Make this configurable through conf file/command line arg
info = 'sqlite:///montecarlo.db'

Base = declarative_base()


class PricePoint(Base):
    """Price Point table definition. 
        Columns:
            id          -TEXT
            code        -TEXT
            exchange    -TEXT
            market      -TEXT
            price       -TEXT
            time        -DATETIME(sqlite text)"""
    
    
    __tablename__ = "PricePoint"
    
    id       = Column('id', TEXT,  primary_key=True)
    code     = Column('code', TEXT)   
    exchange = Column('exchange', TEXT)
    market   = Column('market', TEXT)
    price    = Column('price', TEXT)
    time     = Column('time', DATETIME)

    def __init__(self, code, exchange, price, time, market):
        self.id = str(uuid.uuid1())
        self.exchange = exchange
        self.price = price
        self.time = time
        self.code = code
        self.market = market
    
    def __repr__(self):
        return f"PricePoint(id:{self.id}, exchange:{self.exchange}, price:{self.price}, time:{self.time}, code:{self.code})"


class Ranking(Base):
    """Ranking table definition. 
        Columns:
            id          -TEXT
            code        -TEXT
            exchange    -TEXT
            market      -TEXT"""
    __tablename__ = "Ranking"

    id       = Column('id', TEXT, primary_key=True)
    rank     = Column('rank', TEXT)
    exchange = Column('exchange', TEXT)
    market   = Column('market', TEXT)
    code     = Column('code', TEXT)

    def __init__(self, code, exchange, rank):
        self.id = str(uuid.uuid1())
        self.exchange = exchange
        self.code = code
        self.rank = rank
        self.market = self.code.split(':')[1]

    def __repr__(self):
        return f"Ranking(id:{self.id}, rank:{self.rank}, exchange: {self.exchange}, code: {self.code}, market:{self.market}"
