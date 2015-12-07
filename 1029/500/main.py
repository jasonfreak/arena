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

class Times(object):
    def __init__(self, K):
        self.K = K

    def __str__(self):
        return 'times left:%d' % self.K

class CartInSupermarketEasy(object):
    def __init__(self):
        object.__init__(self)

#    @memo
    def calcByRecursion(self, N, times):
#        print 'debug[13]', N, times
#        raw_input()
        if N == 0:
            return 0
        results = [1+self.calcByRecursion(N-1, times)]
        if times.K > 0:
            for i in range(1, N):
                times.K -= 1
                results.append(1+max((self.calcByRecursion(i, times), self.calcByRecursion(N-i, times))))
                times.K += 1
        return min(results)

    def calc(self, N, K):
        times = Times(K)
        return self.calcByRecursion(N, times)

def main():
    obj = CartInSupermarketEasy()
    print obj.calc(15, 4)

if __name__ == '__main__':
    main()
