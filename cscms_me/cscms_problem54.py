#Sorting 
num = int(input())

descending = sorted(map(int, input().split()), reverse=True)
ascending = sorted(descending)

largest_half = descending[: num // 2 + num % 2]
smallest_half = ascending[: num // 2]

result = []

for i in range(len(largest_half)):
    result.append(largest_half[i])

    if i < len(smallest_half):
        result.append(smallest_half[i])

print(*result)

   
