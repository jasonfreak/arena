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

class TreeAndPathLength3(object):
    def __init__(self):
        object.__init__(self)

    def cal(self, tree, child):
#        print 'debug[25]', child, tree
        ret = 0
        for i in tree[child]:
            for j in tree[i]:
                if j != child:
                    for k in tree[j]:
                        if k != i:
                            ret += 1
        return ret

    def addNode(self, tree, cntOf3SimplePath, parent, child):
#        print 'debug[35]', cntOf3SimplePath, parent, child, tree
        new_tree = deepcopy(tree)
        new_tree[parent].add(child)
        new_tree[child] = set([parent])
        new_cntOf3SimplePath = cntOf3SimplePath + self.cal(new_tree, child)
#        print 'debug[41]', new_cntOf3SimplePath, new_tree
        return new_tree, new_cntOf3SimplePath

    def getRet(self, tree):
        ret = tuple()
        for node in tree.keys():
            for child in tree[node]:
                ret += (node, child)
                tree[child].remove(node)
            
        return ret

    def construct(self, s):
        cntOf3SimplePath = 1
        tree = {0: set([1]), 1: set([0, 2]), 2: set([3, 1]), 3: set([2])}
        if cntOf3SimplePath == s:
            return self.getRet(tree)
        for i in range(4, 500):
            tmp_cntOf3SimplePath = cntOf3SimplePath
            tmp_tree = None
            for node in tree:
                new_tree, new_cntOf3SimplePath = self.addNode(tree, cntOf3SimplePath, node, i)
                if new_cntOf3SimplePath == s:
                    return self.getRet(new_tree)
                if new_cntOf3SimplePath < s and new_cntOf3SimplePath > tmp_cntOf3SimplePath:
                    tmp_cntOf3SimplePath = new_cntOf3SimplePath
                    tmp_tree = new_tree
            cntOf3SimplePath = tmp_cntOf3SimplePath
            tree = tmp_tree

def main():
    obj = TreeAndPathLength3()
    print obj.construct(6)

if __name__ == '__main__':
    main()
