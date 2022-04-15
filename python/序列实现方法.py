ls1=[1,2,3,4,5,6]
#序列初始化
print('ls1值为',ls1)

print('3的下标为',ls1.index(3))

ls1.insert(0,9)
#对应位置0插入元素9
length=eval(input('输入对应长度'))
#input一般输入一个字符串，eval可以计算对应表达式子的值
while len(ls1)<length:#计算当前长度是否和要求长度匹配
    ls1.append(0)
#循环实现后补零
print('ls1值为',ls1)
print('ls1长度',len(ls1))

#ls3=[0,9,2,3,4,5,0]
#ls4=[1,2,3,4,5,6,7]
#ls5=[0,0,0,0,0,0,0]
#ls6=[0,0,0,0,0,0,0]
#i=0
#while i<7:
    #ls5[i]=ls3[i]+ls4[i]
    #ls6[i]=ls3[i]*ls4[i]
    i=i+1
#print('加法',ls5)
#print('乘法',ls6)
