from sys import maxint

class TwoNumberGroupsEasy(object):
    def __init__(self):
        object.__init__(self)

    def distance(self, A, B):
        result = 0
        for i in A:
            result = result + abs(A[i] - B.get(i, 0))
        for j in B:
            if j not in A:
                result = result + B[j]
        return result

    def modulo(self, A, M):
        result = {}
        for i in A:
            result[i%M] = result.get(i%M, 0) + A[i]
        return result

    def multiSet(self, A, numA):
        result = {}
        cntOfNums = len(A)
        for i in range(cntOfNums):
            result[A[i]] = numA[i]
        return result
        
    def solve(self, A, numA, B, numB):
        minDistance = maxint

        A = self.multiSet(A, numA)
        B = self.multiSet(B, numB)
        print 'debug[34]', A, B

        cntOfLoop = max((max(A), max(B)))
        if cntOfLoop == 1:
            return 0

        for i in range(2, cntOfLoop+1):
            newA = self.modulo(A, i)
            newB = self.modulo(B, i)
            d = self.distance(newA, newB)
            print 'debug[41]', i, newA, newB, d
            if d < minDistance:
                minDistance = d
        return minDistance

def main():
    obj = TwoNumberGroupsEasy()
#    print obj.solve((1,2,3,4), (2,1,1,1), (5,6,7,8), (1,1,1,2))
#    print obj.solve((5,7), (1,1), (12,14), (1,1))
#    print obj.solve((100,), (2,), (1,), (1,))
#    print obj.solve((1,), (1,), (1,), (1,))
#    print obj.solve((5,), (1,), (6,), (1,))
#    print obj.solve((733815053,566264976,984867861,989991438,407773802,701974785,599158121,713333928,530987873,702824160), (8941,4607,1967,2401,495,7654,7078,4213,5485,1026), (878175560,125398919,556001255,570171347,643069772,787443662,166157535,480000834,754757229,101000799), (242,6538,7921,2658,1595,3049,655,6945,7350,6915))

if __name__ == '__main__':
    main()
        
        
