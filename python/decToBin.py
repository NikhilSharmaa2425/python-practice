def DecToBin(n):
    res = ""
    while n != 0:
        if n % 2 == 0:
            res += "0"
        else:
            res += "1"
        n //= 2
    return int(res[::-1]) 
n = int(input("enter number"))
print(DecToBin(n))