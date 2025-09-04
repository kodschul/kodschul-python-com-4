import matplotlib.pyplot as plt
import numpy as np

x = list(np.arange( 10))
y = [1,2,10,5, 5,6,7,8,9,2]

plt.plot(x, y) 
plt.title("Entwicklung")
plt.xlabel("Zeit")
plt.ylabel("Werte")
plt.show()