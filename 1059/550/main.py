class stack(list):
    def __init__(self):
        list.__init__(self)

    def pop(self):
        result = self[-1]
        del self[-1]
        return result

    def push(self, e):
        self.append(e)

    def isEmpty(self):
        return True if len(self) == 0 else False

    def top(self):
        return self[-1]

class BearPlaysDiv2(object):
    def __init__(self):
        object.__init__(self)

    def equalPilesByRecursion(self, A, B, C, result):
#        print 'debug[6]', A, B, C
#        raw_input()
        if A == B and B == C:
            return True
        else:
            sortedT = tuple(sorted((A, B, C), reverse=True))
            if 0 in (A, B, C):
                return False
            if sortedT in result:
                return False
            else:
                result.add(sortedT)
                return self.equalPilesByRecursion(sortedT[0]-sortedT[1], 2*sortedT[1], sortedT[2], result) \
                    or self.equalPilesByRecursion(sortedT[0]-sortedT[2], sortedT[1], 2*sortedT[2], result) \
                    or self.equalPilesByRecursion(sortedT[0], sortedT[1]-sortedT[2], 2*sortedT[2], result)

    def equalPilesByStack(self, A, B, C):
        done = set()
        sortedT = tuple(sorted((A, B, C), reverse=True))
        process = stack()
        process.push([sortedT, 0])
        result = False
        while not process.isEmpty():
            numbers, branch = process.top()
#            print 'debug[48]', numbers, branch
#            raw_input()
            if branch == 0:
                if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
                    result = True
                    process.pop()
                    continue
                if 0 in numbers:
                    result = False
                    process.pop()
                    continue
                if numbers in done:
                    result = False
                    process.pop()
                    continue
            done.add(numbers)
            if result == True or branch == 3:
                process.pop()
                continue
            if branch == 0:
                sortedT = tuple(sorted((numbers[0]-numbers[1], 2*numbers[1], numbers[2]), reverse=True))
                new_branch = 1
            elif branch == 1:
                sortedT = tuple(sorted((numbers[0]-numbers[2], numbers[1], 2*numbers[2]), reverse=True))
                new_branch = 2
            elif branch == 2:
                sortedT = tuple(sorted((numbers[0]-numbers[2], numbers[1], 2*numbers[2]), reverse=True))
                new_branch = 3
            tp = process.top()
            tp[1] = new_branch
            process.push([sortedT, 0])
        return result


    def equalPiles(self, A, B, C):
#        result = set()
#        return 'possible' if self.equalPilesByRecursion(A, B, C, result) else 'impossible'
        return 'possible' if self.equalPilesByStack(A, B, C) else 'impossible'

def main():
    obj = BearPlaysDiv2()
    print obj.equalPiles(283, 433, 208)
#    print obj.equalPiles(10, 15, 35)

if __name__ == '__main__':
    main()
