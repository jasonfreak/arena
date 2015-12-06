class PeacefulLine(object):
    def __init__(self):
        object.__init__(self)

    def check(self, y):
        last = y[0]
        for student in y[1:]:
            if student == last:
                return 'impossible'
            last = student
        return 'possible'

    def makeLine(self, x):
        cntOfStudent = len(x)
        heights = {}
        for student in x:
            heights[student] = heights.get(student, 0) + 1

        sortedHeights = sorted(heights.keys(), key=lambda x: heights[x], reverse=True)
#        print 'debug[20]', heights, sortedHeights

        y = [None] * cntOfStudent
        index = range(cntOfStudent)
        for height in sortedHeights:
            cntOfIndex = len(index)
            step = (cntOfIndex + 1) / heights[height]
#            print 'debug[27]', step
            for i in range(cntOfIndex):
                if i % step == 0:
                    y[index[i]] = height
                    index[i] = -1
            index = filter(lambda x: x >= 0, index)
#            print 'debug[32]', y

            
        return self.check(y)

def main():
    obj = PeacefulLine()
    print obj.makeLine((1, 2, 3, 4))
    print obj.makeLine((1, 1, 1, 2))
    print obj.makeLine((1,1,2,2,3,3,4,4))
    print obj.makeLine((3,3,3,3,13,13,13,13,3))

if __name__ == '__main__':
    main()
