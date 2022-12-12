import string
print(int(2))
print(chr(65+0))
fonks_dekryp= lambda mo: ''.join(chr(65+int(mo[i])) for i in range(len(mo)))
print(fonks_dekryp("1-2"))