import time
current = 1
previous = 1
hold = 0
step = 1
def new_func(current, previous, hold, step):
    while 2 != 1:
        hold = current
        print(step,'{:,}'.format(hold))
        current = current + previous
        previous = hold
        step = step + 1
        time.sleep(0.1)

new_func(current, previous, hold, step)