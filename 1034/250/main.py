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

class ThePermutationGame(object):
    def __init__(self):
        object.__init__(self)

    @memo
    def gcd(self, a, b):
        if a < b:
            a += b
            b = a - b
            a = a - b
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)

    def lcm(self, a, b):
        return a * b / self.gcd(a, b)

    def nlcm(self, a):
        cntOfA = len(a)
        result = a[0]
        for i in range(1, cntOfA):
            result = self.lcm(result, a[i])
            result %= 1000000007
        return result

    def findMin1(self, N):
        a = range(N+1)
        for i in xrange(2, (N+1)/2):
            j = 2
            while i*j < (N+1):
                a[i*j] /= a[i]
                j += 1

        print 'debug[13]', a
        result = 1
        for num in a[1:]:
            result *= num
            result %= 1000000007
            
        return result

    def findMin(self, N):
        return self.nlcm(range(1, N+1))
        

def main():
    obj = ThePermutationGame()
#    print obj.findMin1(128)
    print obj.findMin(102)

if __name__ == '__main__':
    main()
