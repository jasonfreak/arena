class TheKingsFactorization(object):
    def __init__(self):
        object.__init__(self)

    def getVector(self, N, primes):
        result = ()
        cntOfPrimes = len(primes)
        cur = 0
        for i in range(0, cntOfPrimes-1):
            N = N / primes[i]
            j = primes[i]
            while  j <= primes[i+1]:
                if N % j == 0:
                    N = N / j
                    break
                j = j + 1
            result = result + (primes[i], j)
        result = result + (primes[cntOfPrimes-1],)
        N = N / primes[cntOfPrimes-1]
#        print 'debug[18]', N, primes[cntOfPrimes-1]

        if N > 1:
            j = primes[cntOfPrimes-1]
            while j <= N:
                if N % j == 0:
                    N = N / j
                    break
                j = j + 1
            result = result + (j,)

        return result

def main():
    obj = TheKingsFactorization()
    print obj.getVector(747175606, (2,))

if __name__ == '__main__':
    main()
