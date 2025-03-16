v = int(input()) 
t = int(input()) 

if v > 0:
    n = (v * t) / 109
    s = v * t - 109 * int(n) 
    print(abs(s)) 
else: 
    n = (v * t) / 109 
    s = 109 - (-(v * t) - 109 * int(n)) 
    print(abs(s))