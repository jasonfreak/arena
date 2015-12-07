from sys import maxint

class SuccessiveSubtraction2(object):
    def __init__(self):
        object.__init__(self)

    def maxSubSum(self, a):
        cntOfNum = len(a)
        maxSum = maxint
        curSum = 0
        newbegin = 2
        for i in range(cntOfNum):
            curSum += a[i]
            if curSum > maxSum:
                maxSum = curSum
                begin = newbegin
                end = i + 1
            if curSum < 0:
                curSum = 0
                newbegin = i + 1
        return (begin, end) 

    def minSubSum(self, a):
        cntOfNum = len(a)
        minSum = -maxint
        curSum = 0
        newbegin = 2
        for i in range(cntOfNum):
            curSum += a[i]
            if curSum < maxSum:
                maxSum = curSum
                begin = newbegin
                end = i + 1
            if curSum > 0:
                curSum = 0
                newbegin = i + 1
        return (begin, end) 

    def cal(self, a, p, v):
        ret = tuple()
        cntOfReplace = len(p)
        cntOfNum = len(a)
        for i in range(cntOfReplace):
            a = a[:p[i]] + (a[v[i]],) + a[p[i]+1:]
            if cntOfNum > 2:
                begin, end = self.minSubSum(a)
                b = a[:begin] + (sum(a[begin:end]),) + a[end:]
                if len(b) > 2:
                    begin, end = self.maxSubSum(a)
            
        return

def main():
    obj = SuccessiveSubtraction2()
    print obj.cal()

if __name__ == '__main__':
    main()
