from sys import maxint
from functools import wraps

def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper

class TheKingsArmyDiv1(object):
    def __init__(self):
        object.__init__(self)

    def isValid(self, index, state):
        cntOfRow = len(state)
        cntOfColumn = len(state[0])
        return True if 0 <= index[0] and index[0] < cntOfRow and 0 <= index[1] and index[1] < cntOfColumn else False

    def getCntOfHappy(self, state):
        result = 0
        cntOfRow = len(state)
        cntOfColumn = len(state[0])
        for i in range(cntOfRow):
            for j in range(cntOfColumn):
                result = result + (1 if state[i][j] == 'H' else 0)
        return result

    def getNeighbors(self, index, state):
        return filter(lambda x: self.isValid(x, state), ((index[0]-1, index[1]), (index[0]+1, index[1]), (index[0], index[1]-1), (index[0], index[1]+1)))

    def getWays(self, state):
        result = ()
        cntOfRow = len(state)
        cntOfColumn = len(state[0])
        for i in range(cntOfRow):
            for j in range(cntOfColumn):
                index = (i, j)
                for neighbor in self.getNeighbors(index, state):
                    if state[index[0]][index[1]] == 'H' and state[neighbor[0]][neighbor[1]] == 'S':
                        result = result + ((0, (index, neighbor)), )

        isRowAllHappy = [True] * cntOfRow
        for i in range(cntOfRow):
            for j in range(cntOfColumn):
                if state[i][j] == 'S':
                    isRowAllHappy[i] = False
                    break
        if isRowAllHappy[0] and not isRowAllHappy[1]:
            result = result + ((1, (0, 1)), )
        elif not isRowAllHappy[0] and isRowAllHappy[1]:
            result = result + ((1, (1, 0)), )

        isColAllHappy = [True] * cntOfColumn
        for j in range(cntOfColumn):
            for i in range(cntOfRow):
                if state[i][j] == 'S':
                    isColAllHappy[j] = False
                    break

        for j in range(cntOfColumn-1):
            if isColAllHappy[j] and not isColAllHappy[j+1]:
                result = result + ((2, (j, j+1)), )

        for j in range(cntOfColumn-1, 0, -1):
            if isColAllHappy[j] and not isColAllHappy[j-1]:
                result = result + ((2, (j, j-1)), )

        return result

    @memo
    def getNumber(self, state):
        cntOfRow = len(state)
        cntOfColumn = len(state[0])
        result = maxint
        cntOfHappy = self.getCntOfHappy(state)
        if cntOfHappy == 0:
            return -1
        elif cntOfHappy == cntOfRow * cntOfColumn:
            return 0
        ways = self.getWays(state)
        print 'debug[80]', state, ways
        raw_input()
        for way in ways:
            if way[0] == 0:
                index = way[1][0]
                neighbor = way[1][1]
                row = state[neighbor[0]][:neighbor[1]] + state[index[0]][index[1]] + state[neighbor[0]][neighbor[1]+1:]
                new = state[:neighbor[0]] + (row, ) + state[neighbor[0]+1:]
            elif way[0] == 1:
                one = way[1][0]
                other = way[1][1]
                row = ''
                for j in range(cntOfColumn):
                    row = row + state[one][j]
                new = state[:other] + (row, ) + state[other+1:]
            elif way[0] == 2:
                one = way[1][0]
                other = way[1][1]
                new = state
                for i in range(cntOfRow):
                    row = state[i][:other] + state[i][one] + state[i][other+1:]
                    new = new[:i] + (row, ) + new[i+1:]

            number = 1 + self.getNumber(new)
            if number < result:
                result = number

        return result

def main():
    obj = TheKingsArmyDiv1()
#    print obj.getNumber(('HSH', 'SHS'))
#    print obj.getNumber(('HHHHH', 'HSHSH'))
#    print obj.getNumber(('HSHHSHSHSHHHSHSHSH', 'SSSSHSSHSHSHHSSSSH'))
#    print obj.getNumber(('HS', 'HS'))
    print obj.getNumber(('HHSHSH', 'SHHHHS'))

if __name__ == '__main__':
    main()

