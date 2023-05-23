import socket
import ssl
import http.server as hs
import sys, os


class safeserver:
    def listenclient(self):
        # ctx:context,SSL上下文
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        # server所用证书和私钥
        ctx.load_cert_chain('certandkey/server.crt', 'certandkey/server_rsa_private.pem.unsecure')

        # 监听端口
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock1:
            sock1.bind(('127.0.0.1', 8050))
            sock1.listen(5)#listen(n)传入的值, 5是一个常用值
            #n表示的是服务器拒绝(超过限制数量的)连接之前，操作系统可以挂起的最大连接数量。
            #n也可以看作是"排队的数量"

            # 将socket转换为SSL加密后的safesocket
            with ctx.wrap_socket(sock1, server_side=True) as safesock:
                while True:
                    # 和客户端建立连接
                    client_socket, addr = safesock.accept()
                    # 接收客户端传来消息：client to server
                    messagectos = client_socket.recv(1024).decode("utf-8")
                    print(f"接收到来自客户端的消息 {addr}：{messagectos}")
                    # 服务器server向客户端发送信息server to client
                    messagestoc = f"hello,i am server!".encode("utf-8")
                    client_socket.send(messagestoc)
                    client_socket.close()

class RequestHandler(hs.BaseHTTPRequestHandler):
    
    def send_content(self, page, status = 200):
        
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(bytes(page, encoding = 'utf-8'))
        print(page)
    
    def do_GET(self):
      
        
            
            #获取文件路径
            full_path = os.getcwd() + self.path
                 
            #如果该路径是一个文件    
            if os.path.isfile(full_path):
            
                self.handle_file(full_path)
        
           
 
    
    def handle_file(self, full_path):
        
        
            
            with open(full_path, 'r') as file:
                
                content = file.read()
                
                
            self.send_content(content,200)
            
        
if __name__ == "__main__":
    a=eval(input("输入数字，选择和浏览器(0)交互还是和客户端(1)进行交互"))
    print("每次只选其中一个，如需更换需要关闭终端重新进入选择")
    if a==0:
        print("在浏览器中输入http://127.0.0.1:8040/index.html")
    
        httpAddress = ('', 8040)
    
        httpd = hs.HTTPServer(httpAddress, RequestHandler)
    
        httpd.serve_forever()
    if a==1:
        print("另一个终端打开客户端")
        server = safeserver()
        server.listenclient()
        
