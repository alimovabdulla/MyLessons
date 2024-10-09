 # 1. zip() funksiyası
# İki listin elementlərini cüt-cüt birləşdirmək üçün zip() istifadə edirik.
adlar = ['Ali', 'Veli', 'Zeynep']  # Adlar listi
yaslar = [22, 25, 20]              # Yaşlar listi

# zip() funksiyası ilə adlar və yaşları birləşdiririk
birlestirilmis = zip(adlar, yaslar)

# Nəticəni list formatında çap edirik
print(list(birlestirilmis))  # [('Ali', 22), ('Veli', 25), ('Zeynep', 20)]


# 2. enumerate() funksiyası
# Bir listin elementlərini və onların indekslərini əldə etmək üçün enumerate() istifadə edirik.
meyveler = ['alma', 'banan', 'portağal']  # Meyvelər listi

# enumerate() ilə listin üzərində iterasiya edirik
for index, meyve in enumerate(meyveler):
    # Hər meyvənin indeksini və adını çap edirik
    print(f"{index}: {meyve}")
    # Çıxış: 
    # 0: alma
    # 1: banan
    # 2: portağal


# 3. List comprehensions
# 1-dən 10-a qədər olan ədədlərin kvadratlarını yaratmaq üçün list comprehensions istifadə edirik.
kvadratlar = [x**2 for x in range(1, 11)]  # Kvadratları hesablamaq

# Nəticəni çap edirik
print(kvadratlar)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 4. while döngüsü
# 1-dən 5-ə qədər olan ədədləri çap etmək üçün while döngüsünü istifadə edirik.
sayi = 1  # Başlanğıc dəyəri

# sayi 5-dən kiçik olduğu müddətdə döngü davam edir
while sayi <= 5:
    print(sayi)  # Hazırki sayını çap edirik
    sayi += 1   # sayi dəyərini 1 artırırıq
    # Çıxış: 
    # 1
    # 2
    # 3
    # 4
    # 5
