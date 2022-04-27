from models.buyer_models import BuyerModel
from sqlalchemy.orm.session import Session

class BuyerDao:
    def __init__(self, session: Session):
        self.__session = session
        
    def get_all_buyers(self):
        return self.__session.query(BuyerModel).all()
    
    def get_buyers_by_id(self, id):
        return self.__session.query(BuyerModel).filter(BuyerModel.id == id)[0]
    
    def get_buyers_by_name(self, name):
        return self.__session.query(BuyerModel).filter(BuyerModel.name == name).all()
    
    def get_buyers_by_email(self, email):
        return self.__session.query(BuyerModel).filter(BuyerModel.email == email).all()
    
    def create_new_buyer(self, buyer: BuyerModel):
        self.__session.add(buyer)
        self.__session.commit()
        print("new buyer added to the database")