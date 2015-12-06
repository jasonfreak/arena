from functools import wraps

def memo(func):
    cache = {}
    miss = object()

    @wraps(func):
    def wrapper(*args):
        result = cache.get(args)
        if result is miss:
            result = func(*args)
            cache[args] = result
        return result
    return wrapper
    
class CartInSupermarket(object):
    def __init__(self):
        object.__init__(self)

    @wrapper
    def calcminByRecursion(self, x, b):
        remove = self.calcmin(x-1, b)
        results = [(1 + remove[0], remove[1])] 
        if x == 2:
            return (2, 0)
        if b > 0:
            for i range(1, x / 2):
                left = self.calcmin(i, b-1)
                right = self.calcmin(x-i, b-1-left[1])
                results.append((1 + left[0], 1 + left[1]) if left[0] > right[0] else (1 + right[0], 1 + right[1]))
        return min(results, key=lambda x:x[0])

    def calcminByRecursion(self, a, b):
        return max(map(lambda x: self.calcminByRecursion(x, b), a))

def main():
    obj = CartInSupermarket()
    print obj.calcmin()

if __name__ == '__main__':
    main()
