
shongkha, n = map(int, input().split())

for i in range(n):
    if shongkha % 10 != 0:
        shongkha -= 1
    else:
        
        shongkha = shongkha // 10

print(shongkha)

