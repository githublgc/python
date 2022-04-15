import numpy as np
from matplotlib import pyplot as plt
from math import *
from scipy import signal
List1 = [1,5,2,3,4]
List2 = [(3+0j),
         (-0.05278640450004221+0.07265425280053583j),
         (-0.9472135954999579+0.3077683537175256j),
         (-0.9472135954999579-0.307768353717525j),
         (-0.052786404500041684-0.07265425280053595j)]
a = [1,0,2,3,0]
def ifft1(b):
    N = len(b)
    f = []
    for k in range(N):
        F = 0
        for m in range(N):
            F += b[m] * e**(2j * pi * (m*k) / N)/N
        f.append(F)
    
    return f

def conv(lst1,lst2):
    print(signal.convolve(lst1,lst2))  #卷积实现


List3=conv(List1,List2)

#print(List3)
plt.plot([0,1,2,3,4],a)
plt.show()
