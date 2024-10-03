
# surusdurme = int(input("Nece defe surusdurulsun\n:"))
# metin = input("Metni Daxil Edin\n:")
# sifrelenmis_metin = ''

# for soz in metin:
#     yeni_soz = ord(soz) + surusdurme
#     sifrelenmis_metin += chr(yeni_soz)
    
# print(f"Sifrelenmis Metin: {sifrelenmis_metin}")
 
desifre_edilmis = ''
surusdurme = int(input("Nece defe surusdurulsun\n:"))
metin = input("Metni Daxil Edin\n:")
for  soz in metin:
     yeni_soz = ord(soz) - surusdurme
     desifre_edilmis += chr(yeni_soz)
     
print(f"Desifre Edilmis Soz: {desifre_edilmis}")


