from sys import maxint

class TheKingsTree(object):
    def __init__(self):
        object.__init__(self)

    def cntOfRedAndGreen(self, cntOfCostOfEach, node, child, color):
#        print 'debug[8]', node, cntOfCostOfEach, child, color
#        raw_input()
        cntOfRed = cntOfGreen = 0
        for c in child[node]:
            r, g = self.cntOfRedAndGreen(cntOfCostOfEach, c, child, color)
            cntOfRed = cntOfRed + r
            cntOfGreen = cntOfGreen + g
#           print 'debug[18]', node, cntOfRed, cntOfGreen
        cntOfCostOfEach.append((1+cntOfRed) if color[node] == 'R' else (1+cntOfGreen))
        return (1+cntOfRed, cntOfGreen) if color[node] == 'R' else (cntOfRed, 1+cntOfGreen)

    def cost(self, node, child, color):
        result = []
        self.cntOfRedAndGreen(result, node, child, color)
#        print 'debug[25]', result
        return sum(result)

    def child(self, parent):
        child = {0:()}
        cntOfNode = len(parent)
        for i in range(cntOfNode):
            child[parent[i]] = child.get(parent[i], ()) + (i+1,)
            child[i+1] = child.get(i+1, ())
        return child
        
    def getNumber(self, parent):
        result = maxint
        cd = self.child(parent)
        RedAndGreen = ('R', 'G')
        cntOfColor = len(RedAndGreen)
        cntOfNode = len(parent) + 1
        poss = cntOfNode * [-1]
        cur = 0
        while cur >= 0:
            poss[cur] = poss[cur] + 1
            if poss[cur] == cntOfColor:
                poss[cur] = -1
                cur = cur - 1
            else:
                if cur == cntOfNode - 1:
                    color = [RedAndGreen[poss[i]] for i in range(cntOfNode)]
                    ct = self.cost(0, cd, color)
#                    print 'debug[51]', color, ct
                    if ct < result:
                        result = ct
                else:
                    cur = cur + 1
        return result

def main():
    obj = TheKingsTree()
#    print obj.getNumber((0, 0, 0))
#    print obj.getNumber((0, 1, 2, 3, 4))
    print obj.getNumber(())

if __name__ == '__main__':
    main()
