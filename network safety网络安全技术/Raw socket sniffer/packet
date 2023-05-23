import struct


TCP_FLAG_TABLE = {0x01:"F",  0x02:"S",  0x08:"P", 
                  0x09:"FP", 0x0A:"SP", 0x10:"A",
                  0x11:"FA", 0x12:"SA", 0x18:"PA",
                  0x19:"FPA",0x1A:"SPA", 0x52:"SAE"}

class packet:

    def __init__(self, data):

        self._raw_data = data
        self._eth_hdr = self.parse_eth(data[0][0:14])
        self._ip_hdr = IpHeader(self.parse_ip(data[0][14:34]))
        self.__repr__ = self.__str__

        if self._ip_hdr.protocol == 6:
            self._l4_hdr = TcpHeader(self.parse_tcp(data[0][34:54]))


        elif self._ip_hdr.protocol == 17:
            self._l4_hdr = UdpHeader(self.parse_udp(data[0][34:42]))

    def __str__(self):
        return f"{str(self._ip_hdr)}\n{str(self._l4_hdr)}"

    @staticmethod
    def parse_eth(edata):
        return struct.unpack("!6s6sH", edata)

    @staticmethod
    def parse_ip(idata):
        return struct.unpack("!BBHHHBBH4s4s", idata)

    @staticmethod
    def parse_tcp(tdata):
        return struct.unpack("!HHLLBBHHH", tdata)

    @staticmethod
    def parse_udp(udata):
        return struct.unpack("!4H", udata)

    @staticmethod
    def parse_icmp(icdata):
        raise NotImplementedError


class TcpHeader:

    def __init__(self, raw_hdr):

        self.src_port = raw_hdr[0]
        self.dest_port = raw_hdr[1]
        self.seq_num = raw_hdr[2]
        self.ack_num = raw_hdr[3]
        self.doff_res = raw_hdr[4]
        self.flags = TCP_FLAG_TABLE[raw_hdr[5]]
        self.window = raw_hdr[6]
        self.checksum = raw_hdr[7]
        self.urg_ptr = raw_hdr[8]
        self.__repr__ = self.__str__

    def __str__(self):
        return f"Source Port: {self.src_port} Destination Port: {self.dest_port} Sequence Number: {self.ack_num} Ack Number: {self.ack_num} Flags: [{self.flags}] Window Size: {self.window}"


class UdpHeader:

    def __init__(self, raw_hdr):

        self.src_port = raw_hdr[0]
        self.dest_port = raw_hdr[1]
        self.length = raw_hdr[2]
        self.checksum = raw_hdr[3]
        self.__repr__ = self.__str__

    def __str__(self):
        return f"Source Port: {self.src_port} Destination Port: {self.dest_port} Length: {self.length} Checksum: {self.checksum}"

class IpHeader:

    def __init__(self, raw_hdr):

        self.version = raw_hdr[0]
        self.tos = raw_hdr[1]
        self.length = raw_hdr[2]
        self.id = raw_hdr[3]
        self.foff = raw_hdr[4]
        self.ttl = raw_hdr[5]
        self.protocol = raw_hdr[6]
        self.hdrchecksum = raw_hdr[7]
        self.src_ip = self.parse_ip(raw_hdr[8])
        self.dest_ip = self.parse_ip(raw_hdr[9])
        self.__repr__ = self.__str__

    def __str__(self):
        return f"{self.src_ip}->{self.dest_ip} Total Length: {self.length} TTL: {self.ttl}"

    @staticmethod
    def parse_ip(raw_ip):
        uip = struct.unpack("!4B", raw_ip)
        return f"{uip[0]}.{uip[1]}.{uip[2]}.{uip[3]}"
