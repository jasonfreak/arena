from math import log
class BearSortsDiv2(object):
    def __init__(self):
        object.__init__(self)

    def mergeSort(self, T, left, right, result, LESS):
        # if there is at most one element, we are done
        if left+1 >= right: return

        # otherwise, split the sequence into halves, sort each half separately
        mid = (left + right) / 2
        self.mergeSort(T, left, mid, result, LESS)
        self.mergeSort(T, mid, right, result, LESS)

        # then merge the two halves together
        merged = []    # an empty sequence
        p1 = left
        p2 = mid
        while (p1 < mid) or (p2 < right):
            if p1 == mid:
                merged.append( T[p2] )
                p2 += 1
            elif p2 == right:
                merged.append( T[p1] )
                p1 += 1
            else:
                if LESS(T[p1], T[p2]):
                    merged.append( T[p1] )
                    p1 += 1
                else:
                    merged.append( T[p2] )
                    p2 += 1
                result.append(1)

        # finally, move the merged elements back into the original array
        for i in range(left, right):
            T[i] = merged[i-left]

    def getProbability(self, seq):
        cntOfNums = len(seq)
        index = {}
        for i in range(cntOfNums):
            index[seq[i]] = i

        LESS = lambda x, y: index[x] < index[y]
        T = range(1, cntOfNums+1)
        result = []
        self.mergeSort(T, 0, cntOfNums, result, LESS)
        return log(pow(0.5, sum(result)))

def main():
    obj = BearSortsDiv2()
#    print obj.getProbability((1, 2))
#    print obj.getProbability((1, 3, 2))
    print obj.getProbability((10,13,18,2,4,6,24,22,19,5,7,20,23,14,21,17,25,3,1,11,12,8,15,16,9))

if __name__ == '__main__':
    main()
