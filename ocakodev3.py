sayi = int(input("lütfen bir sayı giriniz: "))
toplam_for=0
for i in range (1, sayi + 1):
    toplam_for += i
print(f"for döngüsü ile toplam: {toplam_for}")


toplam_while=0
s=1
while s <= sayi:
    toplam_while += s
    sayi += 1
print(f"while döngüsü ile toplam: {toplam_while}")