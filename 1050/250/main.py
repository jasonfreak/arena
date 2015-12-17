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

class Coversta(object):
    def __init__(self):
        object.__init__(self)

    def place(self, a, x, y):
        ret = 0
        cntOfRow = len(a)
        cntOfCol = len(a[0])
        cntOfCov = len(x)
        cntOfStation = cntOfRow * cntOfCol
        for i in range(cntOfStation):
            station_a = (i / cntOfCol, i % cntOfCol)
            cover_a = [(station_a[0]+x[k], station_a[1]+y[k]) for k in range(cntOfCov)]
            cover_a = set(filter(lambda s:0<=s[0] and s[0]<cntOfRow and 0<=s[1] and s[1]<cntOfCol, cover_a))
            for j in range(i+1, cntOfStation):
                station_b = (j / cntOfCol, j % cntOfCol)
                cover_b = [(station_b[0]+x[k], station_b[1]+y[k]) for k in range(cntOfCov)]
                cover_b = set(filter(lambda s:0<=s[0] and s[0]<cntOfRow and 0<=s[1] and s[1]<cntOfCol, cover_b))
                cover = cover_a.union(cover_b)
#                print 'debug[38]', cover
                values = [int(a[s[0]][s[1]]) for s in list(cover)]
                value = sum(values)

                if ret < value:
                    ret = value

        return ret

def main():
    obj = Coversta()
#    print obj.place(('11', '11'), (0, 1), (0, 1))
    print obj.place(('53', '10'), (1, 0, -1, 0), (0, 1, 1, 0))

if __name__ == '__main__':
    main()
