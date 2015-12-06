class maxHeap(list):
    def __init__(self):
        list.__init__(self)
        self.heapSize = 0

    def maxHeapify(self, i):
        l = i * 2
        r = i * 2 + 1
        if l <= self.heapSize and self[l] > self[i]:
            largest = l
        else:
            largest = i
        if r <= self.heapSize and self[r] > self[largest]:
            largest = r
        if largest != i:
            tmp = self[i]
            self[i] = self[largest]
            self[largest] = tmp
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        self.heapSize = len(self) - 1
        for i in range(self.heapSize/2, 0, -1):
            self.maxHeapify(i)
            
    def heapMaximum(self):
        return self[1]

    def heapExtractMax(self):
        if self.heapSize < 1:
            raise Exception('heap underflow')
        maximum = self[1]
        self[1] = self[self.heapSize]
        self.heapSize = self.heapSize - 1
        self.maxHeapify(1)
        return maximum

    def heapIncreaseKey(self, i, key):
        if key < self[i]:
            raise Exception('new key is smaller than current key')
        self[i] = key
        while i > 1 and self[i/2] < self[i]:
            tmp = self[i/2]
            self[i/2] = self[i]
            self[i] = tmp
            i = i / 2

    def maxHeapInsert(self, node):
        self.heapSize = self.heapSize + 1
        self.append(-1)
        self[self.heapSize] = -1
        self.heapIncreaseKey(self.heapSize, node)

class SubdividedSlimes(object):
    def __init__(self):
        object.__init__(self)

    def needCut(self, S, M):
        result = 1
        score = 0
        mhp = maxHeap()
        mhp.append(None)
        mhp.append(S)
        mhp.buildMaxHeap()
        while mhp.heapSize > 0:
            s = mhp.heapExtractMax()
            x = s / 2
            y = s - x
            if x > 0 and y > 0:
                score += x * y
                if score >= M:
                    return result
                mhp.maxHeapInsert(x)
                mhp.maxHeapInsert(y)
            result += 1

        if score < M:
            return -1
        return result

def main():
    obj = SubdividedSlimes()
    print obj.needCut(765, 271828)

if __name__ == '__main__':
    main()
