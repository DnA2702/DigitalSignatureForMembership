from RSA import *
from SHA3 import *

def digitalSign(Name):
    username = Name
    with open("channel.pri", "rb") as rp:
        tmp = rp.read()
        key = str(tmp, 'utf-8').split(',')
        e = int(key[1])
        n = int(key[0])

    digitalSign = enkripsi(hash(username), e, n)
    return(digitalSign)