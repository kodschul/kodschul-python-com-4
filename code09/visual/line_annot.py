import matplotlib.pyplot as plt
import numpy as np

x = [1, 2,3,4]
y = range(0, 20, 5)

plt.figure(figsize=(16, 4))

plt.plot(x, y) 
plt.title("Entwicklung")

plt.xticks(x, labels=["Q1", "Q2", "Q3", "Q4"])
plt.xlabel("Zeit")
plt.ylabel("Werte")



i = 0
for value in x: 
    plt.text(x[i], y[i], f"Q{x[i]}={y[i]}", ha="center")
    i+=1



plt.show()