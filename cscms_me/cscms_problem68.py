num = int(input())
text = input().split()

max_length = max(len(word) for word in text)

for j in range(max_length):
    for i in range(num):
        if j < len(text[i]):
            print(text[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()