from a import getmenu
from b import copyfile
if __name__ == "__main__":
    
    getmenu()
    file1=open('test1.txt',mode='r',encoding='utf-8')#用读取方式打开test1.txt文本
    file2=open('test2.txt',mode='w',encoding='utf-8')#用写入方式打开test2.txt文本 test2.txt是需要复制的文件夹
    copyfile(file1,file2)
