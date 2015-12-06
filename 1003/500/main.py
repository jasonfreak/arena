from copy import deepcopy

class SortishDiv2(object):
    def __init__(self):
        object.__init__(self)

    def getWaysByRecursion(self, ws, maxSortedness, sortedness, i, seq, freeNums):
#        print 'debug[8]', maxSortedness, i, seq, freeNums
#        raw_input()

        if i == len(seq):
            if maxSortedness == sortedness:
#                print 'debug[13] sorted'
                ws.append(1)
            return
        if maxSortedness < sortedness:
            return
        if seq[i] > 0:
            cntUnsortedBefore = 0
            for j in range(0, i):
                cntUnsortedBefore = cntUnsortedBefore + 1 if seq[j] < seq[i] else cntUnsortedBefore
            diff = seq[i] - 1 - cntUnsortedBefore
            self.getWaysByRecursion(ws, maxSortedness-diff, sortedness, i+1, seq, freeNums)
        else:
            for j in range(len(freeNums)):
                new_seq = deepcopy(seq)
                new_seq[i] = freeNums[j]
                self.getWaysByRecursion(ws, maxSortedness, sortedness, i, new_seq, freeNums[:j]+freeNums[j+1:])

    def ways(self, sortedness, seq):
        seq = list(seq)
        cntSeq = len(seq)
        maxSortedness = cntSeq * (cntSeq-1) / 2
        ws = [0]

        freeNums = range(1, cntSeq+1)
        for num in seq:
            if num > 0:
                freeNums[num-1] = 0
        freeNums = filter(lambda x:x>0, freeNums)

        print 'debug[35]', freeNums
        self.getWaysByRecursion(ws, maxSortedness, sortedness, 0, seq, freeNums)

        return sum(ws)

            
def main():
    obj = SortishDiv2()
    print obj.ways(2, (1, 2, 0, 5, 0, 0))

if __name__ == '__main__':
    main()





        

