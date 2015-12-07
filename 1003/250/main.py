class GameOfStones(object):
    def __init__(self):
        object.__init__(self)

    def count(self, stones):
        cntStones = len(stones)

        if cntStones == 1:
            return 0

        sumStones = sum(stones)
        canEquallyAssign = True if sumStones % cntStones == 0 else False
        if not canEquallyAssign:
            return -1

        avgStones = sumStones / cntStones
        isAvgOdd = False if avgStones % 2 == 0 else True

        result = 0
        for stone in stones:
            isStoneOdd = False if stone % 2 == 0 else True
            if isAvgOdd != isStoneOdd:
                return -1
            if stone > avgStones:
                result = result + (stone - avgStones) / 2

        return result

def main():
    obj = GameOfStones()
#    print obj.count((7, 15, 9, 5))
#    print obj.count((10, 16))
#    print obj.count((2, 8, 4))
    print obj.count((1, 29, 11, 35, 57, 15, 85, 19, 5, 47, 53, 5, 63, 19, 13, 63, 27, 43, 53, 75, 67, 93, 33, 31, 47, 3, 63, 17, 11, 53, 35, 23, 17, 45, 31, 19, 63, 75, 5, 3, 49, 19, 11, 89, 21, 69, 71, 5, 45, 81, 31, 13, 11, 19, 7, 99, 33, 63, 19, 57, 73, 29, 35, 9, 47, 1, 17, 7, 13, 31, 5, 85, 95, 23, 45, 65, 63, 41, 81, 33, 45, 1, 15, 45, 19, 87, 51, 7, 13, 39, 1, 59, 29, 35, 1, 43))

if __name__ == '__main__':
    main()

            



            


