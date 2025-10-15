a, b, c = map(int, input().split())

resto = b - a

if resto % c == 0:
    print("S")
else:
    print("N")