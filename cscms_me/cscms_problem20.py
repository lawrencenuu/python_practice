num = int(input())
num_lst = list(map(int, input().split()))
height = max(num_lst)

for i in range(1, height + 1):
    row = ""
    for mountain in num_lst:
        # Which row of this particular mountain are we on?
        local_row = i - (height - mountain)
        if local_row < 1:
            # This mountain hasn't started yet
            row += "-" * (mountain * 2 - 1)
        else:
            # This mountain exists on this row
            leading_dashes = mountain - local_row
            stars = local_row * 2 - 1
            
            row += "-" * leading_dashes
            row += "*" * stars
            row += "-" * leading_dashes

    print(row)