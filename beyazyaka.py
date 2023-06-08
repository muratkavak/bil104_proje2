import calisan

class BeyazYaka(calisan.Calisan):
    def __init__(self):
        self.__tesvikprim=int()

    def get_prim(self):
        return self.__tesvikprim
    def set_prim(self,prim):
        self.__tesvikprim=prim
    def zam_hakki(self):
        tecrube = self.get_tecrube()
        if tecrube < 2:
            self.__yenimaas = int(self.get_maas()) + self.__tesvikprim
        elif tecrube >= 2 and tecrube < 4:
            if self.get_maas() < 15000:
                zam_miktari = ((self.get_maas() % self.get_tecrube()) * 5) + self.__tesvikprim
                self.__yenimaas = int(self.get_maas()) + int(zam_miktari)
            else:
                self.__yenimaas=self.get_maas()
        else:
            if self.get_maas() < 25000:
                zam_miktari = ((self.get_maas() % self.get_tecrube()) * 5) + self.__tesvikprim
                self.__yenimaas = int(self.get_maas()) + int(zam_miktari)
            else:
                self.__yenimaas=self.get_maas()

    def get_yenimaas(self):
        self.zam_hakki()
        return self.__yenimaas
    def __str__(self):
        maasbilgisi = self.get_yenimaas()
        text = "İsim:" + self.get_ad() + "Soyisim:" + self.get_soyad() + "Tecrübe (ay) :" + str(self.get_tecrube()) + "Maas:" + str(maasbilgisi)
        return text