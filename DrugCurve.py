import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(0,24,100)
y=6600*(np.exp(-0.1155*x)-np.exp(-0.1386*x))
z=np.full(x.size,400) #[400,400,...400] 和x等长

plt.figure()
plt.plot(x,y,color="black",linewidth=3)
plt.plot(x,z,"or--",markersize=2)
plt.xlabel("time/h")
plt.ylabel("amount/mg")
plt.plot()
plt.show()