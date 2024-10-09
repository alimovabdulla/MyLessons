 #Python dilində def açar sözü funksiyaları müəyyən etmək üçün istifadə olunur.
 #Funksiya bir qrup əməliyyatın adıdır və həmin əməliyyatları təkrar-təkrar
 #istifadə etmək üçün müəyyən edilir. Yəni, müəyyən bir iş görən kod
 #blokunu bir funksiyaya yığırıq və həmin funksiyanı istədiyimiz
 #yerdə çağıraraq o əməliyyatı icra edirik.

# Funksiya müəyyən edilir
def salamla():
    # Funksiyanın icra etdiyi əməliyyat
    print("Salam, Ali!")

# Funksiya çağırılır
salamla()

# Parametrlərlə funksiyanın müəyyən edilməsi
def topla(a, b):
    # İki rəqəmin cəmini qaytarır
    return a + b

# Funksiya çağırılır və nəticə ekrana yazılır
netice = topla(5, 10)
print(f"Cəm: {netice}")

# Digər bir funksiyanın müəyyən edilməsi (parametrsiz)
def vidalas():
    print("Sağ ol, Ali!")

# Funksiya çağırılır
vidalas()
