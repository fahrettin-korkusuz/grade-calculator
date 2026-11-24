def ortalama_hesapla(vize, final):
    return vize * 0.40 + final * 0.60

def durum_hesapla(ortalama):
    if ortalama >= 60:
        return "Geçti"
    else:
        return "Kaldı"

def harf_notu(ortalama):
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 65:
        return "DC"
    elif ortalama >= 60:
        return "DD"
    elif ortalama >= 50:
        return "FD"
    else:
        return "FF"
    

print("=" * 40)
print("NOT ORTALAMASI HESAPLAMA SİSTEMİ")
print("=" * 40)

ogrenci = input("Öğrenci adı ve soyadı: ")
dersler = []
while True:
    ders = input("Ders adı: ")

    vize = float(input("Vize notu: "))
    final = float(input("Final notu: "))

    ortalama = ortalama_hesapla(vize, final)
    dersler.append(ortalama)
    durum = durum_hesapla(ortalama)
    harf = harf_notu(ortalama)

    print("Öğrenci:", ogrenci)
    print("Ders:", ders)
    print("Vize:", vize)
    print("Final:", final)
    print("Ortalama:", ortalama)
    print("Durum:", durum)
    print("Harf notu:", harf)

    devam = input("Başka ders eklemek ister misiniz? (E/H): ")

    if devam == "H":
        break


genel_ortalama = sum(dersler) / len(dersler)

print("Toplam ders sayısı:", len(dersler))
print("Genel not ortalaması:", genel_ortalama)