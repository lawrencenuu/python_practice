# num = int(input())
# num_lst = list(map(int, input().split()))
num = 2
num_lst =[3, 5]
max_height = max(num_lst)
for i in range(max_height): 
    for j in range(1,num_lst[i]+1):
        print(" "*(num_lst[i]-1)+"*"*(2*j-1))
    