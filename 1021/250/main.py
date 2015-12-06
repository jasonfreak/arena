class BacteriesColony(object):
    def __init__(self):
        object.__init__(self)

    def changeSize(self, colonies):
        result = ()
        cntOfColony = len(colonies)
        result = result + (colonies[0], )
        for i in range(1, cntOfColony-1):
            result = result + ((colonies[i]+1) if colonies[i-1] > colonies[i] and colonies[i+1] > colonies[i] else (colonies[i]-1) if colonies[i-1] < colonies[i] and colonies[i+1] < colonies[i] else colonies[i], )
        result = result + (colonies[-1], )
        return result

    def performTheExperiment(self, colonies):
        while True:
            new = self.changeSize(colonies)
#            print 'debug[17]', new
            if new == colonies:
                break
            colonies = new
        return colonies

def main():
    obj = BacteriesColony()
    print obj.performTheExperiment((5, 3, 4, 6, 1))

if __name__ == '__main__':
    main()
