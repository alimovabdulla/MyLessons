#Aşağıda Python-da istifadə olunan döngü (loop) ifadələrini qısa izahlarla təqdim edirəm:

# 1. for loop
# Bir ardıcıllıq (siyahı, tuple, string, və s.) üzərində döngü qurur.
for element in ardicil:
    print(element)  # Hər element üçün icra ediləcək kod

# 2. while loop
# Şərt doğru olduğu müddətcə döngü davam edir.
sayi = 0
while sayi < 5:
    print(sayi)  # 0-dan 4-ə qədər olan ədədləri çap edir
    sayi += 1  # sayini 1 artır

# 3. break
# Döngünü dayandırmaq üçün istifadə olunur.
for i in range(10):
    if i == 5:
        break  # i 5 olduqda döngünü dayandır
    print(i)

# 4. continue
# Döngünün cari iterasiyasını atlayıb növbəti iterasiyaya keçmək üçün istifadə olunur.
for i in range(5):
    if i == 2:
        continue  # i 2 olduqda cari iterasiyanı atla
    print(i)  # 0, 1, 3, 4 çap ediləcək

# 5. else (for və while döngüləri ilə birlikdə)
# Döngü tamamlandıqda (break olmadan) icra ediləcək kod.
for i in range(5):
    print(i)
else:
    print("Döngü tamamlandı.")  # Döngü tamamlandıqda icra ediləcək

# 6. range()
# Məlumatları müəyyən bir aralıqda döngü ilə təkrar etmək üçün istifadə olunur.
for i in range(1, 6):  # 1-dən 5-ə qədər olan ədədləri döngüləyir.
    print(i)  # 1, 2, 3, 4, 5 çap ediləcək
