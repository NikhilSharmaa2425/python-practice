import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ123456!@#%$*()"
while 1:
    password_len = int(input("what password lenght do you want : "))
    password_count = int(input("How many passwords would you like : "))
    for x in range(0,password_count):
        password = ''
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char
        
        print("Here is your password : ",password)