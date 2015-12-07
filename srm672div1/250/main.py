class Procrastination(object):
    def __init__(self):
        object.__init__(self)

    def nextHour(self, n, h):
        tmp = n
        base = 2
        result = set()
        result.add(1)
        while True:
            if base > n:
                break
            if n % base == 0:
#                print 'debug[14]', n, base
                for e in tuple(result):
                    result.add(base*e)
                n /= base
            else:
                base += 1
#        print 'debug[18]',tmp, sorted(result)
        for temp in sorted(result):
            if temp > h:
                return temp

    def findFinalAssignee(self, n):
        if n <= 3:
            return n

        h = 2
        while True:
            if 2 * h > n:
                return n
            else:
#                print 'debug[25]', h, n
                if n % h == 0 and n / h > 1:
                    n += 1
                elif (n-1) % h == 0 and (n-1) / h > 1:
                    n -= 1
#                print 'debug[30]', h, n
                nh1 = self.nextHour(n-1, h)
                nh2 = self.nextHour(n, h)
                h = min((nh1, nh2))
#                print 'debug[32]', h

def main():
    obj =  Procrastination()
    print obj.findFinalAssignee(196248)

if __name__ == '__main__':
    main()
