#Nickolaydan qolgan class
# class Mashina:
#     def __init__(self, rang, model, tezlik):
#         self.rang = rang
#         self.model = model
#         self.tezlik = tezlik
#
# class Avtobus:
#     def __init__(self, rang, model, tezlik, orindiq_soni):
#         super().__init__(rang, model, tezlik)
#         self.orindiq_soni = orindiq_soni
#
# gentra = Mashina("Oq", "Gentra 1.6", 200)
# damas = Mashina("Oq", "Damas 2", 300)
# bmw = Mashina("qora", "BMW m5", 500)
#
# isuzu = Avtobus("Oq", "Isuzu", 500, 50)
#
# print(isuzu.rang)

# #Dataclass
# from dataclasses import dataclass
#
# @dataclass
# class Mashina:
#     rang: str
#     model: str
#     tezlik: int
#
# @dataclass
# class Avtobus(Mashina):
#     orindiq_soni: int
#
# gentra = Mashina("Oq", "Gentra 1.6", 200)
# damas = Mashina("Oq", "Damas 2", 300)
# bmw = Mashina("qora", "BMW m5", 500)
#
# isuzu = Avtobus("Oq", "Isuzu", 500, 50)
#
# print(isuzu)