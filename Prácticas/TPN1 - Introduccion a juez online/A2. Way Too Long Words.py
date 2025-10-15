n = int(input())

for _ in range(n):
    palabra = input()
    longitud = len(palabra)
    
    if longitud > 10:
        palabra = palabra[0] + str(longitud - 2) + palabra[-1]
    
    print(palabra)