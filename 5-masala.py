from abc import ABC, abstractmethod

class Tolov(ABC):
    def __init__(self, nomi):
        self.nomi = nomi

    @abstractmethod
    def tolash(self, summa):
        pass


class NaqdTolov(Tolov):
    def tolash(self, summa):
        return f"{summa} so'm naqd pul orqali tolandi"


class KartaTolov(Tolov):
    def tolash(self, summa):
        return f"{summa} so'm karta orqali tolandi"


naqd = NaqdTolov("Naqd to'lov")
karta = KartaTolov("Karta to'lovi")

print(f"======== {naqd.nomi} ========\n" \
      f"{naqd.tolash(50000)}")

print(f"======== {karta.nomi} ========\n" \
      f"{karta.tolash(50000)}")