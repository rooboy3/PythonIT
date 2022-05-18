text1 = open("score.txt", "r+")
import random
from matplotlib.pyplot import text
ans = ["Heads","Tails"]
def coinToss():
    wincount = 0
    losscount = 0
    score = text1.read()
    text1.close()
    scoreold = score
    print("You currently have: "+str(score)+" dollars. Payout is 2x")
    try:
        number = int(input("Number of times to flip coin? (int) "))
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
    if(number*bet_amt > int(score)):
        print("You bet is higher than your balance!")
        exit
    else:
        score = int(score) - int(number)*int(bet_amt)
        score = str(score)
        print(score)
        recordList = []
        for i in range(number):
            flip = random.randint(0, 1)
            if (flip == 0):
                recordList.append("Heads")
                wincount = wincount + 1
            else:
                wincount = wincount - 1
                recordList.append("Tails")
        print(wincount)
        print(str(recordList))
        print("The coin landed on heads: "+str(recordList.count("Heads"))+" times."+" The coin landed on tails: "+str(recordList.count("Tails"))+" times.")
        print("Score "+str(score))
        print("bet_amt "+str(bet_amt))
        print("number "+str(number))
        print("Wincoutn "+str(wincount))
        def scorecalc():
            step = wincount
            print(step)
            for i in range(number):
                if(wincount > 0):
                    score = int(scoreold)+(((wincount*bet_amt))*2)
                    print(str(score) + str("up"))
                    step = step + 1
                elif(wincount < 0):
                    score = int(scoreold)+(((wincount*bet_amt)))
                    print(str(score) + str("down"))
                    step = step + 1
                elif(wincount == 0):
                    print("bunga")
                    score = (int(scoreold)+((((number/2)*bet_amt))*2))/2
        scorecalc()
        print(score)
        scorenew = int(score)
        text2=open("score.txt","w")
        text2.write(str(scorenew))
        text2.close()
        print("Skull emoji x7")
coinToss()