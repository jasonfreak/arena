from functools import wraps
from itertools import permutations
from sys import maxint

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


class Mutalisk(object):
    def __init__(self):
        object.__init__(self)
        self.score = (9, 3, 1)

    @memo
    def minimalAttacks(self, x):
#        print 'debug[25]', x
#        raw_input()
        cntOfSCV = len(x)
        arr = filter(lambda i: x[i], range(cntOfSCV))
        cntOfLSCV = min(len(arr), 3)
        if cntOfLSCV == 0:
            return 0
        ps = permutations(arr, cntOfLSCV)
        
        ret = maxint
        for p in ps:
            _x = list(x)
            for i in range(cntOfLSCV):
                _x[p[i]] -= min(_x[p[i]], self.score[i])
            _x = tuple(_x)
            tmp = self.minimalAttacks(_x) + 1
            if tmp < ret:
                ret = tmp
        return ret

def main():
    obj = Mutalisk()
#    print obj.minimalAttacks((54, 18, 6))
#    print obj.minimalAttacks((1,1,1,1,1,1,1,1,1,1))
#    print obj.minimalAttacks((55, 60, 53))
#    print obj.minimalAttacks((60,))
    print obj.minimalAttacks((60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60))

if __name__ == '__main__':
    main()
