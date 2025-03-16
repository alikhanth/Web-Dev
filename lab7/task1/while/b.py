import math

N = int(input())

i = 2
while i <= math.isqrt(N):
    if N % i == 0:
        print(i)
        break
    i += 1
else:
    print(N)
