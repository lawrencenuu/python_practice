num1 = int(input())
num2 = int(input())
check = False 

for i in range(1,num1+1):
    if not (i == num2 or i == num2-1 or i == num2+1):
        print(i, end=" ")
        check = True

if not check:
    print("DIE")