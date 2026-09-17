#Recursive function to multiply two numbers without using the multiplication operator
def multiply(a, b):
    if a == 0 or b == 0:
        return 0

    if a < b:
        a, b = b, a

    if b < 0:
        return -multiply(a, abs(b))

    return a + multiply(a, b - 1)
    

num1 = int(input())
num2 = int(input())
print(multiply(num1,num2))