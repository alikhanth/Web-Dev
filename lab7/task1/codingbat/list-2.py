def count_evens(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
                    
    return count 

def sum13(nums):
    s = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 1
        else:
            s += nums[i]
            
        i += 1
        
    return s 

def big_diff(nums):
    minimum = nums[0]
    maximum = nums[0]
      
    for i in range(1,len(nums)):
        minimum = min(minimum, nums[i])
        maximum = max(maximum, nums[i])
                    
    return maximum - minimum 

def sum67(nums):
    total = 0
    found6 = False
      
    for i in range(len(nums)):
        if nums[i] == 6:
            found6 = True
        if not found6:
            total += nums[i]
        if nums[i] == 7 and found6:
            found6 = False
            
    return total 

def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2) 

def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
                  
    return False