class Buah:
    def __init__(self,nama,warna,rasa):
        self.__nama = nama
        self.__warna = warna
        self.__rasa = rasa

    def getNama(self):
        return self.__nama
    def getWarna(self):
        return self.__warna
    def getRasa(self):
        return self.__rasa
    
    def Informasi(self):
        return f'Nama : {self.getNama()}, Warna : {self.getWarna()}, Rasa : {self.getRasa()}'
    
class Mangga:
    def __init__(self, vitamin):
        self.__vitamin = vitamin

    def get_vitamin(self):
        return self.__vitamin
    
    def info_mangga(self):
        return f'Vitamin: {self.get_vitamin()}'
    
class Gabungan(Buah, Mangga):
    def __init__(self, nama, warna, rasa, vitamin):
        Buah.__init__(self, nama, warna, rasa)
        Mangga.__init__(self, vitamin)
    
    def info(self):
        return f'{self.Informasi()} \nVitamin: {self.get_vitamin()}'
