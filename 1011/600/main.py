from functools import wraps

def cacheFunction(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper
    
class NumberGameAgain(object):
    def __init__(self):
        object.__init__(self)

    def nextForbiddenIndex(self, k, table, i):
#        print 'debug[22]', k, i
        cntOfForbiddenNums = len(table)
        index = i + 1
        while index < cntOfForbiddenNums and table[index] <= k:
#            print 'debug[26]', k, table[index], index, cntOfForbiddenNums
            index = index + 1
#        print 'debug[28]', index - 1
        return index - 1

    @cacheFunction
    def solveByRecursion(self, k, end, table, i):
        cntOfForbiddenNums = len(table)
#        print 'debug[33]', k, i, cntOfForbiddenNums
        if (i != -1 and i < cntOfForbiddenNums and k == table[i]) or k > end:
            return 0
        else:
            return (1 if k > 1 else 0) + self.solveByRecursion(k*2, end, table, self.nextForbiddenIndex(k*2, table, i)) + self.solveByRecursion(k*2+1, end, table, self.nextForbiddenIndex(k*2+1, table, i))

    def solve(self, k, table):
        return self.solveByRecursion(1, pow(2, k)-1, tuple(sorted(table)), -1)

def main():
    obj = NumberGameAgain()
#    print obj.solve(3, (2, 4, 6))
#    print obj.solve(5, ())
    print obj.solve(40, (2,4,8,16,32141531,2324577,1099511627775,2222222222,33333333333,4444444444,2135))

if __name__ == '__main__':
    main()
