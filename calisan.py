import insan

class Calisan(insan.Insan):
    def __init__(self,ad,soyad,tc_no,yas,cinsiyet,uyruk,sektor,tecrube,maas):
        super().__init__(ad,soyad,tc_no,yas,cinsiyet,uyruk)
        if sektor=="inşaat" or sektor=="teknoloji" or sektor=="muhasebe" or sektor=="diğer":
            self.__sektor=sektor
            self.__tecrube=tecrube
            self.__maas=int(maas)
        else:
            while True:
                sektor=input("Lütfen gecerli bir sektör giriniz :")
                if sektor == "insaat" or sektor == "teknoloji" or sektor == "muhasebe" or sektor == "diger":
                    self.__sektor = sektor
                    self.__tecrube = tecrube
                    self.__maas = maas
                    break
        self.yiltecrube = round((self.__tecrube / 12),2)
    def get_sektor(self):
        return self.__sektor
    def set_sektor(self,sektorbilgisi):
        self.__sektor=sektorbilgisi

    def get_tecrube(self):
        return self.__tecrube
    def getyiltecrube(self):
        return self.yiltecrube
    def set_tecrube(self,tecrubebilgisi):
        self.__tecrube=tecrubebilgisi

    def get_maas(self):
        return int(self.__maas)
    def getyenimaas(self):
        self.sonmaas=self.zam_hakki()
        return int(self.sonmaas)
    def set_maas(self,maasbilgisi):
        self.__maas=maasbilgisi

    def zam_hakki(self):

        if self.yiltecrube<2:
            self.zamhakki=0
        elif self.yiltecrube>=2 and self.yiltecrube<4:
            if self.__maas<15000:
                self.zamhakki=self.__maas%self.__tecrube
            else:
                self.zamhakki=0
        else:
            if self.__maas<25000:
                self.zamhakki = (self.__maas % self.__tecrube)/2
            else:
                self.zamhakki=0
        self.yenimaas=self.__maas+((self.__maas*self.zamhakki)/100)
        return self.yenimaas
    def __str__(self):
        maasbilgisi=self.zam_hakki()
        text="İsim:"+self.get_ad()+"\n"+"Soyisim:"+self.get_soyad()+"\n"+"Tecrübe (yıl) :"+str(self.getyiltecrube())+"\n"+"Maas:"+str(maasbilgisi)
        return text


