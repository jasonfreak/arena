class ElectronicPetEasy(object):
    def __init__(self):
        object.__init__(self)

    def isDifficult(self, st1, p1, t1, st2, p2, t2):
        if st1 < st2:
            diff = (st2 - st1) % p1
            maxSec = max(((t1 - 1) * p1, diff + (t2 - 1) * p2))
            n = 1
            while (n * p1 - diff) % p2 != 0 and n * p1 <= maxSec:
                n = n + 1
            m = (n * p1 - diff) / p2
        else:
            diff = (st1 - st2) % p2
            maxSec = max((diff + (t1 - 1) * p1, (t2 - 1) * p2))
            m = 1
            while (m * p2 - diff) % p1 != 0 and m * p2 <= maxSec:
                m = m + 1
            n = (m * p2 - diff) / p1
        if t1 - n <= 0 or t2 - m <= 0:
            return 'Easy'
        else:
            return 'Difficult'

def main():
    obj = ElectronicPetEasy()
    print obj.isDifficult(1, 1, 1, 2, 2, 2)

if __name__ == '__main__':
    main()
