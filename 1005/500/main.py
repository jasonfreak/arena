class PathGameDiv2(object):
    def __init__(self):
        object.__init__(self)

    def initCells(self, board):
#freeCells:
#{cell:[], ...}
        freeCells = {}
        cntOfOneRowCells = len(board[0])
        for i in range(2):
            for j in range(cntOfOneRowCells):
                otherSide = (i + 1) % 2
                if board[i][j] == '#':
                    if j != 0:
                        board[otherSide] = board[otherSide][:j-1]+'b'+board[otherSide][j:]
                    board[otherSide] = board[otherSide][:j]+'b'+board[otherSide][j+1:]
                    if j != cntOfOneRowCells - 1:
                        board[otherSide] = board[otherSide][:j+1]+'b'+board[otherSide][j+2:]

        for i in range(2):
            for j in range(cntOfOneRowCells):
                key = i * cntOfOneRowCells + j
                relations = freeCells.get(key, [])
                otherSide = (i + 1) % 2
                if board[i][j] == '.':
                    if j != 0 and board[otherSide][j-1] == '.':
                        leftKey = otherSide * cntOfOneRowCells + (j-1)
                        relations.append(leftKey)
                    if board[otherSide][j] == '.':
                        middleKey = otherSide * cntOfOneRowCells + j
                        relations.append(middleKey)
                    if j != cntOfOneRowCells - 1 and board[otherSide][j+1] == '.':
                        rightKey = otherSide * cntOfOneRowCells + (j+1)
                        relations.append(rightKey)
                    freeCells[key] = relations

        return freeCells

    def calc(self, board):
        result = 0

        cells = self.initCells(list(board))
#        print 'debug[43]', cells
        while len(cells) > 0:
            print 'debug[45]', cells
            raw_input()
            key = min(cells.keys(), key=lambda x:len(cells[x]))
            for cell in cells[key]:
                print 'debug[47]', key, cell, cells[cell]
                cells[cell] = filter(lambda x:x != key, cells[cell])
            del cells[key]
            result = result + 1

        return max((result - 1, 0))

def main():
    obj = PathGameDiv2()
#    print obj.calc(('#....', '...#.'))
#    print obj.calc(('#', '.'))
#    print obj.calc(('.', '.'))
    print obj.calc(('....#.##.....#...........', '..#......#.......#..#....'))

if __name__ == '__main__':
    main()
