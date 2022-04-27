from models.moto_models import MotoModel
from sqlalchemy.orm.session import Session


class MotoDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_moto(self):
        return self.__session.query(MotoModel).all()

    def get_moto_by_id(self, id):
        return self.__session.query(MotoModel).filter(MotoModel.id == id)[0]

    def get_moto_by_model(self, model):
        return self.__session.query(MotoModel).filter(MotoModel.model == model).all()
    
    def get_moto_by_price(self, price):
        return self.__session.query(MotoModel).filter(MotoModel.price == price).all()
    
    def get_moto_by_year_of_year_of_purchase(self, year_of_purchase):
        return self.__session.query(MotoModel).filter(MotoModel.year_of_purchase == year_of_purchase).all()
    
    def get_moto_by_KM_ride(self, KM_ride):
        return self.__session.query(MotoModel).filter(MotoModel.KM_ride == KM_ride).all()
    
    def get_moto_by_buyer_id(self, buyer_id):
        return self.__session.query(MotoModel).filter(MotoModel.buyer_id == buyer_id).all()
    
    def create_new_moto(self, moto: MotoModel):
        self.__session.add(moto)
        self.__session.commit()
        print("new motorcycle added to the database")