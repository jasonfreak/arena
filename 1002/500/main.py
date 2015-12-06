from sys import float_info
from math import pow

class ClosestRabbit(object):
    def __init__(self):
        object.__init__(self)

    def getEmptyCell(self, board):
        emptyCells = []

        cntRow = len(board)
        cntCol = len(board[0])

        for i in range(cntRow):
            for j in range(cntCol):
                if board[i][j] == '.':
                    emptyCells.append((i, j))
        return emptyCells

    def getCntOfCC(self, cells):
#        print 'debug[22]', cells
        closetCells = {}
        for cell_1 in cells:
            closetDistance = float_info.max
            for cell_2 in cells:
                if cell_1 is not cell_2:
                    distance = pow(cell_1[0]-cell_2[0], 2) + pow(cell_1[1]-cell_2[1], 2)
                    if distance < closetDistance:
                        closetCells[cell_1] = cell_2
                        closetDistance = distance
                    elif distance == closetDistance:
                        if cell_2[0] < closetCells[cell_1][0]:
                            closetCells[cell_1] = cell_2
                        elif cell_2[0] == closetCells[cell_1][0]:
                            if cell_2[1] < closetCells[cell_1][1]:
                                closetCells[cell_1] = cell_2

#        print 'debug[38]', closetCells
        cntOfCC = 0
        for cell in cells:
            if closetCells[cell] and cell is closetCells[closetCells[cell]]:
                closetCells[closetCells[cell]] = None
                cntOfCC = cntOfCC + 1
            closetCells[cell] = None

        return cntOfCC

    def getWholeFromEmptyCellByRecursion(self, whole, cells, emptyCells, r):
        if r == 0:
            whole.append(self.getCntOfCC(cells))
            print 'debug[52]', cells
        else:
            cntEmptyCells = len(emptyCells)

            for i in range(cntEmptyCells):
                cell = emptyCells[i]
                if cntEmptyCells - i >= r:
                    self.getWholeFromEmptyCellByRecursion(whole, cells+[cell], emptyCells[i+1:], r-1)

    def getWholeFromEmptyCellByIteration(self, whole, emptyCells, r):
        cntEmptyCells = len(emptyCells)
#        print 'debug[62]', cntEmptyCells
        poss = [i-1 for i in range(r)]
        cur = 0
        while cur >= 0:
            poss[cur] = poss[cur] + 1 
#            print 'debug[65]', cur, poss
#            raw_input()
            if poss[cur] == cntEmptyCells:
                for i in range(cur, r):
                    poss[i] = poss[i-1] + 1
                cur = cur - 1
            else:
                if cur == r-1:
                    cells = [emptyCells[poss[i]] for i in range(r)]
#                    print 'debug[73]', cells
                    whole.append(self.getCntOfCC(cells))
                else:
                    cur = cur + 1
        
    def getExpected(self, board, r):
        emptyCells = self.getEmptyCell(board)

        whole = []

#        self.getWholeFromEmptyCellByRecursion(whole, [], emptyCells, r)
        self.getWholeFromEmptyCellByIteration(whole, emptyCells, r)
        print 'debug[67]', sum(whole), len(whole), whole

        return float(sum(whole))/len(whole)

def main():
    obj = ClosestRabbit()
#    print obj.getExpected(('.#.#.'), 2)
#    print obj.getExpected(('..###.', '.###.#'), 4)
#    print obj.getExpected(('.....', '#....'), 4)
    print obj.getExpected(('.#####.#####..#....#', '#......#....#.##..##', '.####..#####..#.##.#', '.....#.#...#..#....#', '#####..#....#.#....#'), 19)

if '__main__' == __name__:
    main()


