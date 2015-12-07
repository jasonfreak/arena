from functools import wraps

def memo(func):
    cache = {}
    miss = object()

    @wraps(func)
    def wrapper(*args):
        ret = cache.get(args)
        if ret is miss:
            ret = func(*args)
            cache[args] = ret
        return ret
    return wrapper

class RandomPancakeStack(object):
    def __init__(self):
        object.__init__(self)

    @memo
    def getExpectedByRecursion(self, d, i, n, p, v): 
#        print 'debug[21]', i, n, p, v
        w = v + d[i]
        if i == 0:
            ret = p * w
        else:
            ret = p * w * (n - i - 1) / (n - 1)
#            print 'debug[28]', ret, p, w, n, i
            j = i - 1
            m = n - 1
            q = p / (n - 1)
#            print 'debug[31]', p, n, q
            while j >= 0:
                ret += self.getExpectedByRecursion(d, j, m, q, w)
                j -= 1
#        print 'debug[35]', i, n, p, v, '####', ret
        return ret

    def expectedDeliciousness(self, d):
        ret = 0
        cntOfPancake = len(d)
        for i in range(cntOfPancake):
            ret += self.getExpectedByRecursion(d, i, cntOfPancake, 1.0/cntOfPancake, 0)
        
        return ret

def main():
    obj = RandomPancakeStack()
#    print obj.expectedDeliciousness((1, 1, 1))
#    print obj.expectedDeliciousness((3,6,10,9,2))
    print obj.expectedDeliciousness((10,9,8,7,6,5,4,3,2,1))

if __name__ == '__main__':
    main()
