#Banka Hesap Yönetim ve İşlem Takip Sistemi
from datetime import datetime
def dekor_time(func):
    def wrapper(*args,**kwargs):
        zaman=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        print(f"{zaman} işlem başlatiliyor...")
        sonuc=func(*args,**kwargs)
        print(f"{zaman} işlem başariyla tamamlandi...")
        return sonuc
    return wrapper

class hesap:
    def __init__(self,hesap_sahibi,bakiye=0):
        self.hesap_sahibi=hesap_sahibi
        self.bakiye=bakiye

    @dekor_time
    def para_yatir(self,yatirilacaktutar):
        if yatirilacaktutar<=0:
            print("yatirilacak tutar negatif veya 0 olamaz!!!")
            return
        else:
         self.bakiye+=yatirilacaktutar
         print(f"güncel bakiyeniz : {self.bakiye}")
         return self.bakiye

    @dekor_time  
    def para_çek(self,çekilecek_tutar):
         if çekilecek_tutar<=0:
             print("çekilecek tutar negatif veya 0 olamaz!!!")
             return
         if self.bakiye<çekilecek_tutar:
              print("çekilecek tutar hesap bakiyesinden yüksek olamaz!!!")
              return
         self.bakiye-=çekilecek_tutar
         print(f"güncel bakiyeniz : {self.bakiye}")
         return self.bakiye

class vadeli_hesap(hesap):
    def __init__(self, hesap_sahibi, bakiye=0,faiz_orani=0.15):
        super().__init__(hesap_sahibi, bakiye)
        self.faiz_orani=faiz_orani

    @dekor_time
    def faiz_getirisi_hesapla(self,gün_sayisi):
        if gün_sayisi<=0:
            print("gün sayisi 0 veya eksi olamaz!!!")
            return
        hesaplanmis_faiz=(self.bakiye*gün_sayisi*self.faiz_orani)/365
        print(f"{gün_sayisi} günün toplam faiz getirisi : {hesaplanmis_faiz:.2f}")
        return hesaplanmis_faiz

kisi1=hesap("Masher1",1000)
kisi2=vadeli_hesap("Masher2",15000,0.35)
kisi1.para_yatir(500)
kisi1.para_çek(250)
print("------------------------------------------")
kisi2.para_yatir(5000)
kisi2.faiz_getirisi_hesapla(30)