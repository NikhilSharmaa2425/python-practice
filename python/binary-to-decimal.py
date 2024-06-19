def BinToDec(n):
    key = 0
    res = 0
    while n != 0:
        digit = n % 10
        if digit ==  1:
            res += pow(2,key)
        key += 1
        n = n // 10
    return res
    







n = int(input("enter a binary number to convert it into decimal : "))
print(BinToDec(n))