 # NumPy və Matplotlib kitabxanalarını daxil edirik
import numpy as np  # NumPy böyük və çoxölçülü massivlər üzərində işləmək üçün istifadə olunur
import matplotlib.pyplot as plt  # Matplotlib qrafiklər çəkmək üçün istifadə olunur

# 1. NumPy Massivlərinin Yaradılması
array1 = np.array([1, 2, 3, 4])  # Bu, bir ölçülü massivdir (1D array)
array2 = np.array([[1, 2, 3], [4, 5, 6]])  # Bu isə iki ölçülü massivdir (2D array)

# Massivlərin yaradılmasından sonra bir neçə riyazi əməliyyatları yerinə yetirək:

# 2. Riyazi Əməliyyatlar
print("Cəmləmə:", array1 + 5)  # Hər bir elementə 5 əlavə edir: [1+5, 2+5, 3+5, 4+5] → [6, 7, 8, 9]
print("Çıxma:", array1 - 2)  # Hər bir elementdən 2 çıxır: [1-2, 2-2, 3-2, 4-2] → [-1, 0, 1, 2]
print("Vurma:", array1 * 3)  # Hər bir elementi 3-ə vurur: [1*3, 2*3, 3*3, 4*3] → [3, 6, 9, 12]
print("Toplama:", np.sum(array2))  # Bütün elementləri toplar: 1+2+3+4+5+6 → 21
print("Orta qiymət:", np.mean(array2))  # Elementlərin orta qiymətini tapır: (1+2+3+4+5+6) / 6 → 3.5
print("Matris vurma:", np.dot(array2, array2.T))  
# Matrislərin vurulması (2D massivlər üçün): array2 ilə onun transpozunu (T) vurur, nəticədə yeni matris yaranır

# 3. Təsadüfi Ədədlərlə Massiv Yaratmaq
# np.random.rand() funksiyası ilə 0 və 1 arasında təsadüfi ədədlərdən ibarət massiv yaradırıq
random_array = np.random.rand(3, 3)  # 3x3 ölçüsündə təsadüfi massiv
print("Təsadüfi massiv:", random_array)

# 4. Matplotlib ilə Vizualizasiya
# İndi sadə bir xətt qrafiki yaradacağıq

# X dəyişəni üçün 0-dan 10-a qədər 100 ədəd bərabər məsafəli nöqtə yaradırıq
x = np.linspace(0, 10, 100)  # linspace funksiyası ardıcıl nöqtələr yaradır

# Y dəyişəni üçün isə sin(x) funksiyasını istifadə edirik, bu sin(x) dəyərləri xətt şəklində təsvir edəcək
y = np.sin(x)  # sin(x) funksiyası hər bir x dəyəri üçün sinus hesablayır

# plt.plot() funksiyası ilə qrafiki çəkirik
plt.plot(x, y, label="sin(x)", color="blue")  # X və Y dəyərlərini veririk, etiket və rəng seçirik
plt.xlabel("X oxu")  # X oxu üçün etiket
plt.ylabel("Y oxu")  # Y oxu üçün etiket
plt.title("Sinus Funksiyasının Qrafiki")  # Qrafik üçün başlıq
plt.legend()  # Qrafikdə etiketləri göstərir
plt.show()  # Qrafiki göstərir
