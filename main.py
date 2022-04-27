from utils.moto import Moto
from models.buyer_models import BuyerModel
from models.moto_models import MotoModel

moto = Moto()



print(moto.buyer().get_all_buyers())
print(moto.buyer().get_buyers_by_id(1))
print(moto.buyer().get_buyers_by_name("Abigail"))
print(moto.buyer().get_buyers_by_email("jollyCory53@sbcglobal.net"))
new_buyer = BuyerModel(id = 200, name="prem", email="qwer@gmail.com")
moto.buyer().create_new_buyer(new_buyer)

print(moto.moto().get_moto_by_id(101))
print(moto.moto().get_moto_by_model("Royal Enfield Classic 350"))
print(moto.moto().get_moto_by_price(45000))
print(moto.moto().get_moto_by_year_of_year_of_purchase(2017))
print(moto.moto().get_moto_by_KM_ride(350))
print(moto.moto().get_moto_by_buyer_id(5))

new_moto = MotoModel(id=500, model="honda x10", price=10000, year_of_purchase=2022, KM_ride="0", buyer_id=1000)
moto.moto().create_new_moto(new_moto)
    
    
    

