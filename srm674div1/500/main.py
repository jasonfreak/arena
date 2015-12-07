from sys import maxint

class FindingKids(object):
    def __init__(self):
        object.__init__(self)

    def pseudo_random(self, n, q, A, B, C):
        pos = [None] * n
        dir = [None] * n
        kid = [None] * q
        time = [None] * q
        M = 1000000007
        for i in range(n):
            A = (A * B + C) % M
            p = A % (M - n + i + 1)
            if p in pos:
                p = M - n + i
            pos[i] = p
            if p % 2 == 0:
                dir[i] = 'right'
            else:
                dir[i] = 'left'

        for i in range(q):
            A = (A * B + C) % M
            kid[i] = A % n
            A = (A * B + C) % M
            time[i] = A
        return pos, dir, kid, time

    def getSum(self, n, q, A, B, C):
        pos, dir, kid, time = self.pseudo_random(n, q, A, B, C)
        print 'debug[31]', pos
        print 'debug[32]', dir
        print 'debug[33]', kid
        print 'debug[34]', time
        cur = 0
        end = max(time)
        sortedIndex = sorted(range(q), key=lambda x: time[x])
        index = 0
        ans = [None] * q
        while cur <= end:
            minDistance = maxint 
            for i in range(n-1): 
                if dir[i] == 'right' and dir[i+1] == 'left':
                    distance = pos[i+1] - pos[i]
                    if distance < minDistance:
                        minDistance = distance
            nxt = cur + minDistance
            print 'debug[41]', cur, nxt
            raw_input()
            while time[sortedIndex[index]] <= nxt:
                distance = time[sortedIndex[index]] - cur
                ans[sortedIndex[index]] = pos[kid[sortedIndex[index]]] + (distance if dir[kid[sortedIndex[index]]] == 'right' else -distance)
                index += 1
            for i in range(n-1): 
                pos[i] += (minDistance if dir[i] == 'right' else -minDistance)
                if dir[i] == 'right' and dir[i+1] == 'left':
                    distance = pos[i+1] - pos[i]
                    if distance == minDistance:
                        dir[i] = 'left'
                        dir[i+1] = 'right'
            pos[n-1] += (minDistance if dir[n-1] == 'right' else -minDistance)
            cur = nxt
                    
        return ans

def main():
    obj = FindingKids()
    print obj.getSum(5, 2, 0, 1, 1)

if __name__ == '__main__':
    main()
