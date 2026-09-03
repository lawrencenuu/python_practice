num = int(input())
for i in range(num): 
  for j in range(num):
    if (i==0 and j==0) or (i==num-1 and j==num-1) or (i==0 and j==num-1) or (i==num-1 and j==0):
      print("-", end="")
    else:
      print("*", end="")
  print()