from sys import maxint

class ShufflingCardsDiv1(object):
    def __init__(self):
        object.__init__(self)

    def rearrangesByRecursion(self, result, done, half):
        cntOfDone = len(done)
        cntOfCards = len(half)
        if cntOfDone == cntOfCards:
            result.append(done)
        else:
            for card in half:
                if card not in done:
                    self.rearrangesByRecursion(result, done+[card], half)

    def union(self, half1, half2):
        result = []
        cntOfCards = len(half1)
        for i in range(cntOfCards):
            result.append(half1[i])
            result.append(half2[i])
        return result

    def shuffleByRecursion(self, step, last, current, permutation, permutations, paths):
        if step >= permutations.get(permutation, maxint):
#            print 'debug[28]'
            return
        if step >= permutations.get(current, maxint):
#            print 'debug[32]'
            return
        else:
            permutations[current] = step
            paths[current] = paths.get(last, []) + [current]
            if current == permutation:
                return
            else:
#                    print 'debug[34]', step, current, permutations
                cntOfCards = len(current)
                half1s = []
                self.rearrangesByRecursion(half1s, [], current[:cntOfCards/2])
#                    print 'debug[40]', half1s
                half2s = []
                self.rearrangesByRecursion(half2s, [], current[cntOfCards/2:])
#                    print 'debug[40]', half2s
                for half1 in half1s:
                    for half2 in half2s:
                        new = self.union(half1, half2)
                        self.shuffleByRecursion(step+1, current, tuple(new), permutation, permutations, paths)

    def shuffle(self, permutation):
        permutations = {}
        paths = {}
        cntOfCards = len(permutation)
        current = range(1, cntOfCards+1)
        self.shuffleByRecursion(0, None, tuple(current), permutation, permutations, paths)
        result = permutations.get(permutation, maxint) 
#        print 'debug[58]', paths.get(permutation, None)

#        allrange = []
#        self.rearrangesByRecursion(allrange, [], current)
#        for r in allrange:
#            if tuple(r) not in permutations:
#                print 'debug[64]', r

        return -1 if result == maxint else result

def main():
    obj = ShufflingCardsDiv1()
#    print obj.shuffle((1, 2, 3, 4))
#    print obj.shuffle((3, 1, 4, 2))
#    print obj.shuffle((6, 5, 4, 3, 2, 1))
#    print obj.shuffle((6, 3, 5, 2, 4, 1))
#    print obj.shuffle((8,5,4,9,1,7,6,10,3,2))

if __name__ == '__main__':
    main()
