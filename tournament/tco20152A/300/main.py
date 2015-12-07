from functools import wraps

def memo(func):
    cache = {}
    miss = object()
    
    @wraps(func)
    def wrapper(args*):
        result = cache.get(args, miss)
        if result is miss:
            result = func(args*)
            cache[args] = result
        return result

class ModModMod(object):
    def __init__(self):
        object.__init__(self)

    def findSum(self, m, R):
