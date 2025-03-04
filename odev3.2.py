def not_ekle():
    while True:
        not_ekleme = input("lütfen günlüğünüzü yazın (çıkmak için 'çık' yazın): ")
        if not_ekleme == "çık":
            break
        with open("gunluk.txt","a",encoding="utf-8") as dosya:
            dosya.write(f"{not_ekleme}\n")
        print("notunuz eklendi")

def notları_goruntule():
    with open("gunluk.txt","r",encoding="utf-8") as dosya:
        content=dosya.read()
        if content:
            print("dosyanızdaki notlar:")
            print(content)
        else:
            print("dosya boş!")

def notları_sil():
    if open("gunluk.txt", "r", encoding="utf-8"):
        with open("gunluk.txt","w",encoding="utf-8") as dosya:
            dosya.truncate(0)
        print("dosya silindi!")
    else:
        print("dosya zaten mevcut değil!")


def menu():
    while True:
        komut = input("lütfen yapmak istediğiniz işlemi seçiniz ('not ekle', 'goruntule', 'sil', 'çık'): ")
        if komut == "not ekle":
            not_ekle()
        elif komut == "goruntule":
            notları_goruntule()
        elif komut== "sil":
            notları_sil()
        elif komut == "çık":
            break
        else:
            print("geçersiz komut girdiniz!")
menu()