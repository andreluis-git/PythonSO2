import sys

try:
	dado = sys.stdin.readline();
	print("Dados do pai: ", dado)
	exit(0)
except Exception as e:
	syste.stderr.write(str(e) + "\n")
	exit(1)
