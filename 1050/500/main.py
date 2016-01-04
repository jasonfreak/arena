from functools import wraps
#from itertools import permutations
#from itertools import combinations
#from sys import maxint
#
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

class Privateparty(object):
    def __init__(self):
        object.__init__(self)

    def isCome(self, a, unInvited, guest):
        for g in unInvited:
            if a[g] == guest:
                return False
        return True

    @memo
    def getexpByRecursion(self, a, unInvited):
        print 'debug[31]', unInvited
        ret = 0.0
        cntOfUnInvited = len(unInvited)
        if cntOfUnInvited == 1:
            ret = 1
        else:
            for i in range(cntOfUnInvited):
                newUnInvited = unInvited[:i] + unInvited[i+1:]
                ret += self.getexpByRecursion(a, newUnInvited)
                if self.isCome(a, newUnInvited, unInvited[i]):
                    ret += 1
            ret /= cntOfUnInvited
        print 'debug[42]', ret, unInvited
        return ret

    def getexp(self, a):
        cntOfGuest = len(a)
        unInvited = tuple(range(cntOfGuest))
        return self.getexpByRecursion(a, unInvited)

def main():
    obj = Privateparty()
#    print obj.getexp((0, 1))
#    print obj.getexp((0, 0))
#    print obj.getexp((0, 1, 1))
    print obj.getexp((0, 1, 1, 2))

if __name__ == '__main__':
    main()
