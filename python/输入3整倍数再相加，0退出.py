sum=0
while True:
    n=eval(input('输入一个整数，按0退出程序：'))
    if n==0:
        break
    if n%3!=0:
        continue
    sum=sum+n
print('所有是三倍数的整数之和为%d'%sum)
