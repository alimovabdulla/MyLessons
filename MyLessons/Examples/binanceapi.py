import requests
print("Xosh Geldiniz!")
def menu():
    button = int(input("Qiymet Oyrenmek Ucun 1\nKonvert Emeliyyati Ucun 2\nDuymesini Secin\n:"))
    if button==1:
        coin_price()
    elif button==2:
        coin_convert()
    else: print("Sehf Secim Ettiniz")
    
def coin_convert():
   has = int(input("Mebleginiz\n:$"))
   convert = input("Qarsilardirmaq Istediyiniz Coin\n:")
   convert = convert.upper()
   api = f"https://api.binance.com/api/v3/ticker/price?symbol={convert}USDT"
   response = requests.get(api)
   if response.status_code==200:
      data = response.json()
      if 'price' in data:
          price = data['price']
          price = float(price)
          print(f"\nSizin ${has}'ra {has/price} {convert} Coin Dusur")
      else: print("Coin Movcud Deyil!")
   
   
def coin_price():
    coin = input("Qiymetini Oyrenmek IStediyiniz Coini Yazin\n:")
    coin = coin.upper()
    api = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT"
    response = requests.get(api)
    if response.status_code==200:
      data = response.json()
      if 'price' in data:
             price = data['price']
             print(f"\n{coin} Qiymeti: ${price}")
      else: print("Coin Movcud Deyil!")
   
while True:
    menu()