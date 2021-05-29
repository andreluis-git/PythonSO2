import os

os.system("touch /home/usuario/arquivoP1")
os.chown('/home/usuario/arquivoP1', 1000, 4)
os.chmod('/home/usuario/arquivoP1', 774)
