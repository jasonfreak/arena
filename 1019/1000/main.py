from copy import copy
from itertools import combinations

class TreeCutting(object):
    def __init__(self):
        object.__init__(self)

    def connectedComponent(self, par):
#        print 'debug[9]', par
        result = {}
        cntOfEdge = len(par)
        result[0] = set((0,))
        for i in range(cntOfEdge):
#            print 'debug[13]', result
            if par[i] < 0:
                result[i+1] = result.get(i+1, set((i+1,)))
            else:
#                print 'debug[17]', result.get(par[i], set((par[i],))), result.get(i+1, set((i+1,))) 
                result[par[i]] = result.get(par[i], set((par[i],))).union(result.get(i+1, set((i+1,))))
                for j in result[par[i]]:
                    result[j] = result[par[i]]
        return result

    def isValid(self, par, num):
        ccs = self.connectedComponent(par)
#        print 'debug[23]', ccs
#        raw_input()
        for cc in ccs:
            cntOfCC = len(ccs[cc])
#            print 'debug[30]', cntOfCC
            cntOfInteger = 0
            for i in ccs[cc]:
                if cntOfInteger > 1:
                    return False
                if num[i] > 0 and num[i] == cntOfCC:
                    cntOfInteger = cntOfInteger + 1
            if cntOfInteger == 0:
                return False
        return True

    def can(self, par, num):
        par = list(par)
        cntOfEdge = len(par)
        index = range(cntOfEdge)
        for i in range(0, cntOfEdge+1):
            cbs = combinations(index, i)
            for cb in cbs:
                new = copy(par)
                for i in cb:
                    new[i] = -1
                if self.isValid(new, num):
                    return 'POSSIBLE'

        return 'IMPOSSIBLE'

def main():
    obj = TreeCutting()
#    print obj.can((0, 1, 2, 2, 2), (3, -1, -1, 3, -1, -1))
    print obj.can((), (1,))

if __name__ == '__main__':
    main()
