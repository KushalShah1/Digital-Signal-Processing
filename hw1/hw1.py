import numpy as np
import matplotlib.pyplot as plt
arr=np.convolve([1,1,1,1,1], [0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1])
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('test')
n=np.arange(21)
plt.stem(n, arr)
plt.show()