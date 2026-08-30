#Fibonacci 
num = int(input())

def Fibo(n):
    if n == 1:
        return "0"

    lst = [0, 1]

    for i in range(n - 2):
        next_num = lst[-1] + lst[-2]
        lst.append(next_num)

    return ' '.join(map(str, lst))

print(Fibo(num))