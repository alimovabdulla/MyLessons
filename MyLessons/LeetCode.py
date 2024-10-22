from numpy import number
import pandas as pd
import numpy as np
def menu():
    data = file_read()
    button = int(input("Regemsal Deyerlerin ortalama Analizi ucun 1\nUmumi Analiz ucun 2\n:"))
    if button==1:
        numeric_data_analiz(data)
    elif button == 2:
        general_analysis(data)  
    elif button == 3:
        medium_analiz(data)
        
def file_read():
    file_type = input("Faylın tipini qeyd edin (csv, json, xlsx, hdf, parquet, html, xml, feather, stata, sas, orc, clipboard)\n: ") 
    file_path = input("Faylın yolunu yazın (quotes olmadan)\n: ")
    # if '"' in file_path:
    #     file_path.remo
    data = None
    
    if file_type == 'csv':
        data = pd.read_csv(fr"{file_path}")
    elif file_type == 'json':
        data = pd.read_json(fr"{file_path}")
    elif file_type == 'xlsx':
        data = pd.read_excel(fr"{file_path}")
    elif file_type == 'hdf':
        data = pd.read_hdf(fr"{file_path}")
    elif file_type == 'parquet':
        data = pd.read_parquet(fr"{file_path}")
    elif file_type == 'html':
        data = pd.read_html(fr"{file_path}")
    elif file_type == 'xml':
        data = pd.read_xml(fr"{file_path}")
    elif file_type == 'feather':
        data = pd.read_feather(fr"{file_path}")
    elif file_type == 'stata':
        data = pd.read_stata(fr"{file_path}")
    elif file_type == 'sas':
        data = pd.read_sas(fr"{file_path}")
    elif file_type == 'orc':
        data = pd.read_orc(fr"{file_path}")
    elif file_type == 'clipboard':
        data = pd.read_clipboard()
    else:
        print("Bu tip fayl dəstəklənmir.")
        
    return data 
    print("Fayl uğurla oxundu")
    
 
def numeric_data_analiz(data):
    numeric_data = data.select_dtypes(include=[np.number])
    print(numeric_data.mean())
       
def general_analysis(data):
    print(data.describe())
    
def medium_analiz(data):
    numeric_data = data.select_dtypes(include=[np.number])
    print(numeric_data.median())
    

menu()