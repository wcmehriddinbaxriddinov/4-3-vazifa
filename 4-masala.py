from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, nomi):
        self.nomi = nomi

    @abstractmethod
    def harakatlan(self):
        pass

class Mashina(Transport):
    def harakatlan(self):
        return f"{self.nomi} yo'lda harakatlanmoqda"

class Velosiped(Transport):
    def harakatlan(self):
        return f"{self.nomi} yo'lda harakatlanmoqda"


mashina = Mashina("Mashina")
velosiped = Velosiped("Velosiped")

print(
    f"===== {mashina.nomi} =====\n" \
    f"{mashina.harakatlan()}"
)

print(
    f"===== {velosiped.nomi} =====\n" \
    f"{velosiped.harakatlan()}"
)