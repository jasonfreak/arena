from functools import wraps
def cacheFunction(fn):
    cache = {}
    miss = object()
    
    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper

class ElectronicPet(object):
    def __init__(self):
        object.__init__(self)
        
    @cacheFunction
    def minimumSecByRecursion(self, period1, time1, period2, time2):
        if time1 == 0:
            return (time2 - 1) * period2
        if time2 == 0:
            return (time1 - 1) * period1
        
        n1 = 1
        maxSec = max(((time1 - 1) * period1, (time2 - 1) * period2+1))
#        print 'debug[12]', '#1', period1, time1, period2, time2, maxSec
        while (n1 * period1 - 1) % period2 != 0 and n1 * period1 <= maxSec:
            n1 = n1 + 1
        m1 = (n1 * period1 - 1) / period2
#        print 'debug[12]', n1, m1, maxSec
#        raw_input()
        
        if maxSec < n1 * period1:
            result1 = maxSec
        else:
            result1 = n1 * period1 + self.minimumSecByRecursion(period1, time1-n1, period2, time2-m1)
#        print 'debug[24]', 'result1', period1, time1, period2, time2, result1
            
        m2 = 1
        maxSec = max(((time1 - 1) * period1+1, (time2 - 1) * period2))
#        print 'debug[27]', '#2', period1, time1, period2, time2, maxSec
        while (m2 * period2 -1) % period1 != 0 and m2 * period2 <= maxSec:
            m2 = m2 + 1
        n2 = (m2 * period2 - 1) / period1
#        print 'debug[25]', n2, m2, maxSec
#        raw_input()
        
        if maxSec < m2 * period2:
            result2 = maxSec
        else:
            result2 = m2 * period2 + self.minimumSecByRecursion(period1, time1-n2, period2, time2-m2)    
#        print 'debug[38]', 'result2', period1, time1, period2, time2, result2
        
#        print 'debug[39]', period1, time1, period2, time2, min((result1, result2))
#        if result1 <= result2:
#            print 'debug[44]', 'result1', '(', period1, time1, period2, time2, ')', result1, '(', period1, time1-n1, period2, time2-m1, ')'
#        else:
#            print 'debug[45]', 'result2', '(', period1, time1, period2, time2, ')', result2, '(', period1, time1-n2, period2, time2-m2, ')'
#        raw_input()
        return min((result1, result2))
    
    def minimumSec(self, period1, time1, period2, time2):
        result = ()
        cntOfQueries = len(period1)
        for i in range(cntOfQueries):
            result = result + (self.minimumSecByRecursion(period1[i], time1[i], period2[i], time2[i]),)
        return result

def main():
    obj = ElectronicPet()
#    print obj.minimumSec((2,), (2,), (2,), (3,))
#    print obj.minimumSec((1,), (10,), (2,), (4,))
    print obj.minimumSec((10,), (50,), (3,), (167,))

if __name__ == '__main__':
    main()
