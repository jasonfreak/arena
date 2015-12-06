class GreaterGameDiv2(object):
    def __init__(self):
        object.__init__(self)

    def calc(self, snuke, sothe):
        cntOfCards = len(snuke)
        return reduce(lambda x, y: x + 1 if snuke[y] > sothe[y] else x, range(cntOfCards), 0)

def main():
    obj = GreaterGameDiv2()
    print obj.calc((1,3), (4,2))
    print obj.calc((1,3,5,7,9), (2,4,6,8,10))
    print obj.calc((2,), (1,))
    print obj.calc((3,5,9,16,14,20,15,17,13,2), (6,18,1,8,7,10,11,19,12,4))

if __name__ == '__main__':
    main()
    
