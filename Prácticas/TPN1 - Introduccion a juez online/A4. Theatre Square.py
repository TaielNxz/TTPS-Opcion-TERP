import math

n, m, a = map(int, input().split())

lados_n = math.ceil(n / a)
lados_m = math.ceil(m / a)

total_losas = lados_n * lados_m

print(total_losas)