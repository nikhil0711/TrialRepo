from matplotlib import pyplot as plt
import numpy as np

x=np.arange(12)
y=np.random.randn(12)

plt.plot(x,y,marker="o",label="Random")
plt.legend()
plt.show()
