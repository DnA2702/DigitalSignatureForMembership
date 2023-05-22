from RSA import *
import os

fileName = "channel"
p = generatePrima()
q = generatePrima()
n = p * q
totient = (p - 1) * (q - 1)
while True:
    e = generatePrima()
    if (totient % e != 0):
        break
d = cariD(totient, e)

if (os.path.exists("%s.pub" % (fileName)) or os.path.exists("%s.pri" % (fileName))):
    False
else:
    fo = open("%s.pri" % (fileName), "w")
    fo.write("%s,%s" % (n, e))
    fo.close()

    fo = open("%s.pub" % (fileName), "w")
    fo.write("%s,%s" % (n, d))
    fo.close()
    True