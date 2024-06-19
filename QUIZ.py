print("welcome to the quiz")
playing= input("enter yes to play the quiz ")
if playing.lower != "yes":
    quit()
score = 0
answer= input("what does cpu stands for ? ")
if answer.lower() == "central processing unit" :
    print("correct")
    score += 1
else:
    print("incorrect")    

    answer= input("what GPU stands for ? ")
if answer.lower() == "graphic processing unit" :
    print("correct")
    score += 1
else:
    print("incorrect")  

    answer= input("what does PSU stands for ? ")
if answer.lower() == "power supply unit" :
    print("correct")
    score += 1
else:
    print("incorrect")  