#double_char
def double_char(str):
  text = ''
  for i in str:
    text += i*2
  return text

#count_hi
def count_hi(str):
  return str.count("hi")

#cat_dog
def cat_dog(str):
  cat_count = str.count("cat")
  dog_count = str.count("dog")
  
  return cat_count == dog_count

#count_code
def count_code(str):
  count = 0 
  for i in range(len(str)-3):
    if str[i:i+2]=='co' and str[i+3]=='e':
      count += 1
  return count

#end_other
def end_other(a, b):
  # low_a = a.lower()
  # low_b = b.lower()
  # if low_b.endswith(low_a) or low_a.endswith(low_b):
  #   return True
  # else: 
  #   return False
  return b.lower().endswith(a.lower()) or a.lower().endswith(b.lower())
    
 

#xyz_there
def xyz_there(str):
    for i in range(len(str) - 2):
        if str[i:i+3] == "xyz":
            if i == 0 or str[i-1] != ".":
                return True
    return False
