class BuyingTshirts(object):
    def __init__(self):
        object.__init__(self)

    def meet(self, T, Q, P):
        result = 0
        saveOfQ = saveOfP = 0
        cntOfDays = len(Q)
        for i in range(cntOfDays):
            saveOfP = saveOfP + P[i]
            saveOfQ = saveOfQ + Q[i]
            if saveOfP >= T and saveOfQ >= T:
                result = result + 1
            if saveOfP >= T:
                saveOfP = saveOfP % T
            if saveOfQ >= T:
                saveOfQ = saveOfQ % T
        return result

def main():
    obj = BuyingTshirts()
    print obj.meet(2, (1,2,1,2,1,2,1,2), (1,1,1,1,2,2,2,2))

if __name__ == '__main__':
    main()
