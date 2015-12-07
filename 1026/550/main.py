class KitayutaMart(object):
    def __init__(self):
        object.__init__(self)

    def lastPrice(self, N, K):
        result = 0
        indexes = range(K)
        cntOfApple = [0] * K
        price = lambda x: reduce(lambda y, z: y + pow(2, z), range(x), 0)
        for i in xrange(N):
            index = min(indexes, key=lambda x: price(cntOfApple[x]+1)*(x+1))
#            print 'debug[12]', index, cntOfApple
            cntOfApple[index]+=1
            temp = pow(2, cntOfApple[index]-1)*(index+1)
            if temp > result:
                result = temp
        return result

def main():
    obj = KitayutaMart()
    print obj.lastPrice(1000000000, 1)
#    print obj.lastPrice(3, 2)

if __name__ == '__main__':
    main()
