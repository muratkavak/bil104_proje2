import insan

class Calisan(insan.Insan):
    def __init__(self,ad,soyad,tc_no,yas,cinsiyet,uyruk,sektor,tecrube,maas):
        super().__init__(ad,soyad,tc_no,yas,cinsiyet,uyruk)
        if sektor=="insaat" or sektor=="teknoloji" or sektor=="muhasebe" or sektor=="diger":
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
    def get_sektor(self):
        return self.__sektor
    def set_sektor(self,sektorbilgisi):
        self.__sektor=sektorbilgisi

    def get_tecrube(self):
        return self.__tecrube
    def set_tecrube(self,tecrubebilgisi):
        self.__tecrube=tecrubebilgisi

    def get_maas(self):
        return self.__maas
    def set_maas(self,maasbilgisi):
        self.__maas=maasbilgisi

    def zam_hakki(self):
        if self.__tecrube<2:
            self.zamhakki=0
        elif self.__tecrube>=2 and self.__tecrube<4:
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
        text="İsim:"+self.get_ad()+"Soyisim:"+self.get_soyad()+"Tecrübe (ay) :"+str(self.__tecrube)+"Maas:"+str(maasbilgisi)
        return text


