texto = input().lower()
vocales = "aoyeui"
resultado = ""

for letra in texto:
    if letra not in vocales:
        resultado += "." + letra

print(resultado)