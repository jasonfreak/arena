class TaroJiroDividing(object):
    def __init__(self):
        object.__init__(self)

    def genNumber(self, A):
        while A % 2 == 0:
            yield A 
            A /= 2
        yield A

    def getNumber(self, A, B):
        result = 0
        numbers = set()
        for number in self.genNumber(A):
            numbers.add(number)
        for number in self.genNumber(B):
            if number in numbers:
                result += 1

        return result

def main():
    obj = TaroJiroDividing()
#    print obj.getNumber(8, 4)
    print obj.getNumber(7, 4)

if __name__ == '__main__':
    main()
