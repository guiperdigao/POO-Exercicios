import string

f = open("entrada.txt", "r")
linhas = f.readlines()
f.close()

last = len(linhas)-1
rev = linhas[last::-1]

g = open("entrada-inversa.txt", "w")
for v in rev:
    g.write(v)
g.close()
print(linhas)
print(rev)