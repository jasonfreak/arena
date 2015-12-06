from sys import maxint

class TaroCutting(object):
    def __init__(self):
        object.__init__(self)

    def getNumber(self, height, add, device, time):
        if time == 0:
            return sum(height)
        cntOfTree = len(height)
        height = map(lambda x, y: x + y, height, add)
#        print 'debug[8]', time, height
#        raw_input()
        deviceAvaliable = [list(filter(lambda x: x < h, device)) + [h] for h in height] 
        cur = 0
        poss = [-1] * cntOfTree
        result = maxint
        while cur >= 0:
            poss[cur] = poss[cur] + 1
            if poss[cur] == len(deviceAvaliable[cur]):
                poss[cur] = -1
                cur = cur - 1
            else:
                if deviceAvaliable[cur][poss[cur]] != height[cur]:
                    if deviceAvaliable[cur][poss[cur]] in [deviceAvaliable[i][poss[i]] for i in range(cur)]:
                        continue
                if cur == cntOfTree - 1:
#                    print 'debug[28]', deviceAvaliable
#                    print 'debug[29]', [deviceAvaliable[i][poss[i]] for i in range(cntOfTree)]
                    tmp = self.getNumber([deviceAvaliable[i][poss[i]] for i in range(cntOfTree)], add, device, time-1)
                    if tmp < result:
#                        print 'debug[32]', [deviceAvaliable[i][poss[i]] for i in range(cntOfTree)]
                        result = tmp
                else:
                    cur = cur + 1

        return result
        
def main():
    obj = TaroCutting()
#    print obj.getNumber((4, 7), (7, 1), (7, ), 1)
#    print obj.getNumber((3, 1, 2), (1, 1, 1), (7, 7, 7), 2)
#    print obj.getNumber((100, 50), (75, 30), (200, 100, 50), 2)
    print obj.getNumber((7, 10, 1, 7, 5, 4, 11, 5, 7, 9, 10, 8), (1, 3, 4, 10, 2, 1, 6, 4, 8, 7, 5, 10), (7, 1, 5, 10), 3)
#    print obj.getNumber((35, 45, 32, 8), (2, 25, 31, 5), (29, 28, 3, 11, 28, 37), 8)

if __name__ == '__main__':
    main()
