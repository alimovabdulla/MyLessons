import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
np.random.seed(42)

# Xüsusiyyətləri yarat
Saha = np.random.randint(50, 200, 100)  # Sahə (kv.m)
Mertebe = np.random.randint(1, 10, 100)  # Mərtəbə sayı
Rayon = np.random.choice([1, 2, 3], 100)  # Rayon (1 - Bakı, 2 - Sumqayıt, 3 - Gəncə)

# Qiymət: Sadə xətti modelə əsaslanır
Qiymet = (
    500 * Saha + 1000 * Mertebe + Rayon * 10000 + np.random.randint(-5000, 5000, 100)
)

# DataFrame formatına çevir
data = pd.DataFrame(
    {"Sahə": Saha, "Mərtəbə": Mertebe, "Rayon": Rayon, "Qiymət (AZN)": Qiymet}
)

X = data[['Sahə','Mərtəbə','Rayon']]
y = data["Qiymət (AZN)"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)

plt.figure(figsize=(10,5))
plt.scatter(y_test,y_pred)
plt.plot([y.min(),y.max()],[y.min(),y.max()],color='red')
plt.xlabel("Faktiki Qiymet")
plt.ylabel("Proqnoz Qiymet")
plt.title("Faktiki Ve Proqnoz")
plt.show()