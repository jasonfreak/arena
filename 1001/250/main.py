class IdentifyingWood(object):
    def __init__(self):
        object.__init__(self)

    def findstr(self, s, lenOfS, t, lenOfT, pos):
        '''begin from pos, return isfound and next begin'''
        posOfS = pos
        posOfT = 0

        while posOfT < lenOfT:
            if posOfS == lenOfS:
#                print 'dbeug[12]'
                return (False, posOfS)
            while posOfS < lenOfS:
                if s[posOfS] == t[posOfT]:
#                    print 'debug[13]', posOfS, s[posOfS]
                    posOfS = posOfS + 1
                    posOfT = posOfT + 1
                    break
                posOfS = posOfS + 1

        posOfT = lenOfT - 1
        posOfS = posOfS - 1

        while posOfT >= 0:
            while posOfS >= pos:
                if s[posOfS] == t[posOfT]:
                    posOfS = posOfS - 1
                    posOfT = posOfT - 1
                    break
                posOfS = posOfS - 1

        return (True, posOfS-1)

    def check(self, s, t):
        lenOfS = len(s)
        lenOfT = len(t)

        posOfS = 0

        while posOfS < lenOfS:
            (isFound, posOfS) = self.findstr(s, lenOfS, t, lenOfT, posOfS)
            if isFound:
                return 'Yep, it\'s wood.'

        return 'Nope'

def main():
    obj = IdentifyingWood()
    print obj.check('absdefgh', 'asdf')
    print obj.check('oxoxoxox', 'ooxxoo')
    print obj.check('qwerty', 'qwerty')
    print obj.check('string', 'longstring')
    
if __name__ == '__main__':
    main()

    
