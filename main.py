import insan,issiz,calisan,maviyaka,beyazyaka
import pandas as pd

print("\n\n\n")

insan1=insan.Insan("Mustafa","Ok","12345678912",34,"Erkek","Türk")
insan2=insan.Insan("Ahmet","Ateş","98745632178",23,"Erkek","Türk")

print(insan1,"\n")
print(insan2,"\n")

issiz1=issiz.Issiz("Sonay","Yıldız","12345678912",22,"Kadın","Türk",8,2,5)
issiz2=issiz.Issiz("Cemre","Demir","12345348912",42,"Kadın","Türk",3,1,6)
issiz3=issiz.Issiz("Bradley","James","12345354612",38,"Erkek","İngiliz",4,8,1)

print(issiz1,"\n")
print(issiz2,"\n")
print(issiz3,"\n")

calisan1=calisan.Calisan("Katie","McGrath","12343254612",36,"Kadın","İngiliz","diğer",120,24000)
calisan2=calisan.Calisan("Alaattin","Timurtaş","12343254612",37,"Erkek","Türk","inşaat",15,13000)
calisan3=calisan.Calisan("Barış","Çubuk","12343254612",28,"Erkek","Türk","teknoloji",36,14000)


print(calisan1,"\n")
print(calisan2,"\n")
print(calisan3,"\n")

maviyaka1=maviyaka.MaviYaka("Colin","Morgan","12343254612",24,"Erkek","İngiliz","teknoloji",21,30000,0.2)

maviyaka2=maviyaka.MaviYaka("Megan","Boone","12343254612",43,"Kadın","Amerikan","diğer",47,13000,0.5)

maviyaka3=maviyaka.MaviYaka("Şevket","Çoruh","12343254612",32,"Erkek","Türk","muhasebe",134,23000,0.8)


print(maviyaka1,"\n")
print(maviyaka2,"\n")
print(maviyaka3,"\n")


beyazyaka1=beyazyaka.BeyazYaka("Özgür","Ozan","12343254612",38,"Erkek","İngiliz","inşaat",54,20000)
beyazyaka1.set_prim(500)
beyazyaka2=beyazyaka.BeyazYaka("Megan","Boone","12343254612",33,"Kadın","Amerikan","diğer",34,14000)
beyazyaka2.set_prim(750)
beyazyaka3=beyazyaka.BeyazYaka("Şevket","Çoruh","12343254612",31,"Erkek","Türk","muhasebe",98,44760)
beyazyaka3.set_prim(1000)

print(beyazyaka1,"\n")
print(beyazyaka2,"\n")
print(beyazyaka3,"\n")

print("\n\n\n")

data={"Nesne Değeri :" : ["Çalışan","Çalışan","Çalışan","Mavi Yaka","Mavi Yaka","Mavi Yaka","Beyaz Yaka","Beyaz Yaka","Beyaz Yaka"],
      "TC No: " : [calisan1.get_tcno(),calisan2.get_tcno(),calisan3.get_tcno(),maviyaka1.get_tcno(),maviyaka2.get_tcno(),maviyaka3.get_tcno(),beyazyaka1.get_tcno(),beyazyaka2.get_tcno(),beyazyaka3.get_tcno()],
      "Ad: " : [calisan1.get_ad(),calisan2.get_ad(),calisan3.get_ad(),maviyaka1.get_ad(),maviyaka2.get_ad(),maviyaka3.get_ad(),beyazyaka1.get_ad(),beyazyaka2.get_ad(),beyazyaka3.get_ad()],
      "Soyad: " : [calisan1.get_soyad(),calisan2.get_soyad(),calisan3.get_soyad(),maviyaka1.get_soyad(),maviyaka2.get_soyad(),maviyaka3.get_soyad(),beyazyaka1.get_soyad(),beyazyaka2.get_soyad(),beyazyaka3.get_soyad()],
      "Yaş: " : [calisan1.get_yas(),calisan2.get_yas(),calisan3.get_yas(),maviyaka1.get_yas(),maviyaka2.get_yas(),maviyaka3.get_yas(),beyazyaka1.get_yas(),beyazyaka2.get_yas(),beyazyaka3.get_yas()],
      "Cinsiyet: " : [calisan1.get_cinsiyet(),calisan2.get_cinsiyet(),calisan3.get_cinsiyet(),maviyaka1.get_cinsiyet(),maviyaka2.get_cinsiyet(),maviyaka3.get_cinsiyet(),beyazyaka1.get_cinsiyet(),beyazyaka2.get_cinsiyet(),beyazyaka3.get_cinsiyet()],
      "Uyruk: " : [calisan1.get_uyruk(),calisan2.get_uyruk(),calisan3.get_uyruk(),maviyaka1.get_uyruk(),maviyaka2.get_uyruk(),maviyaka3.get_uyruk(),beyazyaka1.get_uyruk(),beyazyaka2.get_uyruk(),beyazyaka3.get_uyruk()],
      "Sektör: " : [calisan1.get_sektor(),calisan2.get_sektor(),calisan3.get_sektor(),maviyaka1.get_sektor(),maviyaka2.get_sektor(),maviyaka3.get_sektor(),beyazyaka1.get_sektor(),beyazyaka2.get_sektor(),beyazyaka3.get_sektor()],
      "Tecrübe: " : [calisan1.getyiltecrube(),calisan2.getyiltecrube(),calisan3.getyiltecrube(),maviyaka1.getyiltecrube(),maviyaka2.getyiltecrube(),maviyaka3.getyiltecrube(),beyazyaka1.getyiltecrube(),beyazyaka2.getyiltecrube(),beyazyaka3.getyiltecrube()],
      "Maaş:" : [calisan1.get_maas(),calisan2.get_maas(),calisan3.get_maas(),maviyaka1.get_maas(),maviyaka2.get_maas(),maviyaka3.get_maas(),beyazyaka1.get_maas(),beyazyaka2.get_maas(),beyazyaka3.get_maas()],
      "Yıpranma Payı:" : [None,None,None,maviyaka1.get_yipranmapayi(),maviyaka2.get_yipranmapayi(),maviyaka3.get_yipranmapayi(),None,None,None],
      "Teşvik Primi:": [None,None,None,None,None,None,beyazyaka1.get_prim(),beyazyaka2.get_prim(),beyazyaka3.get_prim()],
      "Yeni Maaş:" : [calisan1.getyenimaas(),calisan2.getyenimaas(),calisan3.getyenimaas(),maviyaka1.get_yenimaas(),maviyaka2.get_yenimaas(),maviyaka3.get_yenimaas(),beyazyaka1.get_yenimaas(),beyazyaka2.get_yenimaas(),beyazyaka3.get_yenimaas()]}

frame=pd.DataFrame(data)
df_sonhal = frame.fillna(0)
print(df_sonhal)

print("\n\n\n")

grouped_data = df_sonhal.groupby('Nesne Değeri :').agg({'Tecrübe: ': 'mean', 'Yeni Maaş:': 'mean'})
print(grouped_data)

print("\n\n\n")

onbesbinuzeri = len(df_sonhal[df_sonhal['Yeni Maaş:'] > 15000])
print("Toplam maaşı 15000 TL üzerinde olan çalışan sayısı:", onbesbinuzeri)

print("\n\n\n")

sirali_df = df_sonhal.sort_values(by='Yeni Maaş:')
print(sirali_df)

print("\n\n\n")

beyaz_yakalilar = df_sonhal[(df_sonhal['Nesne Değeri :'] == 'Beyaz Yaka') & (df_sonhal['Tecrübe: '] > 3)]
print(beyaz_yakalilar)

print("\n\n\n")

filtre_df = df_sonhal[df_sonhal['Yeni Maaş:'] > 10000].loc[1:5, ['TC No: ', 'Yeni Maaş:']]
print(filtre_df)

print("\n\n\n")

yeniframe = df_sonhal[['Ad: ', 'Soyad: ', 'Sektör: ', 'Yeni Maaş:']]
print(yeniframe)




