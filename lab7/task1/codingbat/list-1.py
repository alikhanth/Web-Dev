def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

def reverse3(nums):
    return nums[::-1] 

def middle_way(a, b):
  return [a[1],b[1]]

def same_first_last(nums):
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    return False
def sum3(nums):
  return nums[0]+nums[1]+nums[2]

def max_end3(nums):
  max_value = max(nums[0], nums[-1])  
  return [max_value] * 3  