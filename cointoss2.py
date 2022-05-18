import random
def coinToss():
    text1 = open("score.txt", "r+")
    ans = ["Heads","Tails"]
    score = text1.read()
    text1.close()
    print("You currently have: "+str(score)+" dollars. Payout is 2x")
    try:
        gamecount = int(input("Number of times to flip coin? (int) "))
    except ValueError:
        print("Input must be an intiger!")
        exit()
    bet_face = input("Your bet is? (Heads, Tails) ")
    if bet_face not in ans:
        print("You must choose \"Heads\" or \"Tails\". Make sure to capitalize!")
        exit()
    try:
        bet_amt = int(input("You bet amount is? (int) "))
    except ValueError:
        print("Input must be an intiger!")
        exit()
    if(gamecount*bet_amt > int(score)):
        print("You bet is higher than your balance!")
        exit
    else:
        global moneyin
        moneyin = int(gamecount)*int(bet_amt)
        global scoretemp
        scoretemp = int(score) - int(moneyin)
        recordList = []
        print("score"+str(score))
        print("scoretemp"+str(scoretemp))
        for i in range(gamecount):
            flip = random.randint(0, 1)
            if (flip == 0):
                recordList.append("Heads")
            else:
                recordList.append("Tails")
        print("The coin landed on heads: "+str(recordList.count("Heads"))+" times."+" The coin landed on tails: "+str(recordList.count("Tails"))+" times.")
        print("Score Temp" + str(scoretemp))
        print("Score" + str(score))
        score = int(score) + (int(recordList.count("Heads")*2)) -(int(recordList.count("Tails")))
        print(score)
        text2=open("score.txt","w")
        text2.write(str(score))
        text2.close()
coinToss()