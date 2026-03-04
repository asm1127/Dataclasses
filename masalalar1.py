# #1
# from dataclasses import dataclass
# from email.iterators import body_line_iterator
#
#
# @dataclass
# class Tortburchak:
#     eni: float
#     boyi: float
#
#     def hisobla(self):
#         return self.eni * self.boyi
#
# shakl = Tortburchak(15, 6)
#
# print(shakl.hisobla())

# #2
# from dataclasses import dataclass
#
# @dataclass
# class Doira:
#     radius: float
#
# shakl = Doira(5)
# print(shakl.radius * shakl.radius * 3.14)


# #3
# from dataclasses import dataclass
#
# @dataclass
# class Talaba:
#     ism: str
#     baho: int
#
# talaba_bahosi = Talaba("Shaxlo", 5)
#
# print(f"{talaba_bahosi.ism}ning baxosi: {talaba_bahosi.baho}")

# #4
# from dataclasses import dataclass
#
# @dataclass
# class Tortburchak:
#     eni: float
#     boyi: float
#
# eni = float(10)
# boyi = float(20)
#
# perimetr = 2 * (eni + boyi)
# print(f"To'rtburchak perimetri: {r.uzunlik_hisobla()}")

# #5
# from dataclasses import dataclass
# import math
#
# @dataclass
# class Doira:
#     radius: float
#
#     def uzunlik_hisobla(self) -> float:
#         return 2 * math.pi * self.radius
#
# r = Doira(9)
# print(f"Doira radiusi: {r.uzunlik_hisobla()}")

# #6
# from dataclasses import dataclass
#
# @dataclass
# class Mashina:
#     model: str
#     narx: int
#
# mashin = Mashina('Malibu', 80_000_000)
# print(mashin)

# #7
# from dataclasses import dataclass
#
# @dataclass
# class Kitob:
#     nom: str
#     sahifalar: int
#
# sahifa = Kitob("Qo'zichoqlar sukunati", 500)
# print(f"Kitob sahifalari: {sahifa.sahifalar} ta")

# #8
# from dataclasses import dataclass
# from math import sqrt
#
# @dataclass
# class Tortburchak:
#     eni: float
#     boyi: float
#
#     def hisobla(self) -> float:
#         return sqrt(self.eni**2 + self.boyi**2)
#
# a = Tortburchak(10, 5)
# print(a.hisobla())

# #9
# from dataclasses import dataclass
#
# @dataclass
# class Talaba:
#     ismi: str
#     yoshi: int
#
# tal = Talaba('Zokir', 20)
# print(f"Talabaning yoshi: {tal.yoshi} da")

# #10
# from dataclasses import dataclass
#
# @dataclass
# class Uchburchak:
#     asos: int
#     balandlik: int
#
#     def hisobla(self):
#         return self.asos * self.balandlik / 2
#
# b = Uchburchak(6, 8)
# print(b.hisobla())