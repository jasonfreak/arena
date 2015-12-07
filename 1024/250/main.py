class BuildingTowersEasy(object):
    def __init__(self):
        object.__init__(self)


    def maxHeight(self, N, x, t):
        x = [1] + list(x) + [N]
        t = [0] + list(t) + [N-1]

        cntOfLimit = len(x)

        result = 0
        for i in range(1, cntOfLimit):
            left = 0
            for j in range(1, i): 
                left  = min((t[i], left + abs(x[i]-x[i-1])))
            right = t[-1]
            for j in range(cntOfLimit-2, i, -1): 
                right  = min((t[i], right + abs(x[i]-x[i+1])))

            print 'debug[21]', left, right

            height = min((left, right)) + abs(x[i]-x[i-1]) / 2
            if height > result:
                result = height

        height = t[-1] + N - x[-1]
        if height > result:
            result = height

        return result

def main():
    obj = BuildingTowersEasy()
#    print obj.maxHeight(10, (3, 8), (1, 1))
#    print obj.maxHeight(100000, (), ())
    print obj.maxHeight(2718, (1,30,400,1300,2500), (100000,100000,100000,100000,100000))
#    print obj.maxHeight(20, (4,7,13,15,18), (3,8,1,17,16))
#    print obj.maxHeight(447, (32,35,55,60,61,88,91,97,128,151,181,186,192,196,198,237,259,268,291,314,341,367,389,390,391,428,435), (81,221,172,641,25,953,330,141,123,440,692,394,200,649,78,726,50,810,501,4,216,407,2,172,0,29,14))

if __name__ == '__main__':
    main()
