class Bracket107(object):
    def __init__(self):
        object.__init__(self)

    def check(self, s):
        stack = []
        for c in s:
            if len(stack) > 0 and  stack[0] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)
#        print 'debug[19]', s, stack
        if len(stack) > 0:
            return False
        else:
            return True

    def yetanother(self, s):
        result = set()
        cntOfC = len(s)
        for i in range(cntOfC):
            for j in range(cntOfC):
                if i != j: 
                    if i < j:
                        t = s[:i] + s[i+1:j] + s[i:i+1] + s[j:]
                    else:
                        t = s[:j+1] + s[i:i+1] + s[j+1:i] + s[i+1:]
                    if t == s:
                        continue
                    if self.check(t):
#                        print 'debug[23]', t, i, j
                        result.add(t)

#        print 'debug[30]', result
        return len(result)

def main():
    obj = Bracket107()
#    print obj.yetanother('(())')
#    print obj.yetanother('(())()')
    print obj.yetanother('(((())))')

if __name__ == '__main__':
    main()
