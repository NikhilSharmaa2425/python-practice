n = int(input("enter number which you want to print stars : "))

front = 0
back = n-3
for i in range(1,n+1):
    if i == 1:
        print("*"+" "*(n-2)+"*")
    elif i != 1 and i != n-1:
        print("*" + " " * front + "*" + " " * back + "*")
        front += 1
        back -= 1
