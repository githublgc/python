panduan=eval(input('输入判断：'))
if panduan==1:  #模式1：计算器
    x=int (input('操作数1：'))
    y=int (input('操作数2：'))
    # r=eval(x+y)
    print (x+y)
elif panduan==2:    #模式二：随机点名
        import random
        stu=['lili','zhayao','yangmi','liuyan']
        sex=random.choice(stu)
        print("jintianshejing",sex)


elif panduan==3 :
            print("不存在这样的模式")
