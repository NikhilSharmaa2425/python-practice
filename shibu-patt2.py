n = 5

spa = 0


for i in range(n+1,1,-1):
    print(" " * spa , end='')
    spa += 1
    for j in range(1,i):
        if j == i-1:
            print(j)
        else:
            print(j,end='')
        