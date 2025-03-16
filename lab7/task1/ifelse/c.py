a = int(input()) 
b = int(input()) 
if a // 1000 > 1 and a // 1000 < 10: 
    a = str(a) 
    if a[0] == a[3] and a[1] == a[2] and b == 1: 
        print("Yes") 
    else: 
        print("Yes")
else:
    print("No")    