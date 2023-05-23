def copyfile(f1,f2):
    content=f1.read()
    f2.write(content)
    f1.close()#关闭文件
    f2.close()
    return ;

#1.写入信息
#message ="Hello"
#file1=open('test1.txt',mode='w',encoding='utf-8')#打开所需要写入的test1.txt文本
#file1.write(message)#写入信息
#file1.close();#关闭文件

#2.调用函数进行复制
#file1=open('test1.txt',mode='r',encoding='utf-8')#用读取方式打开test1.txt文本
#file2=open('test2.txt',mode='w',encoding='utf-8')#用写入方式打开test2.txt文本 test2.txt是需要复制的文件夹
#copyfile(file1,file2)
