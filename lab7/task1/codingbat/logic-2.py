def make_bricks(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - (5 * big)
    else:
        remainder = goal % 5
        
    return small >= remainder 
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
    
def fix_teen(n):
    if 13 <= n and n <= 19 and n != 15 and n!= 16:
        return 0
            
    return n 

def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
        
    if remainder <= small:
        return remainder
        
    return -1 

def lone_sum(a, b, c):
    s = 0
    if a != b and a != c:
        s += a
            
    if b != a and b != c:
        s += b
                      
    if c != a and c != b:
        s += c
        
    return s 

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
    
def round10(num):
    if num % 10 < 5:
        return num - (num % 10)
        
    return num + (10 - num % 10) 

def lucky_sum(a, b, c):
    if a == 13:
        return 0
        
    if b == 13:
        return a
                
    if c == 13:
        return a + b
                          
    return a + b + c 

def close_far(a, b, c):
    return (is_close(a, b) and is_far(a, b, c)) 
        
def is_close(a, b):
    return abs(a - b) <= 1
    
def is_far(a, b, c):
    return abs(a - c) >= 2 and abs(b - c) >= 2