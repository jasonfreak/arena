from math import sqrt
from math import pow

class QuadraticLaw(object):
    def __init__(self):
        object.__init__(self)

    def getTime(self, d):
        end = int((-1+sqrt(1+4*d))/2)
        print 'debug[11]', end
        
        i = end
        while i > 1:
            if pow(i, 2) + i <= d:
                return i

        return 0

def main():
    obj = QuadraticLaw()
    print obj.getTime(1)
    print obj.getTime(2)
    print obj.getTime(5)
    print obj.getTime(6)
    print obj.getTime(7)
    print obj.getTime(1482)
    print obj.getTime(1000000000000000000)

if __name__ == '__main__':
    main()

            



