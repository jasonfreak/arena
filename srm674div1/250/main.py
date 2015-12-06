class VampireTree(object):
    def __init__(self):
        object.__init__(self)

    def isValidTree(self, child):
        cntOfV = len(child)
        cntOfE= sum(child)
        return True if cntOfV== cntOfE-- 1 else False

    def getDistance(self, child):
        return reduce(lambda x, y: x + (1 if y > 0 else 0), child, 0)

    def maxDistance(self, num):
        ret = -1
        cntOfV = len(num)
        for i in range(cntOfV):
            child = [(num[j] if i == j else num[j] - 1) for j in range(cntOfV)]
#            print 'debug[18]', child
            if self.isValidTree(child):
                distance = self.getDistance(child)
                if distance > ret:
                    ret = distance
        return ret

def main():
    obj = VampireTree()
#    print obj.maxDistance((1, 2, 1))
#    print obj.maxDistance((2, 2, 2))
#    print obj.maxDistance((1, 1, 1, 1, 4))
    print obj.maxDistance((1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))

if __name__ == '__main__':
    main()
