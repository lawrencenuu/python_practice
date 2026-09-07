query = int(input())
result = []
for i in range(query):
    numbers = list(map(int, input().split()))
    a = numbers[0]
    b = numbers[1]
    m = numbers[-1]

    result.append(pow(a, b, m)) #if you want to calculate (a^b) mod m, you can use the built-in pow function with three arguments: pow(a, b, m). This will compute (a^b) mod m efficiently.

for i in result:
    print(i)

