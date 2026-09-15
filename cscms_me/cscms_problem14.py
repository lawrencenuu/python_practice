num = int(input())
years = 0
days = 0
if num>0: 
    years += num//(60*24*365)
    days += ((num/(60*24*365)) - years) * 365

print(years, int(days))