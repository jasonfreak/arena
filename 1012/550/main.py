class ShufflingCardsDiv1(object):
    def __init__(self):
        object.__init__(self)

    def shuffle(self, permutation):
        result = 0
        cntOfCards = len(permutation)
        
        isOdds = {}
        for i in range(cntOfCards):
            isOdds[permutation[i]] = True if i % 2 == 0 else False

        begin = range(1, cntOfCards+1)
        if tuple(begin) == permutation:
            return 0

        cntOfOdds = 0
        cntOfHalf = cntOfCards / 2
        for i in range(cntOfHalf):
            if isOdds[begin[i]]:
                cntOfOdds = cntOfOdds + 1

        cntOfHalfOfHalf = cntOfHalf / 2 if cntOfHalf % 2 == 0 else cntOfHalf / 2 + 1
        print 'debug[22]', cntOfOdds, cntOfHalf, cntOfHalfOfHalf
        if cntOfOdds == cntOfHalf:
            return 1
        else: 
            if cntOfOdds == cntOfHalfOfHalf:
                return 2
            elif cntOfOdds != 0:
                return 3
            else:
                return 4

def main():
    obj = ShufflingCardsDiv1()
#    print obj.shuffle((1, 2, 3, 4))
#    print obj.shuffle((1, 3, 4, 2))
#    print obj.shuffle((6, 3, 5, 2, 4, 1))
#    print obj.shuffle((8,5,4,9,1,7,6,10,3,2))
#    print obj.shuffle((9,1,7,2,10,3,6,4,8,5))

if __name__ == '__main__':
    main()
