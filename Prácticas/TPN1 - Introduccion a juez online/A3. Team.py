n = int(input())

contador = 0
for _ in range(n):
    opiniones = input()
    if opiniones.split().count("1") >= 2:
        contador += 1

print(contador)