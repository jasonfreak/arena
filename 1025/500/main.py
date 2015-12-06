class TravellingSalesmanEasy(object):
    def __init__(self):
        object.__init__(self)

    def getMaxProfit(self, M, profit, city, visit):
        profitOfCity = {}
        cntOfCity = len(city)
        for i in range(cntOfCity):
            profits = profitOfCity.get(city[i], [])
            profitOfCity[city[i]] = sorted(profits + [profit[i]], reverse=True)
#            print 'debug[16]', profitOfCity

        result = 0
        for c in visit:
            if len(profitOfCity.get(c, [])) == 0:
                p = 0
            else:
                p = profitOfCity[c][0]
                del profitOfCity[c][0]
            result = result + p
                    
        return result

def main():
    obj = TravellingSalesmanEasy()
#    print obj.getMaxProfit(2, (3, 10), (1, 1), (2, 1))
    print obj.getMaxProfit(1, (3,5,2,6,4), (1,1,1,1,1), (1,1,1))

if __name__ == '__main__':
    main()
