n = int(input())
numeros = list(map(int, input().split()))

pares = [i+1 for i, x in enumerate(numeros) if x % 2 == 0]
impares = [i+1 for i, x in enumerate(numeros) if x % 2 != 0]

if len(pares) == 1:
    print(pares[0])
else:
    print(impares[0])