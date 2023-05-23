import socket

#抓捕
def sniffIpData():
    host_ip = socket.gethostbyname(socket.gethostname())            #获取IP
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)       #创建套接字、可接受协议类型为UDP、TCP、ICMP、IP
    sniffer.bind((host_ip, 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)         #设置套接字options、包装ip头部
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)          #receive all package
    recv_data, addr = sniffer.recvfrom(1500)
	s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)			# disabled promiscuous mode
    sniffer.close()
    return recv_data

#解析
def decodeIpData(package):
    ip_data = {}
    #RFC791
    ip_data['version'] = package[0] >> 4
    ip_data['headLength'] = package[0] & 0x0f           #& 按位与操作
    ip_data['DSField'] = package[1]
    ip_data['totalLength'] = (package[2] << 8) + package[3]
    ip_data['identification'] = (package[4] << 8) + package[5]
    ip_data['flag'] = package[6] >> 5
    ip_data['moreFragment'] = ip_data['flag'] & 1
    ip_data['dontFragment'] = (ip_data['flag'] >> 1) & 1
    ip_data['fragmentOffset'] = ((package[6] & 0x1f) << 8) + package[7]
    ip_data['TTL'] = package[8]
    ip_data['protocol'] = package[9]
    ip_data['headerCheckSum'] = (package[10] << 8) + package[11]
    #以IP地址形式存储
    ip_data['sourceAddress'] = "%d.%d.%d.%d" % (package[12], package[13], package[14], package[15])
    ip_data['destinationAddress'] = "%d.%d.%d.%d" % (package[16], package[17], package[18], package[19])
    ip_data['options'] = []
    #根据headerLength求出options
    if ip_data['headLength'] > 5:           #一般来说此处的值为0101，表示头长度为20字节、若超出则大于5（0101）
        temp = 5
        while temp < ip_data['headLength']:
            ip_data['options'].append(package[temp * 4] + 0)
            ip_data['options'].append(package[temp * 4] + 1)
            ip_data['options'].append(package[temp * 4] + 2)
            ip_data['options'].append(package[temp * 4] + 3)
            temp += 1
    #根据totalLength求出data
    ip_data['data'] = []
    temp = ip_data['headLength'] * 4
    while temp < ip_data['totalLength']:
        ip_data['data'].append(package[temp])
        temp += 1
    return ip_data

package = sniffIpData()
data_decode = decodeIpData(package)
# for i, k in data_decode:
#     print("%d:%d" % (i, k))
for key in data_decode.items():
    print(key)


