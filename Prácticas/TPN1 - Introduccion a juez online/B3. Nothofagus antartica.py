n = int(input())

coordenadas_x = []
coordenadas_y = []

for _ in range(n):
		x, y = map(int, input().split())
		coordenadas_x.append(x)
		coordenadas_y.append(y)

xmin, xmax = min(coordenadas_x), max(coordenadas_x)
ymin, ymax = min(coordenadas_y), max(coordenadas_y)
		
ancho = (xmax - xmin) + 2
alto = (ymax - ymin) + 2

perimetro = 2 * (ancho + alto)

print(perimetro)