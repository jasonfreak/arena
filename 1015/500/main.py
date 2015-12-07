class LightSwitchingPuzzle(object):
    def __init__(self):
        object.__init__(self)

    def minFlips(self, state):
        result = 0
        state = list(state)
        cntOfLight = len(state)
        for i in range(cntOfLight):
            if state[i] == 'Y':
                for j in range(i, cntOfLight, i+1):
                    state[j] = 'N' if state[j] == 'Y' else 'Y'
                result = result + 1
        for i in range(cntOfLight):
            if state[i] == 'Y':
                return -1
        return result

def main():
    obj = LightSwitchingPuzzle()
#    print obj.minFlips('YYYYY')
    print obj.minFlips('YNYNYNYNY')

if __name__ == '__main__':
    main()
            
