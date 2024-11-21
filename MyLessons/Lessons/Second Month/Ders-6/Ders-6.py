# Lazımi kitabxanaları daxil et
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

# Təsadüfi ədədlərin eyni qaydada yaradılması üçün toxum təyin et
np.random.seed(42)

# 1. Verilənləri yarat
# Sahə üçün təsadüfi ədədlər (50-dən 200-ə qədər kvadrat metr)
Saha = np.random.randint(50, 200, 100)

# Mərtəbə sayı üçün təsadüfi ədədlər (1-dən 10-a qədər)
Mertebe = np.random.randint(1, 10, 100)

# Rayon üçün təsadüfi seçimlər (1 - Bakı, 2 - Sumqayıt, 3 - Gəncə)
Rayon = np.random.choice([1, 2, 3], 100)

# Qiymət: Sadə xətti modelə əsaslanan təsadüfi qiymətlər
# Qiymət (AZN) = Sahə x 500 + Mərtəbə x 1000 + Rayon x 10000 + təsadüfi dəyişkənlik
Qiymet = (
    500 * Saha + 1000 * Mertebe + Rayon * 10000 + np.random.randint(-5000, 5000, 100)
)

# 2. Verilənləri pandas DataFrame formatına çevir
data = pd.DataFrame(
    {"Sahə": Saha, "Mərtəbə": Mertebe, "Rayon": Rayon, "Qiymət (AZN)": Qiymet}
)

# Giriş xüsusiyyətlərini (X) və çıxışı (y) ayır
X = data[['Sahə', 'Mərtəbə', 'Rayon']]  # Xüsusiyyətlər
y = data['Qiymət (AZN)']  # Hədəf dəyişəni

# 3. Verilənləri təlim və test dəstlərinə böl
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model qur və təlim et
# Xətti Reqressiya modelini yarat
model = LinearRegression()

# Təlim məlumatları üzərində modeli öyrət
model.fit(X_train, y_train)

# Test məlumatları üçün qiymətləndirmə proqnozları al
y_pred = model.predict(X_test)

# 5. Nəticələri vizuallaşdır
plt.figure(figsize=(10, 5))  # Şəkilin ölçüsünü təyin et
plt.scatter(y_test, y_pred)  # Faktiki və proqnoz qiymətləri göstəricilər olaraq çək
plt.xlabel("Faktiki Qiymət")  # X oxu üçün etiket
plt.ylabel("Proqnoz Olunan Qiymət")  # Y oxu üçün etiket
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linewidth=2)  # Müqayisə xətti
plt.show()  # Şəkli göstər
