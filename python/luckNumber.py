import random
import re


# a = random.randrange(0,5)
# b = random.randrange(6,10)
# c = random.randrange(11,15)
# d= random.randrange(15,20)
# e= random.randrange(0,100)
# f= random.randrange(0,20)
# g= random.randrange(100,1000)
pastWin=[]

while True:
    # game = [a,b,c,d,e,f,g]
    # result=random.choice(game)
    result = random.randrange(0,5)
    print(f"PastWins : {pastWin}")

    if len(pastWin) <= 10:
        pastWin.append(result)
    
    else:
        pastWin.clear()
    
    userInput = input("Guess the winner ball from 0-5 : ")

    match= re.search(r'\d+', userInput)

    if match:
        userNum = int(match.group())

        if userNum == result:
            print(f"Your Number : {userNum} and the {result}")
            print(" ✅ YOU WON ✅")

        else:
            print(result)
            print("❌ YOU LOSE ❌")
    else:
        print("Thanks for playing 👋")
        break