string1 = input()
string2 = input()
if len(string1)<len(string2):
  if string1 in string2:
    text = string2.replace(string1,"")
    print(text)
  else: 
    print(string2) 
else: 
  if string2 in string1:
    text = string1.replace(string2,"")
    print(text)
  else:
    print(string1)
