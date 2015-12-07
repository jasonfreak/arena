from functools import wraps
from sys import maxint

def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result
    return wrapper

class CandleTimer(object):
    def __init__(self):
        object.__init__(self)

    def degrees(self, A, B, length):
        cntOfCandles = len(length)
        nodes = {}
        for i in range(cntOfCandles):
            nodes[A[i]] = nodes.get(A[i], 0) + 1 if length[i] > 0 else 0
            nodes[B[i]] = nodes.get(B[i], 0) + 1 if length[i] > 0 else 0
        return nodes

    @memo
    def getTimeByRecursion(self, A, B, length, nodes):
#        print 'debug[30]', A, B, length, nodes
        cntOfCandles = len(length)
        cntOfExtinguishedCandles = sum([1 if x > 0 else 0 for x in length])
        cntOfNodes = len(nodes)
        cntOfIgnitedNodes = sum([1 if x else 0 for x in nodes])

        if cntOfExtinguishedCandles == 0:
            return 0
        if cntOfExtinguishedCandles == 1:
            for i in range(cntOfCandles):
                if length[i] > 0:
                    break
            if nodes[A[i]] and nodes[B[i]]:
                return float(sum(length)) / 2

        minLength = maxint
        for i in range(cntOfCandles):
            if (nodes[A[i]] or nodes[B[i]]) and 0 < length[i] and length[i] < minLength:
                minLength = length[i]

        new_length = list(length)
        new_nodes = list(nodes)
        for i in range(cntOfCandles):
            if nodes[A[i]] or nodes[B[i]]:
                if new_length[i] > 0:
                    new_length[i] = new_length[i] - minLength
                    if new_length[i] == 0:
                        new_nodes[A[i]] = True
                        new_nodes[B[i]] = True
        
        return minLength + self.getTimeByRecursion(A, B, tuple(new_length), tuple(new_nodes))

    def differentTime(self, A, B, length):
        times = {}
        dgs = self.degrees(A, B, length)
        cntOfNodes = len(dgs)
        leaves = filter(lambda x:dgs[x] == 1, dgs)
#        print 'debug[69]', leaves
        cntOfLeaves = len(leaves)

        for r in range(1, cntOfLeaves+1):
            cur = 0
            poss = range(-1, r-1)
            while cur >= 0:
                poss[cur] = poss[cur] + 1
                if poss[cur] == cntOfLeaves:
                    for i in range(cur, r):
                        poss[i] = poss[i-1] + 1
                    cur = cur - 1
                else:
                    if cur == r - 1:
#                        print 'debug[84]', poss
                        nodes = [False] * cntOfNodes
                        for i in range(r):
                            nodes[leaves[poss[i]]] = True
                        time = self.getTimeByRecursion(A, B, length, tuple(nodes))
#                        print 'debug[89]', time
                        times[time] = times.get(time, 0) + 1
                    else:
                        cur = cur + 1

#        print 'debug[93]', times
        return len(times)

def main():
    obj = CandleTimer()
#    print obj.differentTime((0, 1), (1, 2), (10, 1))
#    print obj.differentTime((0, 0, 0), (1, 2, 3), (1, 1, 1))
#    print obj.differentTime((0, 0, 0), (1, 2, 3), (1, 2, 3))
#    print obj.differentTime((0,1,1,2,3,3,2,4), (1,2,3,4,5,6,7,8), (5,3,2,4,6,8,7,1))
    print obj.differentTime((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30), (0,1,2,0,0,0,1,0,0,0,2,5,4,7,13,13,6,15,11,18,19,21,22,16,19,19,20,18,22,27), (59,58,147,169,34,14,150,55,156,151,130,109,124,15,100,1,156,16,38,97,99,132,150,18,27,91,110,127,15,105))

if __name__ == '__main__':
    main()
