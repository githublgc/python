#Numpy傅里叶变换
import numpy as np
from matplotlib import pyplot as plt
from math import *
import time
x=[3,7,1,4,5]
a=[1,5,2,3,4]
b=[(15+0j),
   (-0.26393202250021086-0.3632712640026803j),
   (-4.73606797749979-1.5388417685876283j),
   (-4.73606797749979+1.5388417685876252j),
   (-0.26393202250020775+0.36327126400267984j)]
m=[1,8,4,5,6,10,15,9,78,63,99,10756]

'''傅里叶变换'''
def fft(x):
    start=time.time()
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    f = np.dot(M, x)
    #plt.savefig()
    plt.plot([0,1,2,3,4,5,6,7,8,9,10,11],f)
    end=time.time()
    print("run time:",(end-start))
    plt.show()
    return f
    
##########C++里没有numpy包，需要循环遍历####################
def fft1(a):
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
    plt.show()
    return f

############三角函数代替指数函数#################
def fft2(data):
    length=len(data)
    fftdata = [0+0j]*length
    print(fftdata)
    for k in range(length):
        for i in range(length):
            fftdata[k] += data[i]*(cos(-2*pi*k*i/length)+1j*sin(-2*pi*k*i/length))
    return fftdata

'''傅里叶反变换'''
def ifft1(b):
    N = len(b)
    f = []
    for k in range(N):
        F = 0
        for m in range(N):
            F += b[m] * e**(2j * pi * (m*k) / N)/N
        f.append(F)
    plt.plot([0,1,2,3,4],f)
    plt.show()
    return f

############三角函数代替指数函数#################
def ifft2(data):
    length=len(data)
    ifftdata = [0+0j]*length
    print(ifftdata)
    for k in range(length):
        for i in range(length):
            ifftdata[k] += data[i]*(cos(2*pi*k*i/length)+1j*sin(2*pi*k*i/length))/length
    return ifftdata
