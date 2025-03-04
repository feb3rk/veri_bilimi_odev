import json

def kullanici_ekle(dosya):
    ad = input("adınızı girin: ")
    soyad = input("soyadınızı girin: ")
    yas = input("yaşınızı girin: ")
    
    with open(dosya, "r", encoding="utf-8") as f:
        kullanicilar = json.load(f)
    
    kullanicilar.append({"ad": ad, "soyad": soyad, "yas": yas})
    
    with open(dosya, "w", encoding="utf-8") as f:
        json.dump(kullanicilar, f, ensure_ascii=False, indent=4)
    
    print("kullanıcı başarıyla eklendi!")

def kullanicilari_listele(dosya):
    with open(dosya, "r", encoding="utf-8") as f:
        kullanicilar = json.load(f)
        if not kullanicilar:
            print("henüz kayıtlı kullanıcı yok.")
        else:
            for k in kullanicilar:
                print(f"ad: {k['ad']}, soyad: {k['soyad']}, yaş: {k['yas']}")

dosya_adi = "kullanicilar.json"

while True:
    komut = input("komut girin (ekle/listele/çıkış): ").strip().lower()
    if komut == "ekle":
        kullanici_ekle(dosya_adi)
    elif komut == "listele":
        kullanicilari_listele(dosya_adi)
    elif komut == "çıkış":
        print("programdan çıkılıyor...")
        break
    else:
        print("geçersiz komut! lütfen 'ekle', 'listele' veya 'çıkış' komutlarından birini girin.")