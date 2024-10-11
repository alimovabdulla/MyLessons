import time

parol_m = "M123"
parol_t = "S123"
telebe = {}

def telebe_guncelle(ad, yas, sinfi, nomre, bal):
    if ad in telebe:
        telebe[ad]["yas"] = yas
        telebe[ad]["sinfi"] = sinfi
        telebe[ad]["nomre"] = nomre
        telebe[ad]["bal"] = bal
    else:
        print(f"Telebe {ad} Sistemde Tapilmadi!")

def telebe_elave_et(ad, yas, sinfi, nomre, bal):
    telebe[ad] = {"yas": yas, "sinfi": sinfi, "nomre": nomre, "bal": bal}

def muellim():
    parol = input("Parolu Daxil Edin\n: ")
    if parol == parol_m:
        while True:
            secim = int(input("Menuya Xosh Geldiniz!\n"
                              "Telebe Elave Etmek Ucun 1\n"
                              "Telebeni Sistemden Silmek Ucun 2\n"
                              "Sinifinizdeki Telebelere Baxmaq ucun 3\n"
                              "Telebenin Melumatini Guncellemek Ucun 4\n"
                              "Cixis Etmek Ucun 5\n"
                              "Duymesini Secin\n: "))
            
            if secim == 1:
                e = input("Telebenin adi: ")
                f = int(input("Telebenin yasi\n: "))
                g = input("Telebenin sinifi\n: ")
                p = input("Telebenin nomresi\n: ")
                z = input("Telebenin bali\n: ")
                print("Analiz Aparilir, Zehmet olmasa 1 D?qiq? g?zl?yin...")
                time.sleep(10)
                telebe_elave_et(e, f, g, p, z)
                print("U?urla ?lav? edildi")
            
            elif secim == 2:
                sil = input("Telebenin Adin Daxil Edin\n: ")
                if sil in telebe:
                    del telebe[sil]
                    print("Telebe U?urla Silindi!")
                else:
                    print("Telebe Tapilmadi!")
            
            elif secim == 3:
                for ad in telebe:
                    print(ad)
            
            elif secim == 4:
                ad = input("Telebenin Adin Qeyd Edin:\n")
                yeni_yas = int(input("Yeni Yasini Qeyd Edin:\n"))
                yeni_sinif = input("Yeni Sinifini Qeyd Edin:\n")
                yeni_nomre = input("Yeni Nomresini Qeyd Edin:\n")
                yeni_bali = input("Yeni Balini Qeyd Edin:\n")
                telebe_guncelle(ad, yeni_yas, yeni_sinif, yeni_nomre, yeni_bali)
                print(f"Telebe {ad}'n Bali Ugurla Guncellendi!")
            
            elif secim == 5:
                print("Sistemden Ugurla Cixdiniz!\n\n")
                break
    else:
        print("Parol Yanl??d?r!!!")

def sagird():
    c = input("Parol: ")
    if c == parol_t:
        ad = input("Adinizi daxil edin: ")
        if ad in telebe:
            for ad in telebe:
                print(ad)
        else:
            print("Telebe tapilmadi!")
    else:
        print("Siz icaz?li deyilsiniz!")

def menu():
    a = int(input("Xo? G?lmisiniz!\nM??lliml?r ???n 1\n?agirdl?r ???n 2\nD?ym?sini se?in\n: "))
    if a == 1:
        muellim()
    elif a == 2:
        sagird()

while True:
    menu()
