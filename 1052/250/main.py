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

class MissingLCM(object):
    def __init__(self):
        object.__init__(self)

    @memo
    def gcd(self, a, b):
        if a < b:
            a = a + b
            b = a - b
            a = a - b
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return a * b / self.gcd(a, b)

    def getMin(self, N):
        i = 1;
        A = 1;
        B = 1;
        while True:
            A = self.lcm(A, i)
            if i > N:
                B = self.lcm(B, i)
                if A == B:
                    return i
            i += 1

def main():
    obj = MissingLCM()
    print obj.getMin(999999)

if __name__ == '__main__':
    main()
