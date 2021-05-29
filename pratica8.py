import subprocess as sp

p = sp.Popen(args=['python3', './filhoDoP8.py'], stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE)

p_in = "Pai do filho"

p_out = p.communicate(input=p_in.encode('utf-8'))

if p.returncode == 0:
	print("Sucesso - ", str(p_out[0], 'utf-8'))
else:
	print("Falha - ", str(p_out[1], 'utf-8'))
