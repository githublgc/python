import pyDes
import socket
import threading
Des_Key = b'qwerasdf'
Des_IV = b"\x00\x00\x00\x00\x00\x00\x00\x00"
PORT = 4396
BUFF = 1024
def DesEncrypt(str):
    k = pyDes.des(Des_Key, pyDes.CBC, Des_IV, pad = None, padmode = pyDes.PAD_PKCS5)
    Encrypt_Str = k.encrypt(str)
    return Encrypt_Str
def DesDecrypt(str):
    k = pyDes.des(Des_Key, pyDes.CBC, Des_IV, pad = None, padmode = pyDes.PAD_PKCS5)
    Decrypt_Str = k.decrypt(str)
    return Decrypt_Str
def SendMessage(Sock, test):
    while True:
        SendData = input()
        encryptdata = DesEncrypt(SendData)
        print('encrypted data is ' + str(encryptdata))
        if len(SendData) > 0:
            Sock.send(encryptdata)
def RecvMessage(Sock, test):
    while True:
        Message = Sock.recv(BUFF)
        decryptdata = DesDecrypt(Message)
        if len(Message)>0:
            print("receive message:" + decryptdata.decode('utf8'))
def main():
    type = input('please input server or client:')
    if type == 'server':
        ServerSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ServerSock.bind(('127.0.0.1',PORT))
        ServerSock.listen(5)
        print("listening......")
        while True:
            ConSock,addr = ServerSock.accept()
            print('connection succeed' + '\n' + 'you can chat online')
            thread_1 = threading.Thread(target = SendMessage, args = (ConSock, None))
            thread_2 = threading.Thread(target = RecvMessage, args = (ConSock, None))
            thread_1.start()
            thread_2.start()
    elif type == 'client':
        ClientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ServerAddr = input("please input the server's ip address:")
        ClientSock.connect((ServerAddr, PORT))
        print('connection succeed, chat start!')
        thread_3 = threading.Thread(target = SendMessage, args = (ClientSock, None))
        thread_4 = threading.Thread(target = RecvMessage, args = (ClientSock, None))
        thread_3.start()
        thread_4.start()
if __name__ == '__main__':
    main()
