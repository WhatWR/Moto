from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.buyer_dao import BuyerDao
from utils.dao.moto_dao import MotoDao

class Moto:
    def __init__(self, connection_url="sqlite:///moto.db"):
        engine = create_engine(connection_url)
        session = sessionmaker(bind=engine)
        self.__db_session = session()
        
    def buyer(self):
        return BuyerDao(self.__db_session)
    
    def moto(self):
        return MotoDao(self.__db_session)