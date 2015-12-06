from math import sqrt

class AliceGame(object):
    def __init__(self):
        object.__init__(self)

    def findMinimumValue(self, x, y):
        if x == 0:
            return 0
        values = {}
        cntOfRound = sqrt(x+y)
        if cntOfRound % 1 != 0:
            return -1
        cntOfRound = int(cntOfRound)

        for r in range(1, cntOfRound+1):
            cur = 0
            poss = range(-1, r-1)
            while cur >= 0:
                poss[cur] = poss[cur] + 1
#                print 'debug[18]', r, cur, poss
                if poss[cur] == cntOfRound:
                    for i in range(cur, r):
                        poss[i] = poss[i-1] + 1
                    cur = cur - 1
                else:
                    if cur == r - 1:
                        if x == sum([(poss[i]+1) * 2 - 1 for i in range(r)]):
#                            print 'debug[27]', r, cur, poss
                            values[r] = values.get(r, 0) + 1
                    else:
                        cur = cur + 1
        return min(values.keys(), key=lambda x:values[x])

def main():
    obj = AliceGame()
    print obj.findMinimumValue(500000, 500000)

if __name__ == '__main__':
    main()
