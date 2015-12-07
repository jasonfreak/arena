from sys import maxint
from itertools import combinations

class TheConsecutiveIntegersDivTwo(object):
    def __init__(self):
        object.__init__(self)

    def find(self, numbers, k):
        if k == 1:
            return 0
        result = maxint
        cbs = combinations(numbers, k)
        for cb in cbs:
            op = abs(cb[0]-cb[1]) - 1
            if op < result:
                result = op
        return result

def main():
    obj = TheConsecutiveIntegersDivTwo()
    print obj.find((4, 47, 7), 2)

if __name__ == '__main__':
    main()
