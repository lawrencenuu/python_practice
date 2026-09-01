text = list(map(str,input().lower()))

seen = set()
count = 1
for char in text:
    if char in seen:
        count +=1
        seen.clear()
        seen.add(char)
    else:
        seen.add(char)
    
print(count)




