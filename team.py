n = int(input())
solved_problems = 0
for i in range(n):

    a, b, c = map(int, input().split())
    
    if a + b + c >= 2:
        solved_problems += 1


print(solved_problems)
