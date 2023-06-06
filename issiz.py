import insan

class Issiz(insan.Insan):
    def __init__(self,ad,soyad,tc_no,yas,cinsiyet,uyruk,maviyaka_tecrube,beyazyaka_tecrube,yonetici_tecrube):
        super().__init__(ad,soyad,tc_no,yas,cinsiyet,uyruk)
        self.__experience=dict()

        self.__experience["maviyaka"]=maviyaka_tecrube
        self.__experience["beyazyaka"]=beyazyaka_tecrube
        self.__experience["yonetici"]=yonetici_tecrube
    def get_mytecrube(self):
        return self.__experience["maviyaka"]
    def set_mytecrube(self,yenimytecrube):
        self.__experience["maviyaka"]=yenimytecrube
    def get_bytecrube(self):
        return self.__experience["beyazyaka"]
    def set_bytecrube(self,yenibytecrube):
        self.__experience["beyazyaka"]=yenibytecrube
    def get_ytecrube(self):
        return self.__experience["yonetici"]
    def set_ytecrube(self,yeniytecrube):
        self.__experience["yonetici"]=yeniytecrube
    def statu_bul(self):
        maviyaka_deger=self.__experience["maviyaka"]*0.20
        beyazyaka_deger=self.__experience["beyazyaka"]*0.35
        yonetici_deger=self.__experience["yonetici"]*0.45

        uygun_statu=str()

        if yonetici_deger>beyazyaka_deger:
            if yonetici_deger>maviyaka_deger:
                uygun_statu="yonetici"
            else:
                uygun_statu="maviyaka"
        else:
            if beyazyaka_deger>maviyaka_deger:
                uygun_statu="beyazyaka"
            else:
                uygun_statu="maviyaka"
        return uygun_statu
    def __str__(self):
        self.__statu=self.statu_bul()
        text="İsim:",self.get_ad(),"Soyad:",self.get_soyad(),"En Uygun Statü:",self.__statu
        return text
