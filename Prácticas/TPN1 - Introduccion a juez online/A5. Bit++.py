n = int(input())
x = 0

for _ in range(n):
    stmt = input()
    
    if "++" in stmt:
        x += 1
    elif "--" in stmt:
        x -= 1

print(x)