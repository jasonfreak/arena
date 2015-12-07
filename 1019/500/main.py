class LostCharacter(object):
    def __init__(self):
        object.__init__(self)

    def getmins(self, strs):
        cntOfStr = len(strs)
        pos = {}
        index = {}
        for i in range(cntOfStr):
            pos[strs[i]] = 0
            index[strs[i]] = i

        for s1 in pos:
            order = 0
            for s2 in strs:
                if index[s1] != index[s2]:
                    if s2.replace('?', 'z') < s1.replace('?', 'a'):
#                        print 'debug[15]', s1, s1.replace('?', 'a'), s2, s2.replace('?', 'z')
                        order = order + 1
            pos[s1] = order
        
        return tuple([pos[s] for s in strs])

def main():
    obj = LostCharacter()
#    print obj.getmins(('?ala', 'ara', 'baba'))
    print obj.getmins(('a?', 'a', 'a', 'ab', 'aa'))

if __name__ == '__main__':
    main()
