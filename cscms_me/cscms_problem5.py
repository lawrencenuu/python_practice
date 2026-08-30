#Prime Number
from math import sqrt
num = int(input())
if num > 1:
    exist = False
    for i in range(int(sqrt(num))): 
        if num % (i+1) == 0 and not (i+1) == 1 and not (i+1) == num:
            exist = True
            break
    if exist:
        print("No")
    else:
        print("Yes")
else:
    print("No")