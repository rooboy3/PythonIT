import time
n = int(input("How long do you require the countdown to be? "))

while n > 0:
    print("Countdown in T-" + str(n) + " seconds.")
    n = n - 1
    time.sleep(1)

while n == 0:
    print("Liftoff.")
    n = n - 1
    time.sleep(1)

while n < 0:
    print("Liftoff was " + str(n*-1) + " seconds ago.")
    n = n - 1
    time.sleep(1)