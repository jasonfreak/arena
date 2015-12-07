class ChristmasTreeDecorationDiv2(object):
    def __init__(self):
        object.__init__(self)

    def solve(self, col, x, y):
        result = 0
        cntOfRibbons = len(x)
        for i in range(cntOfRibbons):
            if col[x[i]-1] != col[y[i]-1]:
                result = result + 1
        return result

def main():
    obj = ChristmasTreeDecorationDiv2()
    print obj.solve((1,2,3,3), (1,2,3), (2,3,4))

if __name__ == '__main__':
    main()
