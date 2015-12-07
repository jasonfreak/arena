class NarrowPassage2(object):
    def __init__(self):
        object.__init__(self)

    def compute_A(self, n):
        return reduce(lambda x, y: x * y, range(1, n+1), 1)

    def compute_C(self, n, m):
        m = min(m, n-m)
        return reduce(lambda x, y: x * y, range(n-m+1, n+1), 1) / self.compute_A(m)

    def invalid(self, size, maxSizeSum):
        result = []
        cntOfNums = len(size)
        for i in range(cntOfNums-1):
            for j in range(i+1, cntOfNums):
                if size[i]+size[j] > maxSizeSum:
                    result.append((size[j], size[i]))
        return sorted(result, key=lambda x:max(x), reverse = True)

    def getNegativeCountByRecursion(self, cntOfNums, i, pairs, order):
        if i == len(pairs):
            return 0
#        print 'debug[24]', i, order
        cntOfOrderNums = len(order)
        key = max(pairs[i])
        other = min(pairs[i])
        isKeyLeft = True if pairs[0] == key else False
        if cntOfOrderNums == 0:
            result = self.compute_C(cntOfNums, 2) * self.compute_A(cntOfNums-2)
#            print 'debug[31]', result
            result = result + self.getNegativeCountByRecursion(cntOfNums, i+1, pairs, list(pairs[i])[::-1])
        else:
            isOrder = lambda x, y: x >= y if not isKeyLeft else lambda x, y: x <= y
            idx = order.index(key)
            if other in order:
                if not isOrder(order.index(other), idx):
                    return 0
                result = self.compute_C(cntOfNums, cntOfOrderNums) * self.compute_A(cntOfNums-cntOfOrderNums)
#                print 'debug[38]', result
                result = result + self.getNegativeCountByRecursion(cntOfNums, i+1, pairs, order[:])
            else:
                result = (idx+1 if not isKeyLeft else cntOfOrderNums-idx+1) * self.compute_C(cntOfNums, cntOfOrderNums+1) * self.compute_A(cntOfNums-cntOfOrderNums-1)
#                print 'debug[36]', result
                todo = range(0, cntOfOrderNums) if not isKeyLeft else range(0, cntOfOrderNums)[::-1]
                for j in todo:
                    pair = (order[j], other) if not isKeyLeft else (other, order[j])
#                    print 'debug[41]', pair
                    if pair in pairs:
                        return result
                    if isOrder(j, idx):
#                        print 'debug[45]'
                        new = order[:j+1]+[other]+order[j+1:] if not isKeyLeft else order[:j]+[other]+order[j:]
                        result = result + self.getNegativeCountByRecursion(cntOfNums, i+1, pairs, new)
        return result

    def count(self, size, maxSizeSum):
        cntOfNums = len(size)
        pairs = self.invalid(size, maxSizeSum)
#        print 'debug[48]', pairs
        if len(pairs) == 0:
            return self.compute_A(cntOfNums)
        return self.compute_A(cntOfNums) - self.getNegativeCountByRecursion(cntOfNums, 0, pairs, [])

def main():
    obj = NarrowPassage2()
#    print obj.count((1, 2, 3), 4)
#    print obj.count((1,1,1,1,1,1,1,1,1,1,1,1,1), 2)
    print obj.count((2,4,6,1,3,5), 8)

if __name__ == '__main__':
    main()

        

        
