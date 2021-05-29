import os

print(os.getcwd())
os.mkdir("TEMPORARIO")
os.chdir("TEMPORARIO")
print(os.getcwd())
os.chdir("..")
os.rmdir("TEMPORARIO")
print(os.getcwd())
