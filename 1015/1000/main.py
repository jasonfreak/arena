class TallShoes(object):
    def __init__(self):
        object.__init__(self)

    def ways(self, road, current, result, N, X, Y):
#        print 'debug[6]', N, road, current
        cntOfEdges = len(X)
        if current == N - 1:
            result.append(road+[current])
        else:
            if current in road:
                return
            else:
                for i in range(cntOfEdges):
                    if current == X[i] or current == Y[i]:
                        other = X[i] if current == Y[i] else Y[i]
                        self.ways(road+[current], other, result, N, X, Y)

    def heights(self, X, Y, height):
        result = {}
        cntOfEdges = len(X)
        for i in range(cntOfEdges):
            result[(X[i], Y[i])] = height[i]
            result[(Y[i], X[i])] = height[i]
        return result

    def maxHeightForEachWay(self, w, hs, B):
        cntOfVertex = len(w)
        edges = [(w[i], w[i+1])for i in range(cntOfVertex-1)]
        sortedEdges = sorted(edges, key=lambda x: hs[x])
        result = hs[sortedEdges[0]]
        while True:
            result = result + 1
            cost = 0
            for edge in sortedEdges:
                if hs[edge] >= result:
                    break
                cost = cost + pow(result - hs[edge], 2)
            if cost > B:
                result = result - 1
                break
        return result

    def maxHeight(self, N, X, Y, height, B):
        result = 0
        ws = []
        self.ways([], 0, ws, N, X, Y)
        print 'debug[47]', ws
        hs = self.heights(X, Y, height)
        for w in ws:
            h = self.maxHeightForEachWay(w, hs, B)
            if h > result:
                result = h
        return result

def main():
    obj = TallShoes()
    print obj.maxHeight(3, (0, 1, 0), (1, 2, 2), (3, 4, 2), 1)
#    print obj.maxHeight(3, (0, 1, 0), (1, 2, 2), (3, 4, 2), 52)

if __name__ == '__main__':
    main()

