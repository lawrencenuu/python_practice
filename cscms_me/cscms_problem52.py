text = str(input()).lower()

mid = int(len(text)/2)
if len(text)%2==0:
    print(text[mid-1::-1]+text[-1:mid-1:-1])
else:
    print(text[mid-1::-1]+text[mid]+text[-1:mid:-1])