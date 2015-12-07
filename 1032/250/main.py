from functools import wraps
from itertools import combinations
from copy import deepcopy

def memo(func):
    cache = {}
    miss = object()
    
    @wraps(func)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = func(*args)
            cache[args] = result
        return result
    return wrapper
    
class RobotOnMoon(object):
    def __init__(self):
        object.__init__(self)

    def getBegin(self, board):
        cntOfRow = len(board)
        cntOfCol = len(board)
        for i in range(cntOfRow):
            for j in range(cntOfCol):
                if board[i][j] == 'S': return (i, j)

    def search(self, pos, board):
        cntOfRow = len(board)
        cntOfCol = len(board[0])
        x = pos[0]
        y = pos[1]
        if x * y == 0 or x == cntOfRow-1 or y == cntOfCol-1:
            return False
        s = board[x]
        s = s[:y] + '#' + s[y+1:]
        board = board[:x] + (s,) + board[x+1:]
        u = True if board[x-1][y] == '#' else self.search((x-1, y), board)
        d = True if board[x+1][y] == '#' else self.search((x+1, y), board)
        l = True if board[x][y-1] == '#' else self.search((x, y-1), board)
        r = True if board[x][y+1] == '#' else self.search((x, y+1), board)
        return (u and d and l and r)

    def isArbitaryLongPerfect(self, board):
        begin = self.getBegin(board)
        return self.search(begin, board)

    def walk(self, pos, sequence, board):
#        print 'debug[50]', pos, sequence
        cntOfRow = len(board)
        cntOfCol = len(board[0])
        x = pos[0]
        y = pos[1]
        for action in sequence:
            new_x = x
            new_y = y
            if action == 'u':
                new_x -= 1
            elif action == 'd':
                new_x += 1
            elif action == 'l':
                new_y -= 1
            elif action == 'r':
                new_y += 1
            if new_x == -1 or new_y == -1 or new_x == cntOfRow or new_y == cntOfCol:
#                print 'debug[68]', new_x, new_y, cntOfRow, cntOfCol
                return False
            if board[new_x][new_y] != '#':
                x = new_x
                y = new_y
#        print 'debug[71]', pos, sequence
        return True

#    @memo
    def isPerfect(self, pos, sequence, board):
#        print 'debug[76]', pos, sequence
#        raw_input()
        cntOfAction = len(sequence)
        if not self.walk(pos, sequence, board):
            return False
        for i in range(1, cntOfAction):
            cbs = combinations(range(cntOfAction), i)
            for cb in cbs:
                if not self.isPerfect(pos, tuple([sequence[j] for j in cb]), board):
                    return False
#        print 'debug[85]', pos, sequence
        return True

    @memo
    def stepByRecursion(self, pos, sequence, board):
#        print 'debug[83]', pos, sequence
#        raw_input()
        if not self.isPerfect(pos, sequence, board):
            return -1
        else:
            result = 0
            actions = ('u', 'd', 'l', 'r')
            for i in range(len(actions)):
                temp = 1 + self.stepByRecursion(pos, sequence + actions[i:i+1], board)
                if temp > result:
                    result = temp
        return result

    def longestSafeCommand(self, board):
        if self.isArbitaryLongPerfect(deepcopy(board)):
            return -1
        begin = self.getBegin(board)
        return self.stepByRecursion(begin, (), board)

def main():
    obj = RobotOnMoon()
#    print obj.longestSafeCommand(("#####", "#...#", "#.S.#", "#...#", "#####"))
    print obj.longestSafeCommand(("S......",))

if __name__ == '__main__':
    main()
