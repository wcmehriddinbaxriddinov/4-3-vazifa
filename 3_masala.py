class Mahsulot:
    def __init__(self, nom, miqdor):
        self.nom = nom
        self.__miqdor = miqdor

    def miqdorni_korish(self):
        return self.__miqdor

    def qabul_qil(self, son):
        self.__miqdor += son
        return f"{self.nom} - {son} dona qabul qilindi"

    def sotish(self, son):
        if son <= self.__miqdor:
            self.__miqdor -= son
            return f"{self.nom} - {son} dona sotildi"
        else:
            return f"{self.nom} - omborda yetarli emas"


mahsulot = Mahsulot("Daftar", 20)

print(
    f"{mahsulot.sotish(6)}\n" \
    f"{mahsulot.qabul_qil(4)}\n" \
    f"Miqdor: {mahsulot.miqdorni_korish()} dona"
)