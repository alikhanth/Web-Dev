def hello_name(name):
  return "Hello " + name+"!"

def make_out_word(out, word):
    return out[:2] + word + out[2:]

def first_half(str):
    return str[:len(str) // 2]
 
def non_start(str1, str2):
    return str1[1:] + str2[1:]

def make_abba(a, b):
    return a + b + b + a 

def extra_end(str):
    return str[-2:] * 3 

def without_end(str):
    return str[1:-1] 
def left2(str):
    return str[2:] + str[:2] 

def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>" 

def first_two(str):
    return str[:2] 

def combo_string(a, b):
    return a + b + a if len(a) < len(b) else b + a + b
def make_ends(nums):
  return [nums[0],nums[-1]]

def make_pi():
    return [3, 1, 4] 
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return nums[0]
    else:
        return nums[0] + nums[1] 
    
def has23(nums):
  if nums[0]==2 or nums[0]==3 or nums[1]==2 or nums[1]==3: 
    return True 
  else: 
    return False