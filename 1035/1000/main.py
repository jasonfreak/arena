from math import sqrt

class NoRightTurnDiv2(object):
    def __init__(self):
        object.__init__(self)

    def innerProduct(self, base, a, b):
        va = (a[0] - base[0], a[1] - base[1])
        vb = (b[0] - base[0], b[1] - base[1])
        return va[0] * vb[0] - va[1] * vb[1]

    def outerProduct(self, base, a, b):
        va = (a[0] - base[0], a[1] - base[1])
        vb = (b[0] - base[0], b[1] - base[1])
        return va[0] * vb[1] - va[1] * vb[0]

    def distance(self, base, a):
        return sqrt(pow(base[0] - a[0], 2) + pow(base[1] - a[1], 2))

    def findPath(self, x, y):
        cntOfPoint = len(x)
        base = (x[0], y[0])
        for i in range(1, cntOfPoint):
            if y[i] < base[1] or (y[i] == base[1] and x[i] < base[0]):
                base = (x[i], y[i])

        index = {}
        rank = {}
        xaxis = (base[0] + 1, base[1])
        for i in range(cntOfPoint):
            point = (x[i], y[i])
            index[point] = i
            if base != point:
                ip = self.innerProduct(base, xaxis, point)
                rank[ip] = point

        sortedRank = sorted(rank, reverse=True)

        last1 = base
        last2 = rank[sortedRank[0]]
        count = 2
        result = (index[last1], index[last2])
        for ip in sortedRank[1:]:
            if self.outerProduct(last1, last2, rank[ip]):
                result += (index[rank[ip]],)
                last1 = last2
                last2 = rank[ip]
            else:
                return tupe()
            
        return result

def main():
    obj = NoRightTurnDiv2()
    print obj.findPath((-10, 0, 10), (10, -10, 10))

if __name__ == '__main__':
    main()
