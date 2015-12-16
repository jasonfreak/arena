#from functools import wraps
#from itertools import permutations
#from itertools import combinations
#from sys import maxint
from copy import deepcopy
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

class CampLunch(object):
    def __init__(self):
        object.__init__(self)

    def countByRecursion(self, N, M, a, head, seats):
        print 'debug[25]', head, seats
        if head == N * M - 1:
            print 'debug[27]'
            return 1
        ret = 0
        x = head / M
        y = head % M
        print 'debug[30]', x, y
        right = x * M + y + 1
        if y + 1 < M and seats[right]:
            new_seats = deepcopy(seats)
            pre = new_seats[head]['pre']
            pro = new_seats[head]['pro']
            new_seats[pre]['pro'] = pro
            new_seats[pro]['pre'] = pre
            pre = new_seats[right]['pre']
            pro = new_seats[right]['pro']
            new_seats[pre]['pro'] = pro
            new_seats[pro]['pre'] = pre
            new_head = new_seats[new_seats[head]['pre']]['pro']
            new_seats[head] = None
            new_seats[right] = None
            ret += self.countByRecursion(N, M, a, new_head, new_seats)

        down = (x+1) * M + y
        if x + 1 < N and a[x][y] == a[x+1][y] and seats[down]:
            new_seats = deepcopy(seats)
            print 'debug[52]', new_seats
            pre = new_seats[head]['pre']
            pro = new_seats[head]['pro']
            new_seats[pre]['pro'] = pro
            new_seats[pro]['pre'] = pre
            print 'debug[56]', new_seats
            pre = new_seats[down]['pre']
            pro = new_seats[down]['pro']
            new_seats[pre]['pro'] = pro
            new_seats[pro]['pre'] = pre
            print 'debug[61]', new_seats
            new_head = new_seats[new_seats[head]['pre']]['pro']
            new_seats[head] = None
            new_seats[down] = None
            ret += self.countByRecursion(N, M, a, new_head, new_seats)

        new_seats = deepcopy(seats)
        pre = new_seats[head]['pre']
        pro = new_seats[head]['pro']
        new_seats[pre]['pro'] = pro
        new_seats[pro]['pre'] = pre
        new_head = new_seats[new_seats[head]['pre']]['pro']
        new_seats[head] = None
        ret += self.countByRecursion(N, M, a, new_head, new_seats)
        return ret

    def count(self, N, M, a):
        seats = []
        for i in range(N):
            for j in range(M):
                seat = i * M + j
                seats.append({'pre':seat-1, 'pro':seat+1})
        head = 0
        
        return self.countByRecursion(N, M, a, head, seats)

def main():
    obj = CampLunch()
    print obj.count(2, 2, ('AB', 'AB'))

if __name__ == '__main__':
    main()
