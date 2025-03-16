def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40  
    else:
        return 40 <= cigars <= 60  
    
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif 61 <= speed <= 80:
        return 1
    else:
        return 2 
    
def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6 

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1 
def sorta_sum(a, b):
    total = a + b
    if 10 <= total <= 19:
        return 20
    return total 

def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10 
    
def squirrel_play(temp, is_summer):
    upper_limit = 100 if is_summer else 90
    return 60 <= temp <= upper_limit 

def alarm_clock(day, vacation):
    if vacation:
        return "10:00" if 1 <= day <= 5 else "off"
    else:
        return "7:00" if 1 <= day <= 5 else "10:00" 
def near_ten(num):
  if num%10==2: 
    return True 
  else:
    return False
