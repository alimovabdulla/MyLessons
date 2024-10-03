import random

login_check = ['abdulla']
parol_check = ['2004', '2008']
random_number = random.randint(1, 999)
count = 0
kitablar = []
count_for_login =0

def menu():
    while True:
        print("\n1. Kitab əlavə et")
        print("2. Kitab sil")
        print("3. Kitab göstər")
        print("4. Çıxış")
    
        button = int(input("Seçiminizi edin: "))
    
        if button == 1:
            kitab_adi = input("Kitabın adı: ")
            muellif_adi = input("Müəllifin adı: ")
            kitab = {"Kitabin Adi": kitab_adi, "Muellif": muellif_adi}
            kitablar.append(kitab)
            print(f"{kitab['Kitabin Adi']} adlı kitab uğurla əlavə olundu.")
    
        elif button == 2:
            if kitablar:
                print("\nSilmək istədiyiniz kitab:")
                for i, x in enumerate(kitablar, 1):
                    print(f"{i}. Kitab: {x['Kitabin Adi']}, Müəllif: {x['Muellif']}")
                sil = int(input("Silinməsini istədiyiniz kitabın nömrəsini yazın: "))
                if 1 <= sil <= len(kitablar):
                    silinen = kitablar.pop(sil - 1)
                    print(f"{silinen['Kitabin Adi']} nömrəli kitab uğurla silindi.")
                else:
                    print("Kitab tapılmadı.")
            else:
                print("Kitabxana boşdur.")
    
        elif button == 3:
            if kitablar:
                print("\nKitabxanadakı kitablar:")
                for i, x in enumerate(kitablar, 1):
                    print(f"{i}. Kitab: {x['Kitabin Adi']}, Müəllif: {x['Muellif']}")
            else:
                print("Kitabxana boşdur.")
    
        elif button == 4:
            print("Bizi seçdiyiniz üçün təşəkkür edirik!")
            break
    
        else:
            print("Səhv seçim etdiniz. Yenidən cəhd edin.")


while True:
    print("                 Menuya Xosh Geldiniz!\nXidmetimizden Yararlanmaq Ucun Hesabiniza Daxil Olun!\n(Eyer HEsabiniz Yoxdursa Qeydiyyatdan kecin)")
    menu_button = int(input("Hesaba Giris Etmek Ucun 1\nKitablara Baxmaq Ucun 2\n: "))
    
    if menu_button == 1:
        login = input("Login: ")
        parol = input("Parol: ")
        
        if login in login_check and parol in parol_check:
            print("Hesabiniza Xosh Geldiniz!")
            count += 1
            menu()  
        elif login not in login_check and parol not in parol_check:
              
             count_for_try = 3
             count_for_login = count_for_login+1
             print(f"Login Ve Ya Parol Yalnisdir {count_for_try-1} Haqqiniz Qaldi")
              
        elif count_for_login == 3: 
             break