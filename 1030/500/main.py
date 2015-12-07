from itertools import combinations

class TheKingsRoadsDiv1(object):
    def __init__(self):
        object.__init__(self)

    def check(self, subA, subB, level):
        if len(subA) == 0:
            return True
        cntOfRoad = len(subA)
        degrees = {}
        for i in range(cntOfRoad):
            degrees[subA[i]] = degrees.get(subA[i], 0) + 1
            degrees[subB[i]] = degrees.get(subB[i], 0) + 1
        cntOfSource = 0
        for city in degrees.keys():
            if degrees[city] == 2:
                cntOfSource += 1
            if cntOfSource > pow(2, level):
                return False
        if cntOfSource < pow(2, level):
            return False
        else:
            newA = []
            newB = []
            for i in range(cntOfRoad):
                if degrees[subA[i]] != 2 and degrees[subB[i]] != 2:
                    newA.append(subA[i])
                    newB.append(subB[i])
            return self.check(newA, newB, level+1)
        

    def getAnswer(self, h, a, b):
        cntOfRoad = len(a)
        indexes = range(cntOfRoad)
        cbs = combinations(indexes, cntOfRoad-3)
        for cb in cbs:
            subA = map(lambda x: a[x], cb)
            subB = map(lambda x: b[x], cb)
            if self.check(subA, subB, 0):
#                print 'debug[41]', subA, subB
                return 'Correct'
        return 'Incorrect'

def main():
    obj = TheKingsRoadsDiv1()
#    print obj.getAnswer(3, (1, 3, 2, 2, 3, 7, 1, 5, 4), (6, 5, 4, 7, 4, 3, 3, 1, 7))
#    print obj.getAnswer(2, (1, 2, 1, 3, 3), (2, 1, 2, 3, 3))
    print obj.getAnswer(5, (6, 15, 29, 28, 7, 13, 13, 23, 28, 13, 30, 27, 14, 4, 14, 19, 27, 20, 20, 19, 10, 15, 7, 7, 19, 29, 4, 24, 10, 23, 30, 6, 24), (9, 22, 30, 20, 26, 25, 8, 7, 24, 21, 27, 31, 4, 28, 29, 6, 16, 1, 17, 10, 3, 12, 30, 18, 14, 23, 19, 21, 5, 13, 15, 2, 11))

if __name__ == '__main__':
    main()
