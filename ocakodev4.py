def en_kucuk_en_buyuk_sayi():
    sayilar = []
    for i in range(5):
        sayi = int(input(f"{i+1}. sayıyı giriniz: "))
        sayilar.append(sayi)
    en_buyuk = max(sayilar)
    en_kucuk = min(sayilar)
    print(f"en büyük sayı: {en_buyuk}")
    print(f"en küçük sayı: {en_kucuk}")
en_kucuk_en_buyuk_sayi()