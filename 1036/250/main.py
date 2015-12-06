class CountryGroupHard(object):
    def __init__(self):
        object.__init__(self)

    def getNext(self, a, b, i):
        cntOfPeople = len(a)
        j = i + 1
        while j < cntOfPeople:
            if a[j] and not b[j]: break
            j += 1
        return j

    def getPre(self, a, b, i):
        j = i - 1
        while a[i] > i - j and j >= 0:
            if b[j]: break
            j -= 1
        return j + 1

    def getPro(self, a, b, i):
        cntOfPeople = len(a)
        j = i + 1
        while j - i < a[i] and j < cntOfPeople:
            if a[j] and a[j] != a[i]: break
            j += 1
        return j

    def isSufficient(self, b):
        last = -1
        for c in b:
            if c == last and c == 0:
                return False
            last = c
        return True
           
# ret
# 0-sufficient
# 1-insufficient
# 2-invalid
    def getWays(self, a, b, i):
#        print 'debug[37]', i, a, b 
        cntOfPeople = len(a)
        if i == cntOfPeople:
            return 0 if self.isSufficient(b) else 1
        pre = self.getPre(a, b, i)
        pro = self.getPro(a, b, i)
#        print 'debug[43]', pre, pro, a[i]
        if pro - pre < a[i]:
            return 2
        count = 0
        for j in range(pre, pro - a[i] + 1):
            order = max(b) + 1
            nb = b[:j] + [order] * a[i] + b[j+a[i]:]
            ret =  self.getWays(a, nb, self.getNext(a, nb, i))
            if ret == 0:
                count += 1
            elif ret == 1:
                return 1
            else:
                continue
            if count > 1:
                return 1
        return 0

    def solve(self, a):
        cntOfPeople = len(a)
        b = [0] * cntOfPeople
        return 'Sufficient' if 0 == self.getWays(a, b, self.getNext(a, b, -1)) else 'Insufficient'

def main():
    obj = CountryGroupHard()
#    print obj.solve((0,2,3,0,0))
#    print obj.solve((0,2,0))
    print obj.solve((0,3,0,0,3,0))
#    print obj.solve((0,0,3,3,0,0))
#    print obj.solve((2,2,0,2,2))
#    print obj.solve((0, 0, 0))

if __name__ == '__main__':
    main()
