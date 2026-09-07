# Easy way
# num = int(input())
# result = str(bin(num)[2:])
# output = result.count('1')
# print(output)

# Manual way 
num = int(input()) 
result = ''
if num ==0:
    result += '0'
while num > 0: 
    remainder = num%2 
    result = str(remainder)+ result
    num = num//2
print(result)
output = result.count('1')
print(output)
       