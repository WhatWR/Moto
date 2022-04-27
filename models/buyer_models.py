from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class BuyerModel(Base):
    __tablename__ = "buyer"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    
    def __repr__(self) -> str:
        return f"<Buyer : (id={self.id} name={self.name} email={self.email})>"
    