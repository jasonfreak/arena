class SquareOfSquareMatrix(object):
    def __init__(self):
        object.__init__(self)

    def countByRecursion(self, result, zeroRow, zeroColumn, n):
        print 'debug[6]', zeroRow, zeroColumn
        if (tuple(zeroRow), tuple(zeroColumn)) not in result:
            result.add((tuple(zeroRow), tuple(zeroColumn)))
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if i == j:
                        continue
                    if i in zeroRow or j in zeroColumn:
                        continue
                    elif j in zeroRow and i in zeroColumn:
                        continue
                    else:
                        print 'debug[13]', i, j
                        self.countByRecursion(result, zeroRow.union(set((j,))), zeroColumn.union(set((i,))), n)

    def count(self, n, r, c):
        zeroRow = set()
        zeroColumn = set()
        cntOfGivenOnes = len(r)
        for i in range(cntOfGivenOnes):
            zeroRow.add(c[i])
            zeroColumn.add(r[i])
            if r[i] in zeroRow or c[i] in zeroColumn:
                return 0
        result = set()
        self.countByRecursion(result, zeroRow, zeroColumn, n)
        return len(result)


def main():
    obj = SquareOfSquareMatrix()
#    print obj.count(2, (), ())
#    print obj.count(3, (1,), (1,))
#    print obj.count(3, (1,), (2,))

if __name__ == '__main__':
    main()
