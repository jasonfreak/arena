from copy import deepcopy

class CheeseRolling(object):
    def __init__(self):
        object.__init__(self)

    def getWaysToWinByRecursion(self, who, players, wins):
#        print 'debug[6]', who, players
        result = 0
        for opponent in filter(lambda x:wins[who][x] == 'Y', range(len(wins))):
            if opponent in players: 
                frees = filter(lambda x:x is not who and x is not opponent, players)
#                print 'debug[12]', who, opponent, frees
                cntOfFrees = len(frees)
                if cntOfFrees == 0:
                    result =  2
                    break

                cur = 0
                poss = range(-1, cntOfFrees/2-1)
                while cur >=0:
                    poss[cur] = poss[cur] + 1
#                    print 'debug[20]', who, opponent, cur, poss
                    if poss[cur] == cntOfFrees:
                        for i in range(cur, cntOfFrees/2):
                            poss[i] = poss[i-1] + 1
                        cur = cur - 1
                    else:
                        if cur == cntOfFrees/2 - 1:
                            new = deepcopy(frees)
                            remains = []
#                            print 'debug[32]', new, poss
                            for i in range(cntOfFrees/2):
                                remains.append(new[poss[i]])
                                new[poss[i]] = -1
                            new = filter(lambda x:x >= 0, new)
#                            print 'debug[30]', new
#                            print 'debug[31]', remains
                            result = result + 2 * (self.getWaysToWinByRecursion(who, new+[who], wins) * self.getWaysToWinByRecursion(opponent, remains+[opponent], wins))
                        else:
                            cur = cur + 1
#        print 'debug[39]---------', who, result, players
        return result
            
    def waysToWin(self, wins):
        result = []

        cntOfPlayers = len(wins)
        for i in range(cntOfPlayers):
            result.append(self.getWaysToWinByRecursion(i, range(cntOfPlayers), wins))

        return result

def main():
    obj = CheeseRolling()
#    print obj.waysToWin(('NN', 'YN'))
#    print obj.waysToWin(('NYNY', 'NNYN', 'YNNY', 'NYNN'))
    print obj.waysToWin(('NYNYNYNY', 'NNYNYNYY', 'YNNNNNNN', 'NYYNNYNY', 'YNYYNYYY', 'NYYNNNNN', 'YNYYNYNN', 'NNYNNYYN'))
#    print obj.waysToWin(('NYNNNNYYNYYNNYNN', 'NNNNNNNNNYYNYYNY', 'YYNYYNNNNYYYYYYN', 'YYNNYYYNYNNYYYNY', 'YYNNNYYNYYNNNNYY', 'YYYNNNNYYNNYYNYN', 'NYYNNYNYNYNYYYYN', 'NYYYYNNNYYNYNYYY', 'YYYNNNYNNYYYYNNN', 'NNNYNYNNNNNNYYNY', 'NNNYYYYYNYNYYYNN', 'YYNNYNNNNYNNYNNY', 'YNNNYNNYNNNNNYNN', 'NNNNYYNNYNNYNNYY', 'YYNYNNNNYYYYYNNN', 'YNYNNYYNYNYNYNYN'))












if __name__ == '__main__':
    main()
