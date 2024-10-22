import pandas as pd
import numpy as np

# CSV faylını yüklə
df = pd.read_csv(r"C:\Users\ASUS\Desktop\output.csv")

# Yalnız rəqəmsal dəyərləri olan sütunları seçirik
numeric_df = df.select_dtypes(include=[np.number])

# NaN dəyərlərini 0 ilə doldururuq (lazım olarsa)
numeric_df.fillna(0, inplace=True)

# Hər rəqəmsal sütunun orta dəyərlərini hesablamaq
mean_values = numeric_df.mean()
 
# Nəticələri çap edirik
print("Sütunların ortalama dəyərləri:")
print(np.min(numeric_df))
