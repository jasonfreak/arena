from functools import wraps

def memo(func):
    cache = {}
    miss = object()

    @wraps(func)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = func(*args)
            cache[args] = result
        return result

    return wrapper

class JanuszInTheCasino(object):
    def __init__(self):
        object.__init__(self)

    @memo
    def findProbability(self, n, m, k):
#        print 'debug[23]', n, k
        if n == 0:
            return 0
        if k == 0:
            return 1

        cntOfTokenByEachField = n / m
        cntOfLargerField = n % m
        fields = (cntOfTokenByEachField+1, ) * cntOfLargerField + (cntOfTokenByEachField, ) * (m - cntOfLargerField)

#        print 'debug[28]', cntOfTokenByEachField, cntOfLargerField, fields

        result = 0
        for field in fields:
            result = result + (1.0 / m) * self.findProbability(n-field, m, k-1)
#        print 'debug[36]', n, k, result
        return result

def main():
    obj = JanuszInTheCasino()
#    print obj.findProbability(3, 2, 2)
#    print obj.findProbability(1, 3, 3)
    print obj.findProbability(4, 3, 2)
#    print obj.findProbability(1000000000000, 2, 40)

if __name__ == '__main__':
    main()
