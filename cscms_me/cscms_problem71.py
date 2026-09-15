# num = int(input())
# binary = bin(num)[2:]
# print(binary)

num = int(input())
binary_str = ""
if num == 0:
  binary_str += "0"
while num >0:
  remainder = num % 2
  binary_str = str(remainder)+binary_str
  num = num//2

print(binary_str)