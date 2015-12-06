from sys import maxint

class ArmyTeleportation(object):
    def __init__(self):
        object.__init__(self)

    def check(self, x, y, A, B, C, D):
#        print 'debug[8]', A, C, x, B, D, y
        if B != 0:
            fA = A * B
            fC = C * B
            fx = x * B
            fB = B * A - fA
            fD = D * A - fC
            fy = y * A - fx
        else:
            fA = A
            fC = C
            fx = x
            fB = B
            fD = D
            fy = y
#        print 'debug[14]', fA, fC, fx, fB, fD, fy

        if fD == 0:
            if fy != 0:
                return False
            else:
                if fA == 0:
                    if fB == 0:
                        if fx == 0:
                            return True
                        else:
                            return False
                    else:
                        if fx % fB == 0:
                            return True
                        else:
                            return False
                else:
                    k = -10000000
                    while k <= 10000000:
                        if (fx - fC * k) % fA == 0:
                            return True
                        k = k + 1
                    return False
        else:
            if fy % fD != 0:
                return False
            else:
                j = fy / fD

        remain = fx - j * (fC)
        if fA != 0 and remain % fA != 0:
            return False
            
        return True

    def ifPossible(self, x1, y1, x2, y2, xt, yt):
        result = 'impossible'
        cntOfSoldier = len(x1)
        xt = map(lambda x: x * 2, xt)
        yt = map(lambda x: x * 2, yt)
        A = xt[1] - xt[0]
        B = yt[1] - yt[0]
        C = xt[2] - xt[0]
        D = yt[2] - yt[0]

        for i in range(cntOfSoldier):
            sumx = x1[0] + x2[i]
            sumy = y1[0] + y2[i]
            same = {}
            for j in range(cntOfSoldier):
                same[(sumx-x1[j], sumy-y1[j])] = True
            sumsame = True
            for j in range(cntOfSoldier):
                if len(filter(lambda x: x[0] == x2[j] and x[1] == y2[j], same.keys())) == 0:
                    sumsame = False
            if sumsame:
#                print 'debug[55]', i, sumx, sumy, xt[0], yt[0]
                if self.check(sumx-xt[0], sumy-yt[0], A, B, C, D):
                    result = 'possible'

            diffx = x2[i] - x1[0]
            diffy = y2[i] - y1[0]
            diff = {}
            for j in range(cntOfSoldier):
                diff[(diffx+x1[j], diffy+y1[j])] = True
            diffsame = True
            for j in range(cntOfSoldier):
                if len(filter(lambda x: x[0] == x2[j] and x[1] == y2[j], diff.keys())) == 0:
                    diffsame = False
            if diffsame:
                if self.check(diffx, diffy, A, B, C, D):
                    result = 'possible'

        return result

def main():
    obj = ArmyTeleportation()
#    print obj.ifPossible((0, 1), (0, 1), (2, 1), (4, 3), (2, 3, 2), (0, 1, 3))
#    print obj.ifPossible((0, 1), (1, 2), (1, 2), (2, 3), (0, 0, 0), (5, 3, 8))
#    print obj.ifPossible((-816, 188, -293, 627), (162, 802, 732, -348), (-3292, -4296, -3815, -4735), (-546, -1186, -1116, -36), (629, -825, 674), (-493, -470, -442))
#    print obj.ifPossible((3, 2, 1), (1, 2, 3), (4, 5, 6), (6, 5, 4), (-2, 5, 6), (1, -3, 2))
#    print obj.ifPossible((6, -5, 1), (3, -10, -7), (0, 11, 5), (-5, 8, 5), (0, -5, 4), (-8, -9, -4))
#    print obj.ifPossible((1,), (3,), (3,), (7,), (0, 2, 5), (0, 4, 10))
    print obj.ifPossible((0,), (0,), (3,), (0,), (0, 1, 2), (0, 0, 0))

if __name__ == '__main__':
    main()
            

