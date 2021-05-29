import os


os.system("touch arquivo1p5.txt")
file = os.open("arquivo1p5.txt", os.O_RDWR|os.O_CREAT)
os.write(file, '''
Linha 1 arquivo 1
Linha 2 arquivo 1
Linha 3 arquivo 1
Linha 4 arquivo 1
Linha 5 arquivo 1
Linha 6 arquivo 1
Linha 7 arquivo 1
Linha 8 arquivo 1
Linha 9 arquivo 1
Linha 10 arquivo 1'''.encode())
os.close(file)

os.system("touch arquivo2p5.txt")
file = os.open("arquivo2p5.txt", os.O_RDWR|os.O_CREAT)
os.write(file, '''
Linha 1 arquivo 2
Linha 2 arquivo 2
Linha 3 arquivo 2
Linha 4 arquivo 2
Linha 5 arquivo 2
Linha 6 arquivo 2
Linha 7 arquivo 2
Linha 8 arquivo 2
Linha 9 arquivo 2
Linha 10 arquivo 2'''.encode())
os.close(file)

os.system("touch arquivo3p5.txt")
f3 = os.open("arquivo3p5.txt", os.O_RDWR|os.O_CREAT)
f1 = os.open("arquivo1p5.txt", os.O_RDWR)
f2 = os.open("arquivo2p5.txt", os.O_RDWR)

r = os.read(f1,1000).decode()

linesf1 = r.splitlines()

r = os.read(f2,1000).decode()

linesf2 = r.splitlines()

string = ""
for x in range(len(linesf2)):
	string += linesf1[x]+"\n"
	string += linesf2[x]+"\n"

os.write(f3, string.encode())

os.close(f1)
os.close(f2)
os.close(f3)
