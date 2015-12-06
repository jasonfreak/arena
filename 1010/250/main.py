from sys import maxint

class ChristmasTreeDecoration(object):
    def __init__(self):
        object.__init__(self)

    def countOfUgly(self, col, x, y):
        result = 0
        cntOfRibbons = len(x)
        for i in range(cntOfRibbons):
            if col[x[i]-1] == col[y[i]-1]:
                result = result + 1
        return result
    
    def solve(self, col, x, y):
        result = maxint
        cntOfStars = len(col)
        cntOfRibbons = len(x)
        cur = 0
        r = cntOfStars - 1
        poss = range(-1, r-1)
        while cur >= 0:
            poss[cur] = poss[cur] + 1
            if poss[cur] == cntOfRibbons:
                for i in range(cur, r):
                    poss[i] = poss[i-1] + 1
                cur = cur - 1
            else:
                if cur == r - 1:
                    cou = self.countOfUgly(col, [x[poss[i]] for i in range(r)], [y[poss[i]] for i in range(r)])
                    if cou < result:
                        result = cou
                else:
                    cur = cur + 1
        return result

def main():
    obj = ChristmasTreeDecoration()
#    print obj.solve((50,50,50,50), (1,2,3,4,1,2), (2,3,4,1,3,4))
#    print obj.solve((1,4,2,3), (1,2,3), (2,3,4))
    print obj.solve((1,1,1,2,2,2,3,3,3,4,4,4), (1,2,3,4,5,6,7,8,9,10,11,12,1,1,1,1,1,1), (2,3,1,5,6,4,8,9,7,11,12,10,5,7,12,11,6,4))

if __name__ == '__main__':
    main()

