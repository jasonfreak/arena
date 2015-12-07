from itertools import combinations

class JanuszTheBusinessman(object):
    def __init__(self):
        object.__init__(self)

    def isSatisfied(self, cb, arrivals, departures):
#        print 'debug[8]', cb
#        raw_input()
        cntOfCb = len(cb)
        cntOfGuest = len(arrivals)
        for i in range(cntOfGuest):
            j = 0
            while j < cntOfCb:
                if arrivals[cb[j]] <= arrivals[i] and arrivals[i] <= departures[cb[j]]:
                    break
                if arrivals[cb[j]] <= departures[i] and departures[i] <= departures[cb[j]]:
                    break
                j = j + 1
#            print 'debug[16]', j, cntOfCb
            if j == cntOfCb:
                return False
        return True

    def makeGuestsReturn(self, arrivals, departures):
        cntOfGuest = len(arrivals)
        index = range(cntOfGuest)
        sortedIndex = sorted(index, key=lambda x:arrivals[x])
        sortedArrivals = [arrivals[i] for i in sortedIndex]
        sortedDeparture = [departures[i] for i in sortedIndex]
#        print 'debug[28]', sortedIndex, sortedArrivals, sortedDeparture
        for i in range(1, cntOfGuest+1):
            cbs = combinations(index, i)
            for cb in cbs:
                if self.isSatisfied(cb, sortedArrivals, sortedDeparture):
                    return i

def main():
    obj = JanuszTheBusinessman()
#    print obj.makeGuestsReturn((2, 10, 6), (6, 11, 9))
#    print obj.makeGuestsReturn((2, 10, 23, 34, 45, 123, 1), (25, 12, 40, 50, 48, 187, 365))
#    print obj.makeGuestsReturn((124, 328, 135, 234, 347, 124, 39, 99, 116, 148), (237, 335, 146, 246, 353, 213, 197, 215, 334, 223))
    print obj.makeGuestsReturn((8, 12, 20, 30, 54, 54, 68, 75), (13, 31, 30, 53, 55, 70, 80, 76))

if __name__ == '__main__':
    main()
