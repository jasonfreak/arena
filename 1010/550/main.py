class MaximumBipartiteMatchingProblem(object):
    def __init__(self):
        object.__init__(self)

    def solveOrder(self, n1, n2, ans, d):
        m1 = (1 if n2 - ans > 0 else 0) * d
        m2 = ans - m1

        if m1 > 0 and m2 < d:
            return -1
        else:
#            print 'debug[12]', m1, m2
            return m1 * n2 + m2 * n1 - m1 * m2

    def solve(self, n1, n2, ans, d):
        return max((self.solveOrder(n1, n2, ans, d), self.solveOrder(n2, n1, ans, d)))

def main():
    obj = MaximumBipartiteMatchingProblem()
#    print obj.solve(5, 10, 5, 2)
#    print obj.solve(100000000, 87654321, 12345678, 54321)
#    print obj.solve(100000000, 100000000, 100000000, 100000000)

if __name__ == '__main__':
    main()
