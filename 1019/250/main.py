from itertools import combinations

class OkonomiyakiShop(object):
    def __init__(self):
        object.__init__(self)

    def count(self, osize, K):
        result = 0
        cs = combinations(osize, 2)
        for c in cs:
            if abs(c[0]-c[1]) <= K:
                result = result + 1
        return result
