#from functools import wraps
#from itertools import permutations
#from itertools import combinations
#from sys import maxint
#
#def memo(func):
#    cache = {}
#    miss = object()
#
#    @wraps(func)
#    def wrapper(*args):
#        result = cache.get(args, miss)
#        if result is miss:
#            result = func(*args)
#            cache[args] = result
#        return result
#    return wrapper

class ApplesAndOrangesEasy(object):
    def __init__(self):
        object.__init__(self)

    def maximumApples(self, N, K, info):
        apple = 1
        orange = 0
        fruitsEaten = []
        cntOfApple = 0
        maxOfApple = K / 2

        cur = 1
        while cur <= N:
#            print 'debug[31]', cntOfApple, fruitsEaten
            cntOfFruitsEaten = len(fruitsEaten)
            fruit = apple
            if cntOfApple == maxOfApple:
                if cntOfFruitsEaten < K or (cntOfFruitsEaten >= K and fruitsEaten[K-1] == orange):
                    if cur in info:
                        i = 0
                        while fruitsEaten[i] == orange or (fruitsEaten[i] == apple and (cntOfFruitsEaten - i) in info):
                            i += 1
                        fruitsEaten[i] = orange
                        cntOfApple -= 1
                    else:
                        fruit = orange
#            print 'debug[43]', cntOfApple, fruitsEaten
#            print 'debug[44]', fruit
            fruitsEaten.insert(0, fruit)
            if fruit == apple:
                cntOfApple += 1
            if len(fruitsEaten) > K and fruitsEaten[K] == apple:
                cntOfApple -= 1
            cur += 1

#        print 'debug[53]', cntOfApple, fruitsEaten
        ret = sum(fruitsEaten)
        return ret

def main():
    obj = ApplesAndOrangesEasy()
#    print obj.maximumApples(3, 2, ())
#    print obj.maximumApples(10, 3, (3, 8))
#    print obj.maximumApples(9, 4, (1, 4))
#    print obj.maximumApples(9, 4, (2, 4))
    print obj.maximumApples(23, 7, (3, 2, 9, 1, 15, 23, 20, 19))

if __name__ == '__main__':
    main()
