class LuckyCycle(object):
    def __init__(self):
        object.__init__(self)

    def find(self, result, route, begin, end, graph):
        if not begin in route:
            route = route + (begin,)
            cntOfNode = len(graph)
            if begin == end:
                result.append(route)
            else:
                for j in range(cntOfNode):
                    if graph[begin][j] > 0:
                        self.find(result, route, j, end, graph)

    def getCycle(self, begin, end, graph):
        cycle = []
        self.find(cycle, (), begin, end, graph)
        return cycle[0]

    def getGraph(self, edge1, edge2, weight):
        cntOfNode = len(edge1) + 1
        result = []
        for i in range(cntOfNode):
            row = []
            for j in range(cntOfNode):
                row.append(0)
            result.append(row)

        for i in range(cntOfNode-1):
#            print 'debug[25]', edge1[i]-1, edge2[i]-1
            result[edge1[i]-1][edge2[i]-1] = weight[i]
            result[edge2[i]-1][edge1[i]-1] = weight[i]
        return result

    def isEven(self, cycle, graph, isFour):
        cntOfNode = len(cycle)
        if cntOfNode % 2 != 0:
            return False

        cntOf4 = 1 if isFour else 0
        cntOf7 = 1 if not isFour else 0

        for i in range(cntOfNode-1):
            if graph[cycle[i]][cycle[i+1]] == 4:
                cntOf4 = cntOf4 + 1
            elif graph[cycle[i]][cycle[i+1]] == 7:
                cntOf7 = cntOf7 + 1

        return True if cntOf4 == cntOf7 else False

    def getEdge(self, edge1, edge2, weight):
        cntOfNode = len(edge1) + 1
        graph = self.getGraph(edge1, edge2, weight)
#        print 'debug[47]', graph
        for i in range(cntOfNode):
            for j in range(cntOfNode):
                if i != j and graph[i][j] == 0:
                    cycle = self.getCycle(i, j, graph)
#                    print 'debug[59]', i, j, cycle
                    if self.isEven(cycle, graph, True):
                        return (i+1, j+1, 4)
                    elif self.isEven(cycle, graph, False):
                        return (i+1, j+1, 7)
        return ()


def main():
    obj = LuckyCycle()
#    print obj.getEdge((1,), (2,), (4,))
    print obj.getEdge((1, 3, 2, 4), (2, 2, 4, 5), (4, 7, 4, 7))

if __name__ == '__main__':
    main()

