import calisan

class MaviYaka(calisan.Calisan):
    def __init__(self,ad,soyad,tc_no,yas,cinsiyet,uyruk,sektor,tecrube,maas,ypayi):
        super().__init__(ad,soyad,tc_no,yas,cinsiyet,uyruk,sektor,tecrube,maas)
        self.__yenimaas=int()
        self.__yipranma_payi=ypayi

    def set_yipranmapayi(self,ypayi):
        self.__yipranma_payi=ypayi
    def get_yipranmapayi(self):
        return self.__yipranma_payi

    def zam_hakki(self):
        tecrube=self.getyiltecrube()
        if tecrube<2:
            zam_orani=self.__yipranma_payi*10
            self.__yenimaas=self.get_maas()+((self.get_maas()*zam_orani)/100)
        elif tecrube>=2 and tecrube<4:
            if self.get_maas()<15000:
                zam_orani=((self.get_maas()%self.get_tecrube())/2)+(self.__yipranma_payi*10)
                self.__yenimaas = self.get_maas() + ((self.get_maas() * zam_orani) / 100)
        else:
            if self.get_maas()<25000:
                zam_orani= ((self.get_maas()%self.get_tecrube())/3)+(self.__yipranma_payi*10)
                self.__yenimaas = self.get_maas() + ((self.get_maas() * zam_orani) / 100)

    def get_yenimaas(self):
        self.zam_hakki()
        return int(self.__yenimaas)

    def __str__(self):
        maasbilgisi = self.get_yenimaas()
        text = "İsim:" + self.get_ad() +"\n"+ "Soyisim:" + self.get_soyad() +"\n" +"Tecrübe (yıl) :" + str(self.getyiltecrube())  +"\n"+"Maas:" + str(self.get_maas())
        return text