palabra = input().strip()
objetivo = "TAP"
resultado = "S"

for letra in objetivo:
    pos = palabra.find(letra)
    if pos == -1:
        resultado = "N"
        break
    else:
        palabra = palabra[pos+1:]

print(resultado)