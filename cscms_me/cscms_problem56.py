num = int(input())
lst = list(map(int, input().split()))

result = []
count = 0

if num == 1:
    result.append(lst[0])
    count += 1

else:
    for i in range(len(lst)):
        if i == 0:
            if lst[i] > lst[i + 1]:
                result.append(lst[i])
                count += 1

        elif i == len(lst) - 1:
            if lst[i] > lst[i - 1]:
                result.append(lst[i])
                count += 1

        else:
            if lst[i] > lst[i + 1] and lst[i] > lst[i - 1]:
                result.append(lst[i])
                count += 1

print(count)
print(*result)