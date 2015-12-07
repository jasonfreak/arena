class BichromePainting(object):
    def __init__(self):
        object.__init__(self)

    def getState(self, cntOfRow, cntOfCol):
        ret = list()
        for i in range(cntOfCol):
            row = list()
            for j in range(cntOfRow):
                row.append('W')
            ret.append(row)
        return ret

    def modify(self, state, i, j, k):
        cntOfRow = len(state)
        cntOfCol = len(state[0])
        if i + k > cntOfRow or j + k > cntOfCol:
            return False
        color = 'W' if state[i][j] == 'B' else 'B'
        for pi in range(i, i+k):
            for pj in range(j, j+k):
                state[pi][pj] = color
        return True

    def strState(self, state):
        ret = ''
        cntOfRow = len(state)
        cntOfCol = len(state[0])
        for i in range(cntOfRow):
            text = ''
            for j in range(cntOfCol):
                text += state[i][j]
            ret += text + '\n'
        return ret

    def isThatPossible(self, board, k):
        cntOfRow = len(board)
        cntOfCol = len(board[0])
        state = self.getState(cntOfRow, cntOfCol)
        for i in range(cntOfRow):
            for j in range(cntOfCol):
                if state[i][j] != board[i][j]:
                    print 'debug[33]', i, j
                    print self.strState(state)
                    if not self.modify(state, i, j, k):
                        return 'Impossible'
        return 'Possible'

def main():
    obj = BichromePainting()
#    print obj.isThatPossible(("BBBW", "BWWW", "BWWW", "WWWW"), 3)
    print obj.isThatPossible(("BWBWBB", "WBWBBB", "BWBWBB", "WBWBBB", "BBBBBB", "BBBBBB"), 2)
if __name__ == '__main__':
    main()
