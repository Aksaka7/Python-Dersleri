from os import system
from random import randint


class Guns:
    def __init__(self, isim: str, damage: int):
        self.__name = isim
        self.__damage = damage

    def vur(self, rakip):
        rakip.setCan(rakip.getCan() - self.__damage)
        self.__damage -= 1

    def getGunsName(self):
        return self.__name

    def getDamage(self):
        return self.__damage


class Karakter:
    def __init__(self, can: int, silah: Guns):
        self.__can = can
        self.__silah = silah

    def vur(self, rakip):
        self.__silah.vur(rakip)

    def getCan(self):
        return self.__can

    def setCan(self, yeniCan: int):
        self.__can = yeniCan

    def getGunName(self):
        return self.__silah.getGunsName()

    def getdamage(self):
        return self.__silah.getDamage()


class Dusman(Karakter):
    pass


class Player(Karakter):
    def __init__(self, isim: str, can: int, silah: Guns):
        Karakter.__init__(self, can, silah)
        self.__isim = isim

    def getIsim(self):
        return self.__isim


def Main():
    dusmanlar = []

    for i in range(10):
        dusmanlar.append(Dusman(randint(25, 50), Guns('Pala', randint(5, 20))))

    oyuncu = Player('Zoe Nisa', 100, Guns('Samurai Kılıcı', 75))

    while True:
        system('clear')
        print(
            f" Oyuncu: {oyuncu.getIsim()} ----- Can: {oyuncu.getCan()} ----- Silah: {oyuncu.getGunName()} ----- Damage: {oyuncu.getdamage()}")
        print("==========================================================================================")
        for sayi, i in enumerate(dusmanlar):
            print(
                f"No:{sayi+1}  Düşman Can: {i.getCan()} ----- Düşman Damace: {i.getdamage()} ----- Düşman Silah: {i.getGunName()}")
        print("==========================================================================================")

        secim = input("Saldırılacak Olan düşman: ")
        dusman = dusmanlar[int(secim)]
        oyuncu.vur(dusman)
        if dusman.getCan() <= 0:
            dusmanlar.remove(dusman)
            if not dusmanlar:
                print("Kazandınız")
                break

        if dusmanlar:
            # Oyunuya gelişi güzel saldır
            dusmanlar[randint(0, len(dusmanlar) - 1)].vur(oyuncu)
            if oyuncu.getCan() <= 0:
                print("-_-Game Over-_-")
                break


if __name__ == '__main__':
    Main()
