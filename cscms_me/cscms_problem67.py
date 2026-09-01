num = int(input())
total = 0 
for value in range(1,num+1):
    if value%15 ==0: 
        total += (value*10)
    elif value%5 ==0:
        total += (value*3)
    elif value%3==0:
        total += (value*2)
    else:
        total += value
print(total)