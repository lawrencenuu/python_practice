num = int(input())
dimension = num*2-1
half = int(dimension/2)

for i in range(dimension):
    for j in range(dimension):
        if  (i==0 and j>=half) or \
            (i>=half and j==0) or \
            (i==half and j<=half) or \
            (i <=half and j==dimension-1) or \
            (i==dimension-1 and j <=half) or \
            (i>=half and j==half) or \
            (i+j==half and j<half) or \
            (i+j==dimension-1 and j>=half) or \
            (i+j==(dimension-1+half)):
            print("*",end="")
        elif i+j>(dimension-1+half):
            print("",end="")
        else:
            print("-",end="")
    print()
