def bolme_emeliyyati(sayi1, sayi2):
    if sayi1 == 0 and sayi2 == 0:
        raise ValueError("Ededlerin ikisi də 0-dır")
    try:
        netice = sayi1 / sayi2
    except ZeroDivisionError:
        print("Xeta: Eded 0-a bolunmur!")
    else:
        print(f"Netice: {netice}")

 
bolme_emeliyyati(10, 2)

try:
    # Xətaya səbəb ola biləcək kod
    number = int(input("Bir rəqəm daxil edin: "))  # İstifadəçi rəqəm daxil etməzsə səhv olacaq
    result = 100 / number  # Sıfıra bölünmə xətası ola bilər
    print(f"Nəticə: {result}")

except ValueError:
    # Əgər istifadəçi rəqəm yerinə mətn daxil etsə, bu səhv yaranacaq
    print("Xəta: Rəqəm daxil etməlisiniz!")

except ZeroDivisionError:
    # Əgər istifadəçi sıfır daxil edərsə, sıfıra bölünmə xətası baş verəcək
    print("Xəta: Sıfıra bölmək mümkün deyil!")

except Exception as e:
    # Yuxarıda qeyd edilməyən digər bütün xətalar bu blokda idarə olunacaq
    print(f"Başqa bir xəta baş verdi: {e}")

finally:
    # Bu blok hər zaman işləyəcək, istər xəta olsun, istər olmasın
    print("Proqram bitdi.")


####################################################################



import pandas as pd

# 1. read_csv() – CSV faylını oxumaq
df = pd.read_csv('data.csv')

# 2. head() – İlk n sətiri göstərmək
print(df.head(10))  # İlk 10 sətiri göstər

# 3. info() – DataFrame haqqında ümumi məlumat
df.info()

# 4. describe() – Statistik məlumatlar (ortalama, minimum, maksimum və s.)
print(df.describe())

# 5. sort_values() – Verilənləri sıraya salmaq
df_sorted = df.sort_values(by='Age')  # 'Age' sütununa görə sırala
print(df_sorted.head())

# 6. iloc[] və loc[] – İndekslərə və sütun adlarına əsasən verilənlərə müraciət
# İlk 5 sətri və bütün sütunları seç
print(df.iloc[:5, :])
# İlk 10 sətrin 'Age' və 'Name' sütunlarını seç
print(df.loc[:9, ['Age', 'Name']])

# 7. dropna() – Boş dəyərləri silmək
df_cleaned = df.dropna()  # Boş dəyərləri sil
print(df_cleaned)

# 8. fillna() – Boş dəyərləri doldurmaq
df_filled = df.fillna(0)  # Boş olan dəyərləri 0 ilə doldur
print(df_filled)

# 9. groupby() – Məlumatları qruplaşdırmaq
grouped = df.groupby('Department')['Salary'].mean()  # 'Department' sütununa görə qruplaşdır və 'Salary' üçün ortalama hesabla
print(grouped)

# 10. apply() – Funksiyanı hər sətirə və ya sütuna tətbiq etmək
df['New Salary'] = df['Salary'].apply(lambda x: x * 1.1)  # 'Salary' sütununa 10% artım tətbiq et
print(df.head())

# 11. merge() – İki DataFrame-i birləşdirmək (JOIN əməliyyatı)
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ali', 'Ayşe', 'Ahmet']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Salary': [1000, 1500, 2000]})
merged_df = pd.merge(df1, df2, on='ID')  # 'ID' sütununa görə birləşdir
print(merged_df)

# 12. pivot_table() – Pivot cədvəli yaratmaq
pivot = df.pivot_table(values='Salary', index='Department', columns='Year', aggfunc='mean')  # Pivot cədvəli yarat
print(pivot)

# 13. value_counts() – Unikal dəyərlərin sayını hesablamaq
value_counts = df['Department'].value_counts()  # 'Department' sütunundakı dəyərlərin sayını hesabla
print(value_counts)

# 14. to_csv() – DataFrame-i CSV faylı kimi saxlamaq
df.to_csv('output.csv', index=False)  # DataFrame-i CSV faylı olaraq saxla

# 15. drop() – Sətir və ya sütunları silmək
df_dropped = df.drop(columns=['Age'])  # 'Age' sütununu sil
print(df_dropped)

# 16. duplicated() və drop_duplicates() – Təkrarlanan dəyərləri yoxlamaq və silmək
duplicates = df.duplicated()  # Təkrarlanan sətirləri yoxla
print(duplicates)
df_no_duplicates = df.drop_duplicates()  # Təkrarlanan sətirləri sil
print(df_no_duplicates)

# 17. replace() – Məlumatı başqa bir dəyərlə əvəz etmək
df_replaced = df.replace({'Department': {'HR': 'Human Resources'}})  # 'HR' dəyərini 'Human Resources' ilə əvəz et
print(df_replaced)

# 18. concat() – İki və ya daha çox DataFrame-i birləşdirmək
df3 = pd.concat([df1, df2], axis=0)  # İki DataFrame-i birləşdir (sətir üzrə)
print(df3)

# 19. astype() – Sütunların verilən növünü dəyişdirmək
df['Salary'] = df['Salary'].astype(float)  # 'Salary' sütununu float növünə çevir
print(df.dtypes)

# 20. reset_index() – DataFrame-in indeksini sıfırlamaq
df_reset = df.reset_index(drop=True)  # İndeksi sıfırla
print(df_reset)
