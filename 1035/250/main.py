class ValueOfString(object):
    def __init__(self):
        object.__init__(self)

    def val(self, c):
        return ord(c) - ord('a') + 1

    def findValue(self, s):
        k = {}
        for c1 in s:
            if c1 not in k:
                count = 0
                for c2 in s:
                    if self.val(c2) <= self.val(c1):
                        count += 1
                k[c1] = count

        result = 0
        for c in s:
            result += k[c] * self.val(c)
                
        return result

def main():
    obj = ValueOfString()
    print obj.findValue('babca')

if __name__ == '__main__':
    main()
