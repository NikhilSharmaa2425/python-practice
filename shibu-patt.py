n = int(input(" entyer number : "))

spa = 0

for i in range(n,0,-1):
    cha = str(i)
    print(" " * spa, end='')
    spa += 1
    print(cha * i)