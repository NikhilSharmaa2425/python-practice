n = int(input("enter number : "))

# spac = 0
# back = n-2

# for i in range(n):
#     if i == n//2:
#         print(" "* spac , end = '')
#         print( "*" * (n//2)+1,end = '')
#         print("*")
#         spac += 1

#     elif i == n-1:
#         print(" " * spac, )
#     else:
#          print(" " * spac + "*" + " " * back + " ")
#          spac += 1
#          back -= 1 





# front = 0
# back = n - 2

# for i in range(n):
#     if i == n//2:
#         print(' '* front,end='')
#         front += 1
#         back -= 1
#         beech = (n//2)+1
#         print("*" * beech)
#     elif i == n -1:
#         print(" " * front,end='')
#         print("*")






#     print(" " * front, end='')
#     front += 1
#     print("*")
#     print(" " * back,end='')
#     back -= 1
#     print("*")




front = 0
back = n-2
beech = (n // 2)+1 
for i in range(n):
    if i == n -1:
        print(" "*front,end="")
        print("*")
    
    elif i == (n//2)-1:
        print(" "*front,end="")
        front += 1
        print("*" * beech)
        back-=1


    else:
        print(" "*front,end="")
        print("*" + " " * back + "*")
        front += 1
        back -= 1

