from operator import index
from turtle import clear
from numpy import number
import pandas as pd
import numpy as np
from colorama import Fore, Back, Style, init
init()
def menu(data, clear_path):
    stop = True
    while stop:
        try:
            button = int(input(Fore.CYAN+"\nData Analizi Ucun 1\nDatani Temizlemek Ucun 2\nDataya Baxmaq Ucun 3\nBitirmek Ucun 0\n:"))
            if button == 1:
                data_analiz(data)
            elif button == 2:
                data_cleaning(data, clear_path)
            elif button == 3:
                print(data)
            elif button == 0:
                stop = False
                print(Fore.RED +"Ugurla Sona Catti!")
                return False   
            else:
                print(Fore.RED + "Sehf Secim!.")
        except ValueError:
            print(Fore.RED + "Xeta! Duzgun Secim Edin!")
    return stop

        
def data_cleaning(data, clear_path):
  try:
    button = int(input("Null deyerleri 0'ra Cevirmey ucun 1\nOzunnen Evvelkine Cervirmek ucun 2\nOzunden Sonrakina Cevirmek Ucun 3\nGeri donmek ucun 0\n:"))
    if button==1:
        null_to_zero(data, clear_path)
    elif button == 2:
        null_to_previous(data, clear_path)
    elif button == 3:
        null_to_next(data, clear_path)
  except:
      print(Fore.RED + "Xeta! Duzgun Secim Edin!")
       
        
def data_analiz(data):
  try:
    button= int(input("Regemsal Deyerlerin ortalama Analizi ucun 1\nUmumi Analiz ucun 2\nMedian ucun 3\n:"))
    if button==1:
         numeric_data_analiz(data)
    elif button == 2:
        general_analysis(data)
    elif button == 3:
        median_analiz(data)
  except :
      print(Fore.RED + "Xeta! Duzgun Secim Edin!")

def file_read():
   try:
    file_type = input("\nFaylın tipini qeyd edin (csv, json, xlsx, hdf, parquet, html, xml, feather, stata, sas, orc, clipboard)\n:") 
    file_path = input(Fore.LIGHTBLACK_EX+"Faylın yolunu yazın\n: ")
    if file_path.startswith('"') and file_path.endswith('"'):
     clear_path = file_path[1:-1]
     data = None
    
    if file_type == 'csv':
        data = pd.read_csv(fr"{clear_path}")
    elif file_type == 'json':
        data = pd.read_json(fr"{clear_path}")
    elif file_type == 'xlsx':
        data = pd.read_excel(fr"{clear_path}")
    elif file_type == 'hdf':
        data = pd.read_hdf(fr"{clear_path}")
    elif file_type == 'parquet':
        data = pd.read_parquet(fr"{clear_path}")
    elif file_type == 'html':
        data = pd.read_html(fr"{clear_path}")
    elif file_type == 'xml':
        data = pd.read_xml(fr"{clear_path}")
    elif file_type == 'feather':
        data = pd.read_feather(fr"{clear_path}")
    elif file_type == 'stata':
        data = pd.read_stata(fr"{clear_path}")
    elif file_type == 'sas':
        data = pd.read_sas(fr"{clear_path}")
    elif file_type == 'orc':
        data = pd.read_orc(fr"{clear_path}")
    elif file_type == 'clipboard':
        data = pd.read_clipboard()
    else:
        print(Fore.RED+"Bu tip fayl dəstəklənmir.")
        
    
    print(f"{Fore.GREEN}+Fayl uğurla oxundu:\n\n{data}")   
    return data,clear_path
   except :
     print(Fore.RED + "Xeta! Fayl Movcud Deyil!")
      

  
  
    
 
def numeric_data_analiz(data):
    numeric_data = data.select_dtypes(include=[np.number])
    print(f"{numeric_data.mean()}")
     
       
def general_analysis(data):
    print(f"{data.describe()}")
    
    
def median_analiz(data):
    numeric_data = data.select_dtypes(include=[np.number])
    print(f"{numeric_data.median()}")
     
    
def null_to_zero(data, clear_path):
    data.fillna(0,inplace=True)
    data.to_csv(clear_path, index = False)
    print(Fore.GREEN+"Emeliyyat Ugurla Bitti!")
    
def null_to_previous(data, clear_path):
    data.ffill(inplace=True)
    data.to_csv(clear_path, index = False)
    print(Fore.GREEN+"Emeliyyat Ugurla Bitti!")
   
def null_to_next(data, clear_path):
    data.bfill(inplace=True)
    data.to_csv(clear_path, index = False)
    print(Fore.GREEN+"Emeliyyat Ugurla Bitti!")

    
data,clear_path = file_read()
stop = True
while stop:
    stop =menu(data,clear_path)