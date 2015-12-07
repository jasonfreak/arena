from sys import maxint
from itertools import combinations

class TheConsecutiveIntegersDivOne(object):
    def __init__(self):
        object.__init__(self)

    def operations(self, numbers):
        cntOfNumber = len(numbers)
        consecutive = [0, ] * cntOfNumber
        avg = sum(numbers) / cntOfNumber

        half = (cntOfNumber-1) / 2
        consecutive[half] = avg

        for i in range(half-1, -1, -1):
            consecutive[i] = consecutive[i+1] - 1

        for i in range(half+1, cntOfNumber):
            consecutive[i] = consecutive[i-1] + 1

#        print 'debug[22]', half, avg, numbers, consecutive

        return sum(map(lambda x, y: abs(x-y), numbers, consecutive))
            

    def find(self, numbers, k):
        result = maxint
        cbs = combinations(numbers, k)
        for cb in cbs:
            cntOfOperation = self.operations(sorted(cb))
            if cntOfOperation < result:
                result = cntOfOperation
        return result

def main():
    obj = TheConsecutiveIntegersDivOne()
#    print obj.find((4, 7, 47), 2)
#    print obj.find((1, 100), 1)
#    print obj.find((-96, -53, 82, -24, 6, -75), 2)
#    print obj.find((64, -31, -56), 2)
    print obj.find((14, 12, 3, 24, 33, 38, 30, 1, 26, 18, 17, 29, 4, 19, 13, 15, 40, 31, 9, 36, 34, 7, 6, 39, 42, 32, 41, 23, 22, 21, 28, 10, 43, 27, 20, 37, 5, 44, 8, 16, 25, 2, 11, 35), 2)

if __name__ == '__main__':
    main()
