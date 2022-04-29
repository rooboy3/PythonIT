import random

lowBound = 0
highBound = 100
response = ''
randomNumber = random.randint(lowBound,highBound)

while response != "yes":
    print ("Is it ", randomNumber, " ?")
    response = input()
    if response == "higher":
        lowBound = randomNumber + 1   
        randomNumber = random.randint(lowBound,highBound)
    elif response == "lower":
        highBound = randomNumber - 1
        randomNumber = random.randint(lowBound,highBound)
    elif response == "yes":
        print ("Woohooo, I'm so good'")
        break
    else:
        print ('Huh? "higher", "lower", or "yes" are valid responses.')