class Telefon:
    def __init__(self, nomi, quvvat):
        self.nomi = nomi
        self.__quvvat = max(0, min(100, quvvat))

    def quvvatni_korish(self):
        return self.__quvvat

    def zaryadlash(self, foiz):
        self.__quvvat = min(100, self.__quvvat + foiz)
        return f"{self.nomi} - {foiz}% zaryadlandi"

    def ishlat(self, foiz):
        self.__quvvat = max(0, self.__quvvat - foiz)
        return f"{self.nomi} - {foiz}% ishlatildi"


telefon = Telefon("Telefon", 40)

print(
    f"===== {telefon.nomi} =====\n" \
    f"{telefon.zaryadlash(30)}\n"
    f"{telefon.ishlat(20)}\n" \
    f"Zaryad: {telefon.quvvatni_korish()}%"
)