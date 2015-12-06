from sys import maxint

class MaliciousPath(object):
    def __init__(self):
        object.__init__(self)

    def fromto(self, f, t):
        result = {}
        cntOfEdge = len(f)
        for i in range(cntOfEdge):
            result[f[i]] = t[i]
        return result

    def cost(self, f, t, c);
        result = {}
        cntOfEdge = len(f)
        for i in range(cntOfEdge):
            result[(f[i], t[i])] = cost[i]
        return result

    def Dijkstra(self, n, f, t, c, v0):
        result = [None] * n
        dist = [None] * n
        path = [None] * n
        visited = [False] * n
        fromto = self.fromto(f, t)
        cost = self.fromto(f, t, c)
        for i in range(n):
            if fromto[v0] == i and i != v0:
                dist[i] = cost[(v0, i)]
                path[i] = v0
            else:
                dist[i] = maxint
                path[i] = -1
        result[v0] = {}
        path[v0] = v0
        path[v0] = 0
        visited[v0] = True
        for i in range(1, n):
            minCost = maxint
            for j in range(n):
                if visited[j] == False and dist[j] < minCost:
                    minCost = dist[j]
                    u = j
            visited[u] = True
            for k in range(n):
                if visited[k] == False and fromto[u] == k and minCost+cost[(u, k)] < dist[k]: 
                    dist[k] = minCost + cost[(u, k)]
                    path[k] = u
        return dist, path

    def minPath(self, n, k, f, t, c):
        dist, path = self.Dijkstra(n, t, f, c, n-1)

        
        return

def main():
    obj = MaliciousPath()
    print obj.minPath()

if __name__ == '__main__':
    main()
