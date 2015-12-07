class TheGridDivOne(object):
    def __init__(self):
        object.__init__(self)

    def walk(self, begin, seconds, blocks):
#        print 'debug[6]', begin, seconds
#        print 'debug[7]', map(lambda x: (x[0]-1, x[1]), filter(lambda x: x[1] == begin[1] and begin[0] < x[0], blocks)) + [(begin[0]+seconds, begin[1])]
        east = min(map(lambda x: (x[0]-1, x[1]), filter(lambda x: x[1] == begin[1] and begin[0] < x[0], blocks)) + [(begin[0]+seconds, begin[1])], key=lambda x:x[0])
        seconds = seconds - (east[0] - begin[0])
        if seconds == 0:
            return east[0]
        else:
            north = (east[0], east[1]+1)
            w1 = self.walk(north, seconds-1, blocks) if north not in blocks else 0
            south = (east[0], east[1]-1)
            w2 = self.walk(south, seconds-1, blocks) if south not in blocks else 0
            west = (east[0]-1, east[1])
            w3 = self.walk(west, seconds-1, blocks.union(set((begin, )))) if west not in blocks else 0
            return max((w1, w2, w3))

    def find(self, x, y, k):
        blocks = set()
        cntOfBlock = len(x)
        for i in range(cntOfBlock):
            blocks.add((x[i], y[i]))
#        print 'debug[20]', blocks
        return self.walk((0, 0), k, blocks)

def main():
    obj = TheGridDivOne()
#    print obj.find((1, 1, 1, 1), (-2, -1, 0, 1), 4)
#    print obj.find((-1, 0, 0, 1), (0, -1, 1, 0), 9)
#    print obj.find((), (), 1000)
    print obj.find((1,0,0,-1,-1,-2,-2,-3,-3,-4,-4), (0,-1,1,-2,2,-3,3,-4,4,-5,5), 47)

if __name__ == '__main__':
    main()
