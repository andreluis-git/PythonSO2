import os

os.system("touch pratica3.txt")
f = os.open("pratica3.txt", os.O_RDWR|os.O_CREAT)
os.write(f, "Texto pratica 3".encode())
os.close(f)
