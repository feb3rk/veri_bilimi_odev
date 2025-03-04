def numara_ekle(dosya):
    ad = input("adı girin: ")
    numara = input("telefon numarasını girin: ")
    with open(dosya, "a", encoding="utf-8") as f:
        f.write(f"{ad}: {numara}\n")
    print("numara başarıyla eklendi!")

def numara_ara(dosya):
    ad = input("aramak istediğiniz adı girin: ")
    with open(dosya, "r", encoding="utf-8") as f:
        for satir in f:
            kayitli_ad, kayitli_numara = satir.strip().split(": ")
            if kayitli_ad.lower() == ad.lower():
                print(f"{ad} adlı kişinin numarası: {kayitli_numara}")
                return
    print("kişi bulunamadı!")

def rehberi_listele(dosya):
    with open(dosya, "r", encoding="utf-8") as f:
        rehber = f.readlines()
        if not rehber:
            print("rehber boş!")
        else:
            for satir in rehber:
                print(satir.strip())

dosya_adi = "rehber.txt"

while True:
    komut = input("komut girin (ekle/ara/listele/çıkış): ").strip().lower()
    if komut == "ekle":
        numara_ekle(dosya_adi)
    elif komut == "ara":
        numara_ara(dosya_adi)
    elif komut == "listele":
        rehberi_listele(dosya_adi)
    elif komut == "çıkış":
        print("programdan çıkılıyor...")
        break
    else:
        print("geçersiz komut! Lütfen 'ekle', 'ara', 'listele' veya 'çıkış' komutlarından birini girin.")