class LuckyXor(object):
    def __init__(self):
        object.__init__(self)

    def construct(self, a):
        for b in range(a, 101):
            c = str(b ^ a).replace('4', '').replace('7', '')
            if len(c) == 0:
                return b
        return -1

def main():
    obj = LuckyXor()
    print obj.construct(4)

if __name__ == '__main__':
    main()

