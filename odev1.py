sayi_1 = int(input("lütfen birinci sayıyı giriniz: ")) #sayılarımızı istedik
sayi_2 = int(input("lütfen ikinci sayıyı giriniz: "))
toplama = sayi_1 + sayi_2 #işlemleri yaptırdık
çıkarma = abs(sayi_1 - sayi_2)
çarpma = sayi_1 * sayi_2
bölme = sayi_1 / sayi_2
mod = sayi_1 % sayi_2
üs = sayi_1 ** sayi_2
print("toplamları:",toplama) #sonucları yazdırdık
print("farkları:",çıkarma)
print("çarpımları:",çarpma)
print("bölümleri:",bölme)
print("modları:",mod)
print("üsleri:",üs)


toplam = 0 #önce bos bir deger verdik
for i in range(1, 11):
    toplam += i #aralıktaki her sayıyla toplanmasını istedik
print(toplam) 


for cift in range(1, 100):  #1 ve 100 arası sayıları aldık
    if cift % 2==0: #sayıların 2 ile bölümlerinin 0 olanları sectik
        print(cift)

metin= input("bir metin gir: ") #metin istedik
ters_metin = ""
for char in metin:
    ters_metin = char + ters_metin #her karakteri tersten yazdırdık ters_metin'e
print("metnin tersi: ",ters_metin)