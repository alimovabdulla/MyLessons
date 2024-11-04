from numpy import size
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\ASUS\Desktop\user_behavior_dataset.csv")
systems_count  = data["Operating System"].value_counts()
systems_count.plot(kind="bar", color="green", figaspectsize=(10,5))
plt.xlabel("Emeliyyat Sistemi")
plt.ylabel("Alis")
plt.show()