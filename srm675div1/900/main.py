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

class classname(object):
    def __init__(self):
        object.__init__(self)

    def funcname(self, ):
        return

def main():
    obj = classname()
    print obj.funcname()

if __name__ == '__main__':
    main()
