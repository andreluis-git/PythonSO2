import subprocess as sp

p = sp.call(['sh teste.sh'], shell=True)

if p == 0:
	print("OK")
else:
	raise Exception("Erro")
