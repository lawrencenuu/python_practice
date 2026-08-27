#cigar_party
def cigar_party(cigars, is_weekend):
    return (cigars>=40 and cigars<=60) or (is_weekend and cigars >=40)

#date_fashion
def date_fashion(you, date):
  if (you >=8 or date >= 8)  and not (you <=2 or date<=2):
    return 2
  elif you <=2 or date<=2:
    return 0
  else:
    return 1
  
#squirrel_play
def squirrel_play(temp, is_summer):
  if (temp>=60 and temp<=90) and not is_summer:
    return True
  elif (temp>=60 and temp<=100) and is_summer:
    return True
  else:
    return False

#caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    elif speed >=66 and speed <=85:
      return 1
    elif speed >=81:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed >=61 and speed <=80:
      return 1
    elif speed >=81:
      return 2
  
#sorta_sum
def sorta_sum(a, b):
  if (a+b) >=10 and (a+b)<=19:
    return 20
  else:
    return a+b

#alarm_clock
def alarm_clock(day, vacation):
  if (day>=1 and day<=5) and not vacation:
    return '7:00'
  elif (day==0 or day==6) and not vacation:
    return '10:00'
  elif (day>=1 and day<=5) and vacation:
    return '10:00'
  elif (day==0 or day==6) and vacation:
    return 'off'

#love6
def love6(a, b):
  if a==6 or b==6:
    return True
  elif (a+b) == 6 or (abs(a-b))==6:
    return True
  else:
    return False

#in1to10
def in1to10(n, outside_mode):
    if not outside_mode:
        if n>=1 and n <=10:
            return True
        else:
            return False
    else:
        if n<=1 or n >=10:
            return True
        else:
            return False
 

 # near_ten 
def near_ten(num):
  check = False
  for i in range(101):
    if ((i*10)+1) == num or ((i*10)-1) == num or ((i*10)+2) == num or ((i*10)-2) == num or (i*10) == num:
      check = True
  
  return check 
