class TaroFillingAStringDiv1(object):
    def __init__(self):
        object.__init__(self)

    def getNumber(self, N, position, value):
        result = 1
        cntOfValue = len(value)
        indexes = range(cntOfValue)
        sortedIndexes = sorted(indexes, key=lambda x: position[x])
        position = map(lambda x:position[x], sortedIndexes)
        value = map(lambda x:value[x], sortedIndexes)

        for i in range(cntOfValue-1):
            if position[i+1] - position[i] == 1:
                result *= 1
            elif (value[i] != value[i+1] and (position[i+1] - position[i]) % 2 == 0):
                result *= (((position[i+1] - position[i] - 1) / 2 + 1) * 2)

            elif (value[i] == value[i+1] and (position[i+1] - position[i]) % 2 == 1):
                result *= (((position[i+1] - position[i] - 1) / 2) * 2 + 1)
            else:
                result *= 1

        return result % 1000000007

def main():
    obj = TaroFillingAStringDiv1()
    print obj.getNumber(3, (1, 3), 'AB')
    print obj.getNumber(4, (2, 1, 3, 4), 'ABBA')
    print obj.getNumber(25, (23, 4, 8, 1, 24, 9, 16, 17, 6, 2, 25, 15, 14, 7, 13), 'ABBBBABABBAAABA')
    print obj.getNumber(305, (183, 115, 250, 1, 188, 193, 163, 221, 144, 191, 92, 192, 58, 215, 157, 187, 227, 177, 206, 15, 272, 232, 49, 11, 178, 59, 189, 246), 'ABAABBABBAABABBBBAAAABBABBBA')

if __name__ == '__main__':
    main()
