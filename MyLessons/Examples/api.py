import requests
api = 'https://api.escuelajs.co/api/v1/products'
response = requests.get(api)
if response.status_code==200:
      data = response.json()
      if data:
      
        print(data)
      else: print("Data Bosdur")
      
