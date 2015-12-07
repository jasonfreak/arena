class OkonomiyakiParty(object):
    def __init__(self):
        object.__init__(self)

    def A(self, m, n):
        return reduce(lambda x, y: x * y, range(n, n-m, -1), 1)

    def C(self, m, n):
        return self.A(m, n) / self.A(m, m)

    def exceptCount(self, result, begin, end, sortedOsize, M, K):
#        print 'debug[12]', begin, end
        if end - begin + 1 >= M and sortedOsize[end] - sortedOsize[begin] > K and (begin, end) not in result:
            result[(begin, end)] = self.C(M-2, end-begin-1)
            self.exceptCount(result, begin+1, end, sortedOsize, M, K)
            self.exceptCount(result, begin, end-1, sortedOsize, M, K)

    def count(self, osize, M, K):
        cntOfOsize = len(osize)
        sortedOsize = sorted(osize)
        allCount = self.C(M, cntOfOsize)
#        print 'debug[15]', allCount, sortedOsize

        begin = 0
        end = cntOfOsize - 1
        result = {}
        self.exceptCount(result, begin, end, sortedOsize, M, K)
#        print 'debug[28]', result

        return (allCount - sum(result.values())) % 1000000007
            
def main():        
    obj = OkonomiyakiParty()
#    print obj.count((1, 4, 6, 7, 9), 2, 3)
#    print obj.count((1,6,2,7,4,2,6,1,5,2,4), 4, 3)
    print obj.count((10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000), 25, 1)

if __name__ == '__main__':
    main()
