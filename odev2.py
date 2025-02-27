ogrenciler = []

def ogrenci_ekle():
    ad = input("Öğrencinin adını girin: ")
    soyad = input("Öğrencinin soyadını girin: ")
    numara = input("Öğrencinin numarasını girin: ")
    bolum = input("Öğrencinin bölümünü girin: ")
    not_ortalamasi = float(input("Öğrencinin not ortalamasını girin: "))
    
    ogrenci = {
        "Ad": ad,
        "Soyad": soyad,
        "Numara": numara,
        "Bölüm": bolum,
        "Not Ortalaması": not_ortalamasi
    }
    
    ogrenciler.append(ogrenci)
    print(f"{ad} {soyad} başarıyla eklendi!")

def tum_ogrencileri_goruntule():
    if not ogrenciler:
        print("Hiç öğrenci kaydı bulunmamaktadır.")
    else:
        for ogrenci in ogrenciler:
            print(ogrenci)

def ogrenci_bilgileri_goruntule():
    numara = input("Bilgilerini görmek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            print(ogrenci)
            return
    print("Öğrenci bulunamadı!")

def ogrenci_guncelle():
    numara = input("Bilgilerini güncellemek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            yeni_bolum = input("Yeni bölüm: ")
            yeni_not_ortalamasi = float(input("Yeni not ortalaması: "))
            ogrenci["Bölüm"] = yeni_bolum
            ogrenci["Not Ortalaması"] = yeni_not_ortalamasi
            print("Öğrenci bilgileri güncellendi!")
            return
    print("Öğrenci bulunamadı!")

def ogrenci_sil():
    numara = input("Silmek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["Numara"] == numara:
            ogrenciler.remove(ogrenci)
            print("Öğrenci silindi!")
            return
    print("Öğrenci bulunamadı!")

def menu():
    while True:
        print("\nÖğrenci Yönetim Sistemi")
        print("1 - Öğrenci Ekle")
        print("2 - Tüm Öğrencileri Listele")
        print("3 - Öğrenci Bilgilerini Görüntüle")
        print("4 - Öğrenci Güncelle")
        print("5 - Öğrenci Sil")
        print("6 - Çıkış")
        
        secim = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
        
        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            tum_ogrencileri_goruntule()
        elif secim == "3":
            ogrenci_bilgileri_goruntule()
        elif secim == "4":
            ogrenci_guncelle()
        elif secim == "5":
            ogrenci_sil()
        elif secim == "6":
            print("Uygulamadan çıkılıyor....")
            break
        else:
            print("Lütfen 1-6 arasında bir sayı giriniz.")

menu()
