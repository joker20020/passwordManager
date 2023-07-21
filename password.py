from Crypto.Cipher import AES
from random import randbytes


class PWcontroller():
    def __init__(self,key):
        self.encryptor = AES.new(key,AES.MODE_ECB)
        self.decryptor = AES.new(key,AES.MODE_ECB)

    @staticmethod
    def padding(password):
        password = password.encode("utf-8")
        tail = 16-len(password)%16
        if tail != 0 :
            password += randbytes(tail)
        return tail,password

    def encrypt(self,pw:str):
        tail,pw = self.padding(pw)
        return tail,self.encryptor.encrypt(pw).hex()

    def decrypt(self,pw:str):
        pw = bytes.fromhex(pw)
        return self.decryptor.decrypt(pw)

