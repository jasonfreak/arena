class MakingTournament(object):
    def __init__(self):
        object.__init__(self)

    def A(self, m, n):
        return reduce(lambda x, y: x * y, range(n, n-m, -1), 1)

    def C(self, m, n):
        return self.A(m, n) / self.A(m, m)

    def howManyWays(self, N, K):
        if K == 0:
            return 1
        minCntOfRoom = pow(2, K-1)
        maxCntOfRoom = N / 2
#        print 'debug[14]', N, K, minCntOfRoom, maxCntOfRoom
        result = 0
        for i in range(minCntOfRoom, maxCntOfRoom+1):
            remain = N - 2 * i
            result = result + self.C(i-1, remain+i-1) * self.howManyWays(i, K-1)
        return result % 1000000007

def main():
    obj = MakingTournament()
#    print obj.howManyWays(6, 2)
#    print obj.howManyWays(8, 3)
#    print obj.howManyWays(10, 2)

if __name__ == '__main__':
    main()
            
