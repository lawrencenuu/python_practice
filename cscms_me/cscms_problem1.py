numbers = str(input())
number_list= list(map(int, str(numbers).split()))
number_list.sort()
print(number_list[1])