#first_last6
def first_last6(nums):
  check=False
  if nums[0]==6 or nums[-1]==6 :
    check = True
    
  return check

#same_first_last
def same_first_last(nums):
  if len(nums) >=1 and nums[0] == nums[-1]:
    return True
  else:
    return False

#make_pi
def make_pi():
  lst = [3,1,4]
  return lst

#common_end
def common_end(a, b):
  if a[0]==b[0] or a[-1] == b[-1]:
    return True
  else:
    return False

#sum3
def sum3(nums):
  total = sum(nums)
  return total

#rotate_left3
def rotate_left3(nums):
  first = nums[0]
  rest = nums[1:]
  rest.append(first)
  return rest

#reverse3
def reverse3(nums):
  reversed = nums[::-1]
  return reversed


#max_end3
def max_end3(nums):
  biggest = 0
  new_nums = []
  # for i in range(len(nums)):
  #   if i+1 < len(nums)-1 and nums[i+1] >= nums[i]:
  #     biggest = nums[i+1]
  #   elif i < len(nums)-1 and nums[i] >= biggest: 
  #     biggest = nums[i]
  if nums[0] > nums[-1]:
    biggest = nums[0]
  else:
    biggest = nums[-1]
  for i in range(len(nums)): 
    new_nums.append(biggest)
  
    
  return new_nums

#sum2
def sum2(nums):
  total=0
  if len(nums) <=2:
    total= sum(nums)
  else:
    # total= nums[0] + nums[1]
    total = sum(nums[0:2])
  return total

#middle_way
def middle_way(a, b):
  a_mid = a[1]
  b_mid = b[1]
  new_lst = [a_mid,b_mid]
  return new_lst

#make_ends
def make_ends(nums):
  if len(nums)<2:
    new_lst = [nums[0],nums[0]]
    return new_lst
  else: 
    new_lst = [nums[0],nums[-1]]
    return new_lst

#has23
def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  
  return False
