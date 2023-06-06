class Insan():
    def __init__(self,ad,soyad,tc_no,yas,cinsiyet,uyruk):
        self.__ad=ad
        self.__soyad=soyad
        self.__tc_no=tc_no
        self.__yas=yas
        self.__cinsiyet=cinsiyet
        self.__uyruk=uyruk

    def __str__(self):
        text = "İsim : {}\nSoyisim:{}\nT.C. Kimlik Numarası : {}\nYas : {}\nCinsiyet : {}\nUyruk : {}".format(self.__ad,self.__soyad,self.__tc_no,self.__yas,self.__cinsiyet,self.__uyruk)
        return text

    def get_ad(self):
        return self.__ad

    def set_ad(self, isim):
        self.__ad = isim

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyisim):
        self.__soyad = soyisim

    def get_tcno(self):
        return self.__tc_no

    def set_tcno(self, tcnumara):
        self.__tc_no = tcnumara

    def get_yas(self):
        return self.__yas

    def set_yas(self, yeniyas):
        self.__yas = yeniyas

    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_cinsiyet(self, gender):
        self.__cinsiyet = gender

    def get_uyruk(self):
        return self.__uyruk

    def set_uyruk(self, nationanlity):
        self.__uyruk = nationanlity