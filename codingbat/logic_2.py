#make_bricks
def make_bricks(small, big, goal):
    big_needed = min(big, goal // 5)
    remaining = goal - (big_needed * 5)

    return remaining <= small

# lone_sum
def lone_sum(a, b, c):
  if a==b==c:
    return 0
  elif a==b:
    return c
  elif b==c:
    return a
  elif c==a:
    return b
  else:
    return a+b+c
  
#luck_sum
def lucky_sum(a, b, c):
  if a== 13:
    return 0
  elif b==13:
    return a
  elif c==13:
    return a+b
  else:
    return a+b+c

#no_teen_sum
def no_teen_sum(a, b, c):
  if fix_teen(a) and fix_teen(b) and fix_teen(c):
    return 0 
  elif fix_teen(b) and fix_teen(c):
    return a
  elif fix_teen(a) and fix_teen(b):
    return c
  elif fix_teen(a) and fix_teen(c):
    return b
  elif fix_teen(a):
    return b+c
  elif fix_teen(b):
    return a+c
  elif fix_teen(c):
    return a+b
  else:
    return a+b+c

def fix_teen(n):
  if (n>=13 and n<15) or (n>=17 and n<=19):
    return True

# round_sum
def round_sum(a, b, c):
  return round10(a)+round10(b)+round10(c)

def round10(num):
  rounded_num = round(num,-1)
  
  return int(rounded_num)

# close_far
def close_far(a, b, c):
  if abs(a-b)==1 or abs(a-b)==0:
    if abs(a-c)>=2 and abs(b-c)>=2:
      return True
    else:
      return False
  elif abs(a-c)==1 or abs(a-c)==0: 
    if abs(a-b)>=2 and abs(c-b)>=2:
      return True
    else: 
      return False

#make_chocolate 
def make_chocolate(small, big, goal):
    required_chocolate = min(big,goal//5)
    remaining = goal-(required_chocolate*5)

    if remaining <= small:
        return remaining
    else:
        return -1
