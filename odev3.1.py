def kisi_ekle():
    while True:
        ad = input("lütfen isim giriniz (çıkış yapmak için 'bitti' yazın): ")
        if ad == "bitti":
            break
        with open("ogrenciler.txt","a",encoding="utf-8") as dosya:
            dosya.write(f"\n{ad}")
        print("kişi eklendi!")

def kisileri_goster():
    with open("ogrenciler.txt", "r", encoding="utf-8") as dosya:
        content = dosya.read()
        if content:
            print("\ndosyadaki öğrenciler: ")
            print(content)
        else:
            print("dosya boş")
kisi_ekle()

kisileri_goster()