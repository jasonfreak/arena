class ShufflingCardsDiv2(object):
    def __init__(self):
        object.__init__(self)

    def index(self, permutation):
        result = {}
        cntOfCards = len(permutation)
        for i in range(cntOfCards):
            result[permutation[i]] = i
        return result

    def shuffle(self, permutation):
        cntOfCards = len(permutation)
        cntOfHalf = cntOfCards/2
        cntOfSwitchCards = cntOfCards/4
        idx = self.index(permutation)
        init = range(1, cntOfCards+1)
        cntOfErrors = sum([1 if idx[init[i]] >= cntOfHalf else 0 for i in range(cntOfHalf)])

        cntOfSwitches = cntOfErrors / cntOfSwitchCards if cntOfErrors % cntOfSwitchCards == 0 else cntOfErrors / cntOfSwitchCards + 2
        print 'debug[21]', cntOfSwitches

        if cntOfSwitches % 2 == 0:
            return 'Possible'
        else:
            return 'Impossible'

def main():
    obj = ShufflingCardsDiv2()
#    print obj.shuffle((1, 2, 3, 4))
#    print obj.shuffle((4, 3, 2, 1))
#    print obj.shuffle((1, 3, 2, 4))
    print obj.shuffle((1,4,2,5,3,6))

if __name__ == '__main__':
    main()
