def double_char(str):
    str2 = []
    for c in str:
        str2.append(2*c)
        
    return "".join(str2) 

def count_code(str):
    count = 0
    for i in range(len(str)-3):
        if str[i:i+2] == "co" and str[i+3] == "e":
            count += 1
                    
    return count 

def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "hi":
            count += 1
            
    return count 

def end_other(a, b):
    a = a.lower()
    b = b.lower()
        
    return a.endswith(b) or b.endswith(a) 

def cat_dog(str):
    cat = 0
    dog = 0
      
    for i in range(len(str) - 2):
        if str[i:i+3] == "cat":
            cat += 1
        elif str[i:i+3] == "dog":
            dog += 1
                                  
    return cat == dog 

def xyz_there(str):
    if str[:3] == "xyz":
        return True
                    
    for i in range(1, len(str) - 2):
        if str[i-1] != "." and str[i:i+3] == "xyz":
            return True
                                      
    return False