n = int(input("enter number to display fibonacci triangle : "))


fib = [0,1]

for i in range(n-2):
    new = fib[-2] + fib[-1]
    fib.append(new)
print(fib)

point = 0
front = n//2 
back = 0
for i in range(n//2 + 1):
    if i == 0:
        # for i in range(point):
        #     print(" ",end = '')
        print(" " * front, end='')
        print(fib[point])
        front -= 1
        point += 1
    else:
        # for i in range(point):
        #     print(" ",end = '')
        print(" " * front, end='')
        front -= 1
        print(fib[point],end='')
        point += 1
        print(" " * back, end='')
        back += 1
        print(fib[point])
        point += 1




    
        