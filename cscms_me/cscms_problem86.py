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

# This will be for huge inputs
# def multiply(a, b):
#     # Base case
#     if a == 0 or b == 0:
#         return 0

#     # Handle negative numbers
#     if b < 0:
#         return -multiply(a, -b)

#     # If b is even:
#     # a × b = (a × (b/2)) × 2
#     if b % 2 == 0:
#         half = multiply(a, b // 2)
#         return half + half

#     # If b is odd:
#     # a × b = a + (a × (b-1))
#     return a + multiply(a, b - 1)


# num1 = int(input())
# num2 = int(input())

# print(multiply(num1, num2))