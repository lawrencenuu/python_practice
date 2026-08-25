#string_times
def string_times(str, n):
  return str*n

#front_times
def front_times(str, n):
  return str[0:3]*n

#string_bits
def string_bits(str):
  return str[::2]

#string_splosion
def string_splosion(str):
  text = ''
  for i in range(len(str)):
    text += str[:i+1]
  
  return text

#last2
def last2(str):
  last_2chars = str[-2:] 
  count = 0
  for i in range(len(str)-2): 
    if last_2chars == str[i]+str[i+1]: 
      count += 1
  return count

#array_count9
def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count += 1
  
  return count
#array_font9
def array_front9(nums):
  if 9 in nums[:4]:
    return True
  else:
    return False

#array123
def array123(nums):
  seq = [1,2,3]
  for i in range(len(nums)):
    if nums[i:i+3] == seq:
      return True
  return False

#string_match
def string_match(a, b):
  count = 0 
  
  for i in range(len(a)-1): 
    for j in range(len(b)-1):
      if a[i:i+2] == b[j:j+2] and i==j:
        count += 1

  return count
