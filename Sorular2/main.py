class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"{self.ad}: Merhaba, ben bir insanım.")


class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    def konus(self):
        print(f"{self.ad}: Merhaba, ben hocayım.")

    def ders_ver(self):
        print(f"{self.ad} ders veriyor.")


class Sekreter(Insan):
    def __init__(self, ad, yas, ofis_no):
        super().__init__(ad, yas)
        self.ofis_no = ofis_no

    def konus(self):
        print(f"{self.ad}: Merhaba, ben sekreterim.")

    def randevu_ayarla(self):
        print(f"{self.ad} randevu ayarlıyor.")


class Ogrenci(Insan):
    def __init__(self, ad, yas, ogr_no):
        super().__init__(ad, yas)
        self.ogr_no = ogr_no

    def konus(self):
        print(f"{self.ad}: Merhaba, ben öğrenciyim.")

    def ders_calıs(self):
        print(f"{self.ad} ders çalışıyor.")


hoca = Hoca("Ahmet", 40, "H123")
sekreter = Sekreter("Ayşe", 35, "Ofis-2")
ogrenci = Ogrenci("Mehmet", 20, "O456")

hoca.konus()
hoca.ders_ver()

sekreter.konus()
sekreter.randevu_ayarla()

ogrenci.konus()
ogrenci.ders_calıs()
