class BankHisobi:
    def __init__(self, nomi, balans):
        self.nomi = nomi
        self.__balans = balans

    def balansni_korish(self):
        return self.__balans

    def pul_qosh(self, miqdor):
        if miqdor > 0:
            self.__balans += miqdor
            return f"{self.nomi} - {miqdor} so'm qo'shildi"
        else:
            return "Miqdor 0 dan kam bolmasligi kerak"

    def pul_yechish(self, miqdor):
        if 0 < miqdor <= self.__balans:
            self.__balans -= miqdor
            return f"{self.nomi} - {miqdor} so'm yechildi"
        else:
            return f"{self.nomi} Balans yetarli emas"


hisob = BankHisobi("hisob", 100000)

print(
    f"===== {hisob.nomi} =====\n" \
    f"{hisob.pul_qosh(25000)}\n" \
    f"{hisob.pul_yechish(30000)}\n" \
    f"Balans: {hisob.balansni_korish()} so'm"
)