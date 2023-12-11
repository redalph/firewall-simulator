import random
import sys

class Computer:
    name = ''
    ip_address = '000.000.000.000'
    supported_protocols = []
    ports = []
    life_of_package = 0
    is_protected = False
    is_allowed = False

    def __init__(self, name):
        self.__name__ = name
        #прописать геттеры и сеттеры для значений

    def gen_ip(self):
        self.ip_address = f"{random.randint (1, 255)}.{random.randint (1, 255)}.{random.randint (1, 255)}.{random.randint (1, 255)}"
