from math import log
class KitayutaMart2(object):
    def __init__(self):
        object.__init__(self)

    def numBought(self, K, T):
        return int(log(T / K + 1, 2))

def main():
    obj = KitayutaMart2()
    print obj.numBought(150, 1050)

if __name__ == '__main__':
    main()
