from sys import float_info

class GreaterGame(object):
    def __init__(self):
        object.__init__(self)

    def optimalScore(self, shew1, shew2):
        result = 0
        min_1 = 0
        max_1 = len(shew1) - 1
        max_2 = len(shew2) - 1
        while min_1 <= max_1:
            if shew1[max_1] >= shew2[max_2]:
                result = result + 1 if shew1[max_1] > shew2[max_2] else 0
                max_1 = max_1 - 1
                max_2 = max_2 - 1
            else:
                min_1 = min_1 + 1
                max_2 = max_2 - 1
        return result

    def getExpectedScoreByRecursion(self, results, done, todo, unShew1, unShew2):
        cntUnShew = len(unShew1)
#        print 'debug[23]', done, todo
        cntOfTodo = len(todo)
        if cntOfTodo == 0:
#            print 'debug[26]', sum([1 if unShew1[done[i]] > unShew2[i] else 0 for i in range(cntUnShew)]), unShew1, unShew2
            results.append(sum([1 if unShew1[done[i]] > unShew2[i] else 0 for i in range(cntUnShew)]))

        else:
            for i in range(cntOfTodo):
                self.getExpectedScoreByRecursion(results, done+[todo[i]], todo[:i]+todo[i+1:], unShew1, unShew2)

    def expectedScore(self, unShew1, unShew2):
        cntOfUnShew = len(unShew1)
        results = []
        self.getExpectedScoreByRecursion(results, [], range(cntOfUnShew), unShew1, unShew2)

        return float(sum(results)) / reduce(lambda x, y: x * y, range(1, cntOfUnShew+1))

    def calc(self, hand, sothe):
        result = float_info.min

        shew = sorted(filter(lambda x:x > 0, sothe))
        cntOfShew = len(shew) 
        cntOfHand = len(hand)

        allCards = range(1, 2*cntOfHand+1)
        for card in hand:
            allCards[card-1] = 0
        for card in shew:
            allCards[card-1] = 0

        unShew = filter(lambda x:x > 0, allCards)
        cntUnShew = len(unShew)
            

        poss = range(-1, cntOfShew-1)
        cur = 0

        if cntOfShew > 0:
            while cur >= 0:
#                print 'debug[63]', cur, poss
                poss[cur] = poss[cur] + 1
                if poss[cur] == cntOfHand:
                    for i in range(cur, cntOfShew):
                        poss[i] = poss[i-1] + 1
                    cur = cur - 1
                else:
                    if cur == cntOfShew - 1:
                        againstShew = sorted([hand[poss[i]] for i in range(cntOfShew)])
                        result_1 = self.optimalScore(againstShew, shew)
                        print 'debug[72]', result_1, againstShew, shew

                        againstUnShew = filter(lambda x: x not in againstShew, hand)
                        result_2 = self.expectedScore(againstUnShew, unShew) if cntUnShew > 0 else 0

                        if result < result_1 + result_2:
                            result = result_1 + result_2

                    else:
                        cur = cur + 1
        else:
            result = self.expectedScore(hand, unShew) 

        return result

def main():
    obj = GreaterGame()
    print obj.calc((4, 2), (1, 3))
    print obj.calc((2,), (-1,))
    print obj.calc((1,3,5,7), (8,-1,4,-1))

if __name__ == '__main__':
    main()
