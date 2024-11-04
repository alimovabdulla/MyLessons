import pandas as pd

# ================================
# 1. pd.cut() funksiyası
# ================================

# Sayısal bir məlumatlar listesi
məlumatlar = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]

# pd.cut() funksiyası ilə məlumatları intervallara bölək
# Bu nümunədə, `bins` ilə xüsusi intervallar təyin edirik.
# `labels` isə hər interval üçün ad verir.
kateqoriyalar = pd.cut(məlumatlar, bins=[0, 20, 40, 60, 80, 100], labels=["Çox Aşağı", "Aşağı", "Orta", "Yüksək", "Çox Yüksək"])

print("pd.cut() funksiyasının nəticəsi:")
print(kateqoriyalar)
# Nəticə: Kateqoriyalara uyğun olaraq hər bir məlumatın hansı aralığa düşdüyünü göstərir.
print("\n")

# ================================
# 2. pd.merge() funksiyası
# ================================

# İki fərqli DataFrame yaradaq
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Ad': ['Ali', 'Nigar', 'Əli', 'Aytac']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 5, 6],
    'Yaş': [25, 30, 35, 40]
})

# `pd.merge()` funksiyası ilə iki DataFrame'i birləşdirək
# Burada `on='ID'` parametri ilə `ID` sütunu əsasında birləşdiririk.
birləşmiş_df = pd.merge(df1, df2, on='ID', how='inner')
# `how='inner'` - yalnız hər iki cədvəldə olan ortaq ID-ləri gətirir.

print("pd.merge() funksiyasının nəticəsi:")
print(birləşmiş_df)
# Nəticə: Ortada kəsişən ID-lər üzrə `df1` və `df2` birləşdirilir.
print("\n")

# ================================
# 3. pd.join() funksiyası
# ================================

# İki fərqli DataFrame yaradaq və onları indekslərlə birləşdirəcəyik
df_left = pd.DataFrame({
    'Ad': ['Ali', 'Nigar', 'Əli'],
    'Yaş': [25, 30, 35]
}, index=['A', 'B', 'C'])

df_right = pd.DataFrame({
    'Şəhər': ['Bakı', 'Gəncə', 'Sumqayıt']
}, index=['A', 'B', 'D'])

# `pd.join()` funksiyası ilə sol və sağ cədvəlləri indekslər əsasında birləşdirək
birləşmiş_df_join = df_left.join(df_right, how='outer')
# `how='outer'` - hər iki DataFrame-dən bütün satırları gətirir, uyğun olmayanlar `NaN` olur.

print("pd.join() funksiyasının nəticəsi:")
print(birləşmiş_df_join)
# Nəticə: İndekslərə əsaslanaraq `df_left` və `df_right` birləşdirilir.

