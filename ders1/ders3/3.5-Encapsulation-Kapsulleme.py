# Kapsülleme

#  bir Class verisine sadece SET VE GET ile ulasma anlamına gelmektedir. Geri kalan Class Metodlarına ulaşılmaz


class Araba:
    def __init__(self):
        self.__hiz = 0

    def setHiz(self, hiz):
        self.__hiz = hiz

    def getHiz(self):
        return self.__hiz


x = Araba()

print(x.getHiz())

x.setHiz(70)

print(x.getHiz())
