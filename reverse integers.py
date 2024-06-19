number=int(12345)

reverse_number = 0
while(number > 0):
    remainder = number % 10  
    reverse_number = (reverse_number * 10) + remainder  
    number = number // 10  
    print("the reversed number is:{}".format(reverse_number))