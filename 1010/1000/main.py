from functools import wraps

def cacheFunction(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args[2], miss)
        if result is miss:
            result = fn(*args)
            cache[args[2]] = result
        return result

    return wrapper
    

class TwoNumberGroups(object):
    def __init__(self):
        object.__init__(self)

    @cacheFunction
    def primes(self, pos, n):
#        print 'debug[6]', n
        if n == 1 or n == 0:
            return ()
        else:
            i = pos + 1
            while n % i != 0:
#                print 'debug[12]', n, i
                i = i + 1
            while n % i == 0:
#                print 'debug[33]', n
                n = n / i
            return (i,) + self.primes(i, n)

    def solve(self, A, numA, B, numB):
        result = 0
        cntOfNumsInA = len(A)
        cntOfNumsInB = len(B)
        for i in range(cntOfNumsInA):
            for j in range(cntOfNumsInB):
#                print 'debug[42]', i, j, A[i], B[j]
                result = result + sum(self.primes(1, abs(A[i]-B[j]))) * numA[i] * numB[j]
        return result % 1000000007
                
def main():
    obj = TwoNumberGroups()
#    print obj.solve((1,), (2,), (3, 7), (1, 1))
#    print obj.solve((100,), (2,), (1,), (1,))
#    print obj.solve((5, 1), (1, 1), (12, 999999894), (1, 1))
    print obj.solve((5, 1), (1, 1), (12, 999999894), (1, 1))
#    print obj.solve((1,), (1,), (1,), (100000,))
#    print obj.solve((11795180,41472124,44285836,84280940,117000811,150317409,154188370,167804776,225797581, 240995620,301931440,306528163,327332717,333523124,341325123,350292524,400857064,401290197, 426573408,427972026,448467719,563926065,574489831,579516358,609409829,659343788,678481187, 775710113,806992032,831437250,839580344,842388073,869876247,899553191,902366903,975081878), (1188,1769,1782,1757,1527,4958,3083,4439,3621,3958,2655,2250,2079,3885,3598, 3236,3035,2286,7340,4127,3126,2904,2592,3082,3789,2776,3907,2368,4005,4863, 4482,3307,2459,1436,1656,2007), (11795180,41472124,44285836,84280940,117000811,150317409,154188370,167804776,225797581,240995620, 301931440,306528163,327332717,333523124,341325123,350292524,400857064,401290197,426573408, 427972026,448467719,563926065,574489831,579516358,609409829,659343788,678481187,775710113, 806992032,831437250,839580344,842388073,869876247,899553191,902366903,942362007,975081878), (3024,902,798,2,1426,4959,3082,4439,3622,3958,2653,2249,2081,3884,3599, 3237,3033,2285,7340,4125,3127,2904,2592,3082,3789,2775,3907,2369,4006, 4863,4483,3307,623,2303,2642,1757,2107))

if __name__ == '__main__':
    main()
