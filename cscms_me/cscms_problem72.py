def stair(n):
  if n == 1:
    return 1
  if n == 2:
    return 1

  return stair(n-1) + stair(n-2)

num = int(input())
print(stair(num))