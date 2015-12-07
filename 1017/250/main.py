class TheKingsArmyDiv2(object):
    def __init__(self):
        object.__init__(self)

    def getNumber(self, state):
        cntOfRow = len(state)
        cntOfColumn  = len(state[0])
        isHappyExist = False
        for i in range(cntOfRow-1):
            for j in range(cntOfColumn-1):
                if state[i][j] == 'H':
                    isHappyExist = True
                    if state[i+1][j] == 'H' or state[i][j+1] == 'H':
                        return 0
                elif state[i+1][j] == 'H' or state[i][j+1] == 'H':
                    isHappyExist = True
        if state[cntOfRow-1][cntOfColumn-1] == 'H':
            isHappyExist = True
        if isHappyExist:
            return 1
        else:
            return 2

def main():
    obj = TheKingsArmyDiv2()
    print obj.getNumber(('SH', 'SS'))

if __name__ == '__main__':
    main()
