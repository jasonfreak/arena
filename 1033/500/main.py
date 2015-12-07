from itertools import combinations

class FoxAndSouvenirTheNext(object):
    def __init__(self):
        object.__init__(self)

    def ableToSplit(self, value):
        cntOfSouvenir = len(value)
        if cntOfSouvenir % 2 != 0:
            return 'Impossible'
        cntOfHalfSouvenir = cntOfSouvenir / 2
        sumValue = sum(value)
        if sumValue % 2 != 0:
            return 'Impossible'
        halfValue = sumValue / 2

        cbs = combinations(value, cntOfHalfSouvenir)
        for cb in cbs:
            if sum(cb) == halfValue:
                return 'Possible'
        return 'Impossible'

def main():
    obj = FoxAndSouvenirTheNext()
#    print obj.ableToSplit((1,2,3,4))
    print obj.ableToSplit((1,1,1,3))

if __name__ == '__main__':
    main()
