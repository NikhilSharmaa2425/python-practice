def differenceofSum(n,m):
    sum_divisible  = 0
    sum_not_divisible = 0
    for i in range(1,m+1):
        if i % n == 0:
            sum_divisible  += i
        else:
            sum_not_divisible += i
    return (abs(sum_not_divisible - sum_divisible)) 

n = 3
m = 10
print(differenceofSum(n,m))