a, b = int(input()), int(input())  
print(*[i for i in range(a, b) if i % 2 == 0])
