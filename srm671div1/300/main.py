from itertools import combinations
class BearCries(object):
    def __init__(self):
        object.__init__(self)

    def countByRecursion(self, message):
        cntOfC = len(message)
        if message[0] != ':':
            return 0
        result = 0
        whereUnderscores = []
        for i in range(1, cntOfC):
            if message[i] == ':' and whereUnderscores:
                cntOfUnderscore = len(whereUnderscores)
                for j in range(1, cntOfUnderscore+1):
                    cbs = combinations(whereUnderscores, j)
                    for cb in cbs:
                        remain = filter(lambda x: 

                for where in whereUnderscores:
                    message =
                result +=
            

    def count(self, message):
        return

def main():
    obj = BearCries()
    print obj.count()

if __name__ == '__main__':
    main()
