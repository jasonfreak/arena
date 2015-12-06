from sys import maxint
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


class OrderOfOperationsDiv2(object):
    def __init__(self):
        object.__init__(self)

    def getTime(self, ins1, ins2):
##        print 'debug[23]', ins1, ins2, map(lambda x, y:1 if y == 1 and x == 0 else 0, ins1, ins2)
        k = sum(map(lambda x, y:1 if y == '1' and x == '0' else 0, ins1, ins2))
        return k * k

    def getLast(self, last, ins):
        result = ''
        cnt = len(last)
        for i in range(cnt):
            result = result + ('1' if last[i] == '1' or ins[i] == '1' else '0')
        return result

    @memo
    def minTimeByRecursion(self, last, s):
#        print 'debug[27]', last, s
        if len(s) == 0:
            return 0
        t = maxint
        cntOfIns = len(s)
        for i in range(cntOfIns):
            tm = self.getTime(last, s[i]) + self.minTimeByRecursion(self.getLast(last, s[i]), tuple(s[:i]+s[i+1:]))
#            print 'debug[27]', last, s, tm
            if tm < t:
                t = tm
        return t

    def minTime(self, s):
        last = '0' * len(s[0])
        return self.minTimeByRecursion(last, s)

def main():
    obj = OrderOfOperationsDiv2()
#    print obj.minTime(('111', '001', '010'))
#    print obj.minTime(("11101", "00111", "10101", "00000", "11000"))
#    print obj.getTime('001', '010')

if __name__ == '__main__':
    main()
