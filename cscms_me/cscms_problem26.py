# Trying Every Possible Combination --> Time Limit Exceeded
# N = int(input())
# students = list(map(int, input().split()))
# total = sum(students)
# minimum = float("inf")
# for i in range(1,2**N-1):
#   sum_a = 0
#   for position in range(N):
#       bit = (i >> position) & 1
#       if bit == 0:
#           sum_a += students[position]
#   sum_b = total - sum_a

#   difference = abs(sum_a - sum_b)

#   if difference < minimum:
#       minimum = difference

# print(minimum)

# Dynamic Programming Approach
N = int(input())
students = list(map(int, input().split()))

total = sum(students)
target = total // 2

possible = [False] * (target + 1)
possible[0] = True

for student in students:
    for current_sum in range(target, student - 1, -1):
        if possible[current_sum - student]:
            possible[current_sum] = True

for group_a in range(target, -1, -1):
    if possible[group_a]:
        group_b = total - group_a
        print(abs(group_a - group_b))
        break