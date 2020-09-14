import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

arr=np.convolve([1,1,1,1,1], [0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1])
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('test')
n=np.arange(21)
plt.stem(n, arr)
plt.show()

numerator=[.008,-.033,.05,-.033,.008]
denominator=[1,2.37,2.7,1.6,.41]
w,h=signal.freqz(numerator,denominator)
fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)

plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [rad/sample]')

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
plt.plot(w, angles, 'g')
plt.ylabel('Angle (radians)', color='g')
plt.grid()
plt.axis('tight')
plt.show()

plt.show()
