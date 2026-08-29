num = int(input())

def factorial(n):
  total = 1
  if n <= 20: 
    for i in range(n):
      total *= n
      n -= 1 
      
  return total

print(factorial(num))
      
      