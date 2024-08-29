def strangeCounter(t):

    firstSecond = 3
    nextSecond = firstSecond

    while t > nextSecond:
        firstSecond = 2 * firstSecond 
        nextSecond = nextSecond + firstSecond

    print((firstSecond + 1) - (t - (nextSecond - firstSecond)))
if __name__ == '__main__':
    t = int(input().strip())
    strangeCounter(t)