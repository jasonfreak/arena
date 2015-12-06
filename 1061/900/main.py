class LuckySum(object):
    def __init__(self):
        object.__init__(self)

    def construct(self, note):
        note = list(note)
        cntOfdigit = len(note)
        isPlus = False
        for i in range(cntOfdigit-1, -1, -1):
            if note[i].isdigit(): 
                if int(note[i]) in (1, 4, 2, 5):
                    isPlus = True
                note[i] = int(note[i])
            else:
                if i == 1 and not note[i-1].isdigit():
                    if isPlus:
                        note[i] = 2
                    else:
                        note[i] = 1
                    note[i-1] = 1
                elif i == 0:
                    if isPlus:
                        note[i] = 8
                    else:
                        note[i] = 9
                else:
                    if isPlus:
                        note[i] = 1
                    else:
                        note[i] = 8
        return reduce(lambda x, y: x * 10 + note[y], range(cntOfdigit), 0)

def main():
    obj = LuckySum()
    print obj.construct('4?4')

if __name__ == '__main__':
    main()

