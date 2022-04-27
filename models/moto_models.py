from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey
Base = declarative_base()

class MotoModel(Base):
    
    __tablename__ = "moto"

    id = Column(Integer, primary_key=True, nullable=False)
    model = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    year_of_purchase = Column(Integer, nullable=False)
    KM_ride = Column(Integer, nullable=False)
    buyer_id = Column(Integer, nullable=False) 
    
    def __repr__(self) -> str:
        return f"<Motorcycle:(id={self.id},model={self.model},price={self.price},year of purchase={self.year_of_purchase},KM of ride={self.KM_ride})> "