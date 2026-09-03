input_str = str(input())
input_list = input_str.split()
num1, num2 = int(input_list[0]), int(input_list[1])
for i in range(num1): 
  for j in range(num2):
    if i == 0 or i== num1-1 or j==0 or j==num2-1:
      print("*", end="")
    else:
      print("-", end="")
  print()