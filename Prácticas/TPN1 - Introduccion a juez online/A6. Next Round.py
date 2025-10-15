n, k = map(int, input().split())
puntajes = list(map(int, input().split()))
puntaje_de_corte = puntajes[k - 1]
cant_avanzan = 0

for puntaje in puntajes:
    if puntaje >= puntaje_de_corte and puntaje > 0:
        cant_avanzan += 1

print(cant_avanzan)