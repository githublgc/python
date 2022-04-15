from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def conv(lst1,lst2):
    print(signal.convolve(lst1,lst2))  #卷积实现      

def ifft1(b):#傅里叶逆变换
    N = len(b)
    f = []
    for k in range(N):
        F = 0
        for m in range(N):
            F += b[m] * e**(2j * pi * (m*k) / N)/N
        f.append(F)
        
def fft1(a):#傅里叶变换
    start=time.time()
    N = len(a)
    f = []
    for k in range(N):
        F = 0
        for m in range(N):
            F += a[m] * e**(-2j * pi * (m*k) / N)
        f.append(F)
    plt.plot([0,1,2,3,4,5,6,7,8,9,10,11],f)
    end=time.time()
    print("run time:",(end-start))

b, a = signal.butter(4, 100, 'low', analog=True)
w, h = signal.freqs(b, a)       # 由分子b,分母a的系数求解频率响应，w为频率，h为对应的响应。



conv([4,3,1,8], [4,3,1,8])

plt.semilogx(w, 20 * np.log10(abs(h))) 	#绘制幅频响应，频率轴取对数，幅度轴转换成dB。
plt.title('Butterworth filter')
plt.xlabel('hz')
plt.ylabel('AMP(dB)')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.axvline(100, color='red') # cutoff frequency
plt.show()



