from copy import copy

class SquareScores(object):
    def __init__(self):
        object.__init__(self)

    def getP(self, p):
        base = ord('a')
        cntOfP = len(p)
        ret = dict()
        for i in range(cntOfP):
            ret[chr(base+i)] = float(p[i]) / 100
        return ret

    def getScore(self, s):
        ret = 0
        cntOfLetter = len(s)
        head = 0
        while head < cntOfLetter:
            tail = head + 1
            while tail < cntOfLetter:
                if s[head] == s[tail]:
                    tail += 1
                else:
                    break
            length = tail - head
#            print 'debug[28]', head, tail
            ret += length * (length + 1) / 2
            head = tail 
        return ret

    def calcexpectation(self, p, s):
        ret = 0
        cntOfP = len(p)
        p = self.getP(p)
        keys = p.keys()
        cntOfLetter = len(s)
        indexes = []
        for i in range(cntOfLetter):
            if s[i] == '?':
                indexes.append(i)

        cntOfUnknown = len(indexes)
        for i in xrange(pow(cntOfP, cntOfUnknown)):
            pc = 1
            temp = copy(s)
            num = i
            for j in range(cntOfUnknown):
                base = num % cntOfP
                num = num / cntOfP
                pc *= p[keys[base]]
                temp = temp[:indexes[j]] + keys[base] + temp[indexes[j]+1:]
#            print 'debug[52]', temp
            ret += pc * self.getScore(temp)

        return ret

def main():
    obj = SquareScores()
#    print obj.calcexpectation((1, 99), 'aaaba')
#    print obj.calcexpectation((10, 20, 70), 'aa?bbbb')
    print obj.calcexpectation((10, 20, 30, 40), 'a??c?dc?b')

if __name__ == '__main__':
    main()
