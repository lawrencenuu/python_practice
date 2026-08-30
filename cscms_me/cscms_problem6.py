text = str(input())
lst = text.split()
num1 = int(lst[0])
num2 = int(lst[1])
for i in range(num1):
  for j in range(num2):
    print("*", end="")
  print()