bucket_day= list(map(int, input().split()))
bucket = bucket_day[0]
day = bucket_day[1]
result = [0 for i in range(bucket)]
for i in range(day): 
    q = list(map(int, input().split()))
    x = q[0]
    y = q[1]
    for j in range(bucket):
        if j>= x-1 and j<=y-1: 
            result[j] +=1

print(*result)