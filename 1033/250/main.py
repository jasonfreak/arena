class RobotOnMoonEasy(object):
    def __init__(self):
        object.__init__(self)

    def isSafeCommand(self, board, S):
        cntOfRow = len(board)
        cntOfCol = len(board[0])
        for i in range(cntOfRow):
            for j in range(cntOfCol):
                if board[i][j] == 'S':
                    x = i
                    y = j
                    for s in S:
                        last = (x, y)
                        if s == 'U':
                            x -= 1
                        elif s == 'D':
                            x += 1
                        elif s == 'L':
                            y -= 1
                        elif s == 'R':
                            y += 1
                        if x < 0 or y < 0 or x == cntOfRow or y == cntOfCol:
                            return 'Dead'
                        if board[x][y] == '#':
                            x = last[0]
                            y = last[1]
                        
                    return 'Alive'

def main():
    obj = RobotOnMoonEasy()
    print obj.isSafeCommand()

if __name__ == '__main__':
    main()
