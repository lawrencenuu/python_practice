#count_events
def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i]%2 == 0:
      count += 1
  
  return count

#big_diff
def big_diff(nums):
  big = max(nums)
  small = min(nums) 
 
  return big - small

#centered_average
def centered_average(nums):
  sm = min(nums) 
  bg = max(nums) 
  nums.remove(sm)
  nums.remove(bg) 
  divisor = len(nums) 
  answer = int(sum(nums)/divisor)
  return answer

#sum13
def sum13(nums):
  total = 0
  i = 0 
  
  while i < len(nums):
    if nums[i] == 13:
      i += 2
    else:
      total += nums[i]
      i += 1
      
  return total

#sum67
def sum67(nums):
  total = 0 
  i = 0 
  while i < len(nums): 
    if nums[i]==6: 
      i+=1
      while nums[i] !=7: 
        i +=1 
      i+=1 
    else: 
      total +=nums[i]
      i += 1
  return total 

#has22
def has22(nums):
  check = False
  for i in range(len(nums)-1): 
    if nums[i] == 2 and nums[i+1] ==2:
      check = True
      
  return check

