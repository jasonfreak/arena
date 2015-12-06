class ShadowSculpture(object):
    def __init__(self):
        object.__init__(self)

    def isConnected(self, i, j, XY):
        cntOfPoints = len(XY)
        neighbors = ((i, j-1), (i, j+1), (i-1, j), (i+1, j))
        result = False
        for neighbor in neighbors:
#            print 'debug[10]', neighbor[0], neighbor[1]
            if not (0 <= neighbor[0] and neighbor[0] < cntOfPoints):
                continue
            if not (0 <= neighbor[1] and neighbor[1] < cntOfPoints):
                continue
            if XY[neighbor[0]][neighbor[1]] == 'Y':
                return True
        return result

    def isFourConnected(self, XY):
        cntOfPoints = len(XY)
        result = True
        cntOfY = 0
        for i in range(cntOfPoints):
            for j in range(cntOfPoints):
                if XY[i][j] == 'Y':
                    cntOfY = cntOfY + 1
                    if not self.isConnected(i, j, XY):
                        result = False
        if cntOfY == 1:
            result = True
        return result

    def ways(self, i, j, XY, YZ, ZX):
        result = []
        cntOfPoints = len(XY)
        for k in range(cntOfPoints):
            print 'debug[37]', i, j, k, XY[i][j], YZ[j][k], ZX[k][i]
            if YZ[j][k] == XY[i][j] and ZX[k][i] == YZ[j][k]:
                result.append(k)
        return result

    def isOccupied(self, XY):
        cntOfPoints = len(XY)
        for i in range(cntOfPoints):
            for j in range(cntOfPoints):
                if XY[i][j] != 'O':
                    return False
        return True

    def possible(self, XY, YZ, ZX):
        XY = [list(xy) for xy in XY]
        YZ = [list(yz) for yz in YZ]
        ZX = [list(zx) for zx in ZX]

        if not self.isFourConnected(XY):
#            print 'debug[55]'
            return 'Impossible'
        if not self.isFourConnected(YZ):
#            print 'debug[58]'
            return 'Impossible'
        if not self.isFourConnected(ZX):
#            print 'debug[61]'
            return 'Impossible'

        cntOfPoints = len(XY)
        waysOfEachXY = {}
        for i in range(cntOfPoints):
            for j in range(cntOfPoints):
                waysOfEachXY[(i, j)] = self.ways(i, j, XY, YZ, ZX)
        order = sorted(waysOfEachXY.keys(), key=lambda x:len(waysOfEachXY[x]))

        for xy in order:               
            print 'debug[72]', XY
            print 'debug[73]', YZ
            print 'debug[74]', ZX
            print '---------'
            XY[xy[0]][xy[1]] = 'O'
            isNotAllOccupied = False
            for k in waysOfEachXY[xy]:
                if YZ[xy[1]][k] != 'O' and ZX[k][xy[0]] != 'O':
                    YZ[xy[1]][k] = 'O'
                    ZX[k][xy[0]] = 'O'
                    isNotAllOccupied = True 
                    break
            if not isNotAllOccupied:
                print 'debug[80]', XY
                print 'debug[81]', YZ
                print 'debug[82]', ZX
                return 'Impossible'

        if not self.isOccupied(XY):
#            print 'debug[83]'
            return 'Impossible'
        if not self.isOccupied(YZ):
#            print 'debug[86]'
            return 'Impossible'
        if not self.isOccupied(ZX):
#            print 'debug[89]', ZX
            return 'Impossible'

        return 'Possible'

def main():
    obj = ShadowSculpture()
#    print obj.possible(('YN','NN'), ('YN','NN'), ('YN','NN'))
#    print obj.possible(('YN','NY'), ('YN','NY'), ('YN','NY'))
#    print obj.possible(('YYY','YNY','YYY'), ('YYY','YNY','YYY'), ('YYY','YNY','YYY'))
#    print obj.possible(('YYY','YNY','YYY'), ('NYY','YNY','YYY'), ('YYY','YNY','YYN'))
#    print obj.possible(('N',), ('N',), ('N',))
    print obj.possible(('YYYYY', 'YYNYY', 'YYYYY', 'YYNYY', 'YYYYY'), ('YYYYY', 'YYNYY', 'YYYYY', 'YYNYY', 'YYYYY'), ('YYYYY', 'YYNYY', 'YYYYY', 'YYNYY', 'YYYYY'))


if __name__ == '__main__':
    main()



