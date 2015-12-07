from itertools import combinations
class Decipherability(object):
    def __init__(self):
        object.__init__(self)

    def check(self, s, K):
        cntOfChar = len(s)
        indexes = range(cntOfChar)
        rest = set()
        for c in combinations(indexes, K):
            c = sorted(c)
            t = ''
            begin = 0
            for i in c:
                t = t + s[begin:i]
                begin = i + 1
            t = t + s[begin:]
            if t in rest:
                return 'Uncertain'
            rest.add(t)

        return 'Certain'

def main():
    obj = Decipherability()
#    print obj.check('snuke', 2)
    print obj.check('deagcbfdeagcbfdeagcbfdeagcbfdeagcbfdeagcbf', 6)

if __name__ == '__main__':
    main()
