print("Xosh Gelmisiniz!")
def menu():
   button = int(input("Fayl elave etmek ucun 1\nMovcud Fayla baxmaq ucun 2\nDuymesini Secin\n:"))
   if button==1:
       metn_yazma()
   elif button == 2:
       metn_oxuma()
      
       
def metn_yazma():
    file_name = input("Fayla Ad Verin\n:")
    file_txt = input("Fayla geyd etmek istediyiniz Yazini daxil Edin\n:")
    with open(file_name+'.txt','w') as file:
       file.write(file_txt)
       print("Metn Fayla Yazildi")

    
def metn_oxuma():
    oxunacaq_metn = input("Faylin adin daxil edin\n:")
    oxunacaq_metn += ".txt"
    with open(oxunacaq_metn,'r') as file:
         content = file.read()
         print(f"{oxunacaq_metn}:\n{content}")
    
while True:
    menu()
