class ConnectingCars(object):
    def __init__(self):
        object.__init__(self)

    def energy(self, positions, lengths, x):
        result = 0
        cntOfCar = len(positions)
        for i in range(cntOfCar):
            result = result + abs(x-positions[i])
            x = x + lengths[i]
        print 'debug[11]', result
        return long('%.0f' % result) if type(result) is float else result
            

    def minimizeCost(self, positions, lengths):
        result = 0
        cntOfCar = len(positions)
        indexes = sorted(range(cntOfCar), key=lambda x:positions[x])
        lengths = [lengths[i] for i in indexes]
        positions = [positions[i] for i in indexes]
        lenOfTrain = sum(lengths)
        print 'debug[11]', positions, lengths, lenOfTrain

        begin = positions[0]
        end = positions[-1] - lenOfTrain
        print 'debug[15]', begin, end

        A = cntOfCar
        bs = []
        la = 0
        for i in range(cntOfCar):
            print 'debug[21]', la, positions[i]
            bs.append(la-positions[i])
            la = la + lengths[i]
        B = 2 * sum(bs)
        C = reduce(lambda x, y: x + pow(y, 2), bs)
        print 'debug[24]', bs, A, B, C
        mid = - float(B) / (2 * A)

        func = lambda x: A * pow(x, 2) + B * x + C
        possible = (begin, mid, end) if begin <= mid and mid <= end else (begin, end)
        x = min(possible, key=lambda x: func(x))
        print 'debug[41]', begin, mid, end, x
#        print 'debug[43]', self.energy(positions, lengths, 5)

        return self.energy(positions, lengths, mid)

def main():
    obj = ConnectingCars()
#    print obj.minimizeCost((1, 3, 10, 20), (2, 2, 5, 3))
#    print obj.minimizeCost((4, 10, 100, 13, 80), (5, 3, 42, 40, 9))
    print obj.minimizeCost((5606451, 63581020, 81615191, 190991272, 352848147, 413795385, 468408016, 615921162, 760622952, 791438427), (42643329, 9909484, 58137134, 99547272, 39849232, 15146704, 144630245, 604149, 15591965, 107856540))

if __name__ == '__main__':
    main()
