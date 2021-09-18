from typing import Tuple
from random import randint
import urllib.request
import socket

class UserAddress:


    def __init__(self):
        self.external_ip: str = self.__get_device_ip()
        self.port: int = self.__generate_port()
    
    def get_result(self) -> Tuple[str, int]:
        return self.external_ip, self.port

    def __get_device_ip(self) -> str:
        return urllib.request.urlopen('https://ident.me').read().decode('utf8')

    def __generate_port(self) -> int:
        port: int = randint(1000, 5000)
        return port



