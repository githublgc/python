import socket
import ssl

class safeclient:
    def connect(self):
        # 上下文context
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        # 加载信任根证书
        ctx.load_verify_locations('certandkey/ca.crt')

        # 请求和服务器建立连接
        with socket.create_connection(('127.0.0.1', 8050)) as sock1:
            # 将socket转换成SSL加密的safe socket
            with ctx.wrap_socket(sock1, server_hostname='server') as safesock:
            #server_hostname是服务器里面CN：constant name的名字server
                # 向服务端发送信息
                message1 = "hello i am client!!".encode("utf-8")
                safesock.send(message1)
                # 接收服务端发送的信息
                message2 = safesock.recv(1024).decode("utf-8")
                print(f"接收到服务器的消息为 : {message2}")
                safesock.close()

if __name__ == "__main__":
    client = safeclient()
    client.connect()
