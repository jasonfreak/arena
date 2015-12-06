from sys import maxint
from functools import wraps

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

class Treestrat(object):
    def __init__(self):
        object.__init__(self)

    @memo
    def roundcntByRecursion(self, isA, tree, boardA, boardB):
        print 'debug[23]', isA, boardA, boardB
        cntOfEdge = len(tree)
        result = maxint
        if isA:
            for i in range(cntOfEdge):
                boardA = list(boardA)
                if boardA[tree[i]] > 0 and boardB[i+1] == 0:
                    boardA[tree[i]] -= 1
                    boardA[i+1] += 1
                    temp = 1 + self.roundcntByRecursion(False, tree, tuple(boardA), boardB)
                    if temp < result:
                        result = temp
                if boardA[i+1] > 0 and boardB[tree[i]] == 0:
                    boardA[i+1] -= 1
                    boardA[tree[i]] += 1
                    temp = 1 + self.roundcntByRecursion(False, tree, tuple(boardA), boardB)
                    if temp < result:
                        result = temp
                if boardB[i+1] > 0 or boardB[tree[i]] > 0: 
                    temp = self.roundcntByRecursion(False, tree, tuple(boardA), boardB)
                    if temp < result:
                        result = temp
        else:
            for i in range(cntOfEdge):
                if (boardA[tree[i]] > 0 and boardB[i+1] > 0) or (boardB[tree[i]] > 0 and boardA[i+1] > 0):
                    return 1
                else:
                    if boardB[tree[i]] > 0:
                        boardB = list(boardB)
                        boardB[tree[i]] -= 1
                        boardB[i+1] += 1
                        temp = 1 + self.roundcntByRecursion(False, tree, boardA, tuple(boardB))
                        if temp < result:
                            result = temp
                    if boardB[i+1] > 0:
                        boardB = list(boardB)
                        boardB[i+1] -= 1
                        boardB[tree[i]] += 1
                        temp = 1 + self.roundcntByRecursion(False, tree, boardA, tuple(boardB))
                        if temp < result:
                            result = temp
                    if boardA[i+1] > 0 and boardA[tree[i]] > 0: 
                        temp = self.roundcntByRecursion(False, tree, boardA, tuple(boardB))
                        if temp < result:
                            result = temp
                    
        return result
        

    def roundcnt(self, tree, A, B):
        cntOfVertex = len(tree) + 1
        boardA = [0] * cntOfVertex
        for v in A:
            boardA[v] += 1
        boardB = [0] * cntOfVertex
        for v in B:
            boardB[v] += 1

        return self.roundcntByRecursion(True, tree, tuple(boardA), tuple(boardB))

def main():
    obj = Treestrat()
#    print obj.roundcnt((0,), (0,), (1,))
#    print obj.roundcnt((0,1), (1,), (2,))
    print obj.roundcnt((0,0,0,3,4), (2,), (1,))

if __name__ == '__main__':
    main()
