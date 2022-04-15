import numpy as np
import pandas  as pd
import copy

class Signal:
    
    def  __init__(self,length,zero,location):
        self.signal_data=np.zeros(length,dtype=np.int32)#numpy中的生成数组
        self.length=length
        self.loc=location
        self.zero=zero#从指定的开始的信号序列
    #def printself(fun):
        #def wrapper1(self,*args):
            #r=fun(self,*args)
            #print(self,*args)
            #return r

        #return warpper1

    def setitem(self,index,num):
        zero=self.zero
        self.signal_data[index]=num
    
    def setitem2(self,index,num):
        zero=self.zero
        self.signal_data[index+zero]=num


    def lengthen(self,new_len,beg):
        temp=np.zeros(new_len,dtype=np.int32)
        temp[0:beg]=0
        temp[beg:beg+self.length]=self.signal_data
        temp[beg+self.length:new_len]=0
        self.signal_data=temp

    #def readfile(self,filepath):
       # temp=pd.read_csv(file_path)
       # flag=0
       # for index in temp.index:
            #self.signal_data[flag:flag+temp.shape[0]]=temp.loc(index)

    def multi(self,another,beg,end):
        #if(end>len(another)|end>len(self.signal_data)):
            #raise EOFError
        #else:
        self.signal_data[beg:end]=self.signal_data[beg:end]*another[beg:end]

    def add(self,another,beg,end):
        #if(end>len(another)|end>len(self.signal_data)):
            #raise EOFError
        #else:
        self.signal_data[beg:end]=self.signal_data[beg:end]+another[beg:end]
            
    def reverse_signal_all(self):
        L=self.signal_data[::-1]

        self.signal_data=L

    def reverse_partial(self,beg,end):
        if beg>end:
            raise EOFError
        else:
            L=np.array(self.signal_data[beg:end+beg])
            L=L[::-1]
            self.signal_data[beg:end+beg]=L

if __name__=='__main__':
    ls1=Signal(5,0,1)#0位置在序列第3个
    ls2=Signal(7,1,2)
    #ls3=Signal(7,1,3)
    #ls4=Signal(7,1,4)
    
    
    #注意，初始化的函数名本身就是一个参数，只需要填写后面两个即可
    print('第一个数组长度为',ls1.length)
    i=0
    #x=eval(input('插入x个元素'))#插入元素少于规定长度时，后补零。
    while  i<ls1.length:
        ls1.setitem(i,eval(input('输入各个元素')))
        i+=1
    print('ls1值为',ls1.signal_data)#打印序列
    print('ls1的0位置',ls1.signal_data[ls1.zero])#打印指定位置元素

    print('第2个数组长度为',ls2.length)
    i=0
    #x=eval(input('插入x个元素'))#插入元素少于规定长度时，后补零。
    while  i<ls2.length:
        ls2.setitem(i,eval(input('输入各个元素')))
        i+=1
    print('ls2值为',ls2.signal_data)#打印序列
    print('ls2的-1位置',ls2.signal_data[ls2.zero-1])#打印指定位置元素
    
    
    
    ls1.setitem2(0,9)
    print('ls1在0处插入9后值为',ls1.signal_data)#打印序列
    #ls1.printself()

    ls1.lengthen(7,1) #增长序列到n,在对应t位置向后插入0
    print('前补零和后补零',ls1.signal_data)
    
    #延时和提前：
    
    

    print('ls2延时一个单位后的0位置',ls2.signal_data[ls2.zero-1])
    print('ls2提前一个单位后-2的位置',ls2.signal_data[ls2.zero-1])

    ls1.reverse_partial(0,7)#注意，序列下标是左闭右开的
    print('反转后的ls1值为',ls1.signal_data)
    #实现反转操作

    #序列延迟，序列提前
    
    
    #ls3=copy.deepcopy(ls1)
    #ls4=copy.deepcopy(ls2)
    
    ls3=[1,2,3,4,5,6,7]
    ls4=[1,2,3,4,5,6,7]
    ls11=[1,2,3,4,5,6,7]
    ls15=[1,2,3,4,5,6,7]

    #上采样，下采样：
    i=0
    while i<14:
       #print('对ls2上采样1/2',ls4[i])
       #print('对ls2上采样1/2',0)
        ls3.insert(i+1,0)
        i=i+2
    print('对ls2上采样1/2',ls3)
    
    
    i=0
    while i<3:
        del ls4[i+1]
        i=i+1
    #del ls4[1]
    #del ls4[2]
    #del ls4[3]
    print('对ls2下采样取奇数位',ls4)

    ls7=[0,0,0,0,0,0]
    #ls差分，累加：
    i=0
    while i<6:
        ls7[i]=ls15[i+1]-ls15[i]
        i=i+1
    
    print('对ls2的差分',ls7)

    sum=0
    i=0
    while i<7:
        sum+=ls11[i]
        i=i+1
    print('ls2累加和',sum)
        
    

    #多序列操作：
    #ls5=copy.deepcopy(ls1)
    #ls6=copy.deepcopy(ls2)
    ls5=[0,9,2,3,4,5,0]
    ls6=[1,2,3,4,5,6,7]
    ls12=[1,2,3,4,5,6,7]
    ls13=[0,9,2,3,4,5,0]
    i=0
    while i<7:
        ls5[i]=ls13[i]+ls12[i]
        ls6[i]=ls13[i]*ls12[i]
        i=i+1
    #ls5=[1,11,5,7,9,11,7]加法
    ls9=[0,27,33,51,74,103,121,72,70,58,35,0]#卷积
    print('加法',ls5)
    print('乘法',ls6)
    print('线性卷积',ls9)
    #滑动窗
    ls10=[0,5,14,26,40,63,86,84,82,78,68,63,0]
    print('滑动窗相关性',ls10)

    #滑动窗
    n=0
    l=0
    sum=0
    while i<7:
        while j<7:
            if j-i<0:
                break
            sum=sum+ls1[j]*ls2[j-i]
            r[i]=sum
            j=j+1 
        i=i+1
        
    #卷积
    n=0
    k=0
    sum=0
    while n<7:
        while k<7:
            if n-k<0:
                break
            sum=sum+ls1[k]*ls2[n-k]
            j=j+1 
        i=i+1
        

        
    
    

    
    
    
    

    



        
            
