from itertools import combinations

class Fragile2(object):
    def __init__(self):
        object.__init__(self)

    def DFS(self, vertex, graph, isNotVisited):
        cntOfVertex = len(graph)
        for i in range(cntOfVertex):
            if graph[vertex][i] == 'Y' and i in isNotVisited:
                isNotVisited.remove(i)
                self.DFS(i, graph, isNotVisited)

    def cntOfConnectedComponent(self, graph, pair):
        result = 0
        isNotVisited = set()
        cntOfVertex = len(graph)
        for i in range(cntOfVertex):
            isNotVisited.add(i)
        for vertex in pair:
            isNotVisited.remove(vertex)
        while len(isNotVisited) > 0:
            vertex = isNotVisited.pop()
            self.DFS(vertex, graph, isNotVisited)
            result += 1
        return result
            

    def countPairs(self, graph):
        result = 0
        cntOfVertex = len(graph)
        pairs = combinations(range(cntOfVertex), 2)
        cntOfCC1 = self.cntOfConnectedComponent(graph, ()) 
        for pair in pairs:
            cntOfCC2 = self.cntOfConnectedComponent(graph, pair) 
#            print 'debug[32]', pair, cntOfCC1, cntOfCC2
            if cntOfCC1 < cntOfCC2:
                result = result + 1
        return result

def main():
    obj = Fragile2()
#    print obj.countPairs(('NYNN', 'YNYN', 'NYNY', 'NNYN'))
    print obj.countPairs(("NYNNNN", "YNYNNN", "NYNNNN", "NNNNYN", "NNNYNY", "NNNNYN"))

if __name__ == '__main__':
    main()
