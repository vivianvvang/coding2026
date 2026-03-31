from typing import List, Optional

class IPv4Iterator:
    def __init__(self, startIp: str):
        self.MAX_IP = self._ip_to_long("255.255.255.255")
        self.current = self._ip_to_long(startIp)

    def hasNext(self, ) -> bool:
        return self.current <= self.MAX_IP

    def next(self, ) -> str:
        ip = self._long_to_ip(self.current)
        self.current += 1
        return ip
    
    def _ip_to_long(self, ip):
        secs = ip.split(".")
        res = 0
        for sec in secs:
            res = res * 256 + int(sec)
        return res
    
    def _long_to_ip(self, val):
        num = val
        ip = ""
        for i in range(4):
            ip = "." + str(num % 256) + ip
            num = num // 256
        return ip[1:]

