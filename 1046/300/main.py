class OddEvenTree(object):
    def __init__(self):
        object.__init__(self)

    def addDistance(self, d1, d2):
        return 'E' if d1 == d2 else 'O'

    def isValidChild(self, x, node1, node2, node3, children):
        ret = self.addDistance(x[node1][node2], x[node2][node3]) == x[node1][node3]
        for child in children[node3]:
            ret = ret and self.isValidChild(x, node1, node2, child)
        return ret

    def isValidSubTree(self, x, node1, node2, children):
#        print 'debug[15]', node1, node2, children
        ret = True
        for child in children[node2]:
            ret = ret and self.isValidChild(x, node1, node2, child)
#        print 'debug[19]', ret, node1, node2, children
        return ret

    def isValid(self, x, node1, node2, parent, children):
#        print 'debug[21]', node1, node2, parent, children
        ret = True
        node = node1
        while node is not None:
            ret = ret and self.addDistance(x[node][node1], x[node1][node2]) == x[node][node2] and self.isValidSubTree(x, node, node2, children)
            node = parent[node]
#        print 'debug[29]', ret, node1, node2, parent, children 
        return ret

    def getTree(self, x):
        error = (-1,)
        cntOfNode = len(x)
        parent = {}
        children = {}

        for i in range(cntOfNode):
            parent[i] = None
            children[i] = set()
        for i in range(cntOfNode):
            for j in range(i, cntOfNode):
                if x[i][j] != x[j][i]:
                    return error
                if i == j:
                    if x[i][j] == 'O':
                        return error
                elif x[i][j] == 'O':
                    if self.isValid(x, i, j, parent, children):
                        children[i].add(j)
                        parent[j] = i
                    else:
                        return error

        ret = tuple()
        for node in children:
            if children[node]:
                ret += (node, children[node].pop())
        if len(ret) / 2 != cntOfNode - 1:
            return error
                        
        return ret

def main():
    obj = OddEvenTree()
#    print obj.getTree(('EOE', 'OEO', 'EOE'))
#    print obj.getTree(('EO', 'OE'))
#    print obj.getTree(('OO', 'OE'))
#    print obj.getTree(('EO', 'EE'))
#    print obj.getTree(('EOEO', 'OEOE', 'EOEO', 'OEOE'))
    print obj.getTree(('EE', 'EE'))

if __name__ == '__main__':
    main()
