#!/usr/bin/env python
# _*_ coding=utf-8 _*_

import socket
import struct
import binascii

rawSocket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))

def is_odd(n):
    if n==192:
       return n  
t = filter(is_odd, [192,127,168])
n = list(t)

pkt = rawSocket.recvfrom(2048)
print("pkt:")
print(pkt)

ethernetHeader = pkt[0][0:14]   #提取以太网帧头
print("ethernetheader: " )
print(ethernetHeader)
eth_hdr = struct.unpack("!6s6s2s",ethernetHeader) #6字节目的mac地址，6字节源mac地址，2字节协议类型
print("eth_hdr:" )
print(eth_hdr)

binascii.hexlify(eth_hdr[0])
binascii.hexlify(eth_hdr[1])
binascii.hexlify(eth_hdr[2])

ipHeader = pkt[0][14:34]        #提取IP协议头，不包含option和padding字段。
print("ip header: ")
print(ipHeader)
ip_hdr = struct.unpack("!12s4s4s",ipHeader)         # ！标示转换网络字节序，前12字节为版本、头部长度、服务类型、总长度、标志等其他选项，后面的两个四字节依次为源IP地址和目的IP地址。

print(ip_hdr)

print ("source IP address: "+ socket.inet_ntoa(ip_hdr[1]))

print ("destination IP address: " + socket.inet_ntoa(ip_hdr[2]))

tcpHeader = pkt[0][34:54]
print("tcp header: ")
print(tcpHeader)
tcp_hdr = struct.unpack("!HH16s",tcpHeader)
print("tcp_hdr:")
print (tcp_hdr)

