class WaitingForBus(object):
    def __init__(self):
        object.__init__(self)

    def whenWillBusArrive(self, time, prob, s):
        result = 0
        cntOfBuses = len(prob)
        mtime = min(time)
        maxCntOfTrips = s / mtime if s % mtime == 0 else s / mtime + 1
#        print 'debug[9]', maxCntOfTrips, cntOfBuses
        
        cur = 0
        poss = [-1] * maxCntOfTrips

        while cur >= 0:
            poss[cur] = poss[cur] + 1
#            print 'debug[15]', cur, poss
            if poss[cur] == cntOfBuses:
                poss[cur] = -1
                cur = cur - 1
            else:
                t = sum([time[poss[i]] for i in range(cur+1)])
#                print 'debug[22]', t, s
                if t >= s:
                    result = result + (t-s) * reduce(lambda x, y: x * y, [float(prob[poss[i]]) / 100 for i in range(cur+1)])
#                    print 'debug[25]', result
                else:
                    cur = cur + 1

        return result

def main():
    obj = WaitingForBus()
    print obj.whenWillBusArrive((5, 100), (90, 10), 5)
#    print obj.whenWillBusArrive((5,), (100,), 101)
#    print obj.whenWillBusArrive((5, 10), (50, 50), 88888)
#    print obj.whenWillBusArrive((8990, 14526, 92133, 94958, 15718, 7457, 16830, 76565, 44296, 8615, 74026, 57068, 21713, 14207, 40014, 39977, 80364, 12935, 20382, 90847, 98641, 39372, 3245, 80436, 49640, 20530, 78329, 254, 53142, 6243, 45651, 65389, 27767, 98333, 40780, 7891, 69896, 70919, 85008, 55482, 43946, 4832, 28240, 85009, 54556, 42790, 89978, 37803, 85445, 8769, 19554, 84970, 31962, 24993, 90546, 34676, 24773, 3005, 16348, 80584, 40653, 81474, 23911, 884, 23029, 32712, 50932, 30700, 89681, 62330, 38095), (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 3, 2, 2, 1, 3, 2, 1, 1, 1, 3, 1, 1, 2, 2, 1, 1, 3, 2, 1, 2, 1, 1, 1, 1, 1), 1232)

    
if __name__ == '__main__':
    main()

            

        
