class DecipherabilityEasy(object):
    def __init__(self):
        object.__init__(self)

    def check(self, s, t):
        cntOfS = len(s)
        cntOfT = len(t)
        if cntOfS != cntOfT + 1:
            return 'Impossible'
        for i in range(cntOfS):
            if s[:i] + s[i+1:] == t:
                return 'Possible'
        return 'Impossible'

def main():
    obj = DecipherabilityEasy()
    print obj.check('snuke', 'skue')

if __name__ == '__main__':
    main()
