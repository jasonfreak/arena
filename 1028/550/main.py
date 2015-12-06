class XorSequence(object):
    def __init__(self):
        object.__init__(self)

    def getA(self, N, sz, A0, A1, P, Q, R):
        A = [A0, A1]
        for i in range(2, sz):
            A.append((A[i-2] * P + A[i-1] * Q + R) % N)
        return A

    def getC(self, A, B):
        C = []
        for number in A:
            C.append(number ^ B)
        return C

    def getSortNumber(self, C):
        result = 0
        cntOfNumber = len(C)
        for i in range(cntOfNumber-1):
            for j in range(i, cntOfNumber):
                if C[i] < C[j]:
                    result += 1
        return result

    def getmax(self, N, sz, A0, A1, P, Q, R):
        result = 0
        A = self.getA(N, sz, A0, A1, P, Q, R)

        for B in range(N):
            C = self.getC(A, B)
            temp = self.getSortNumber(C)
            if temp > result:
                result = temp
            
        return result

def main():
    obj = XorSequence()
    print obj.getmax(4, 6, 3, 2, 0, 1, 2)

if __name__ == '__main__':
    main()
