num = int(input())
lst = list(map(int, input().split()))
query = int(input())

for i in range(query):
    q = list(map(int, input().split()))
    a = q[0]
    b = q[1]
    result = 0
    for j in range(a,b+1):
        result += lst[j]
    print(result)


