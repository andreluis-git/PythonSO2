import os

f = os.open("pratica3.txt", os.O_RDWR)
r = os.read(f,22)
print(r)
os.close(f)
