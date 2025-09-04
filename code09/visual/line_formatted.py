import matplotlib.pyplot as plt
import numpy as np
import math
import json

x = list(range(0, 10, 2))
y =  [i**2 for i in x]
y2 = [i*2 for i in y]


y1_line = plt.plot(x, y, color="darkblue")
y2_line = plt.plot(x,y2, color="red") 
# plt.ylim(0, 100)
plt.xlim(0, 1)

plt.title("Entwicklung")
plt.xlabel("Zeit")
plt.ylabel("Werte")




plt.savefig("plot.jpg", dpi=300)


