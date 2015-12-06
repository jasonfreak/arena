class TaroFillingAStringDiv2(object):
    def __init__(self):
        object.__init__(self)

    def getNumber(self, S):
        result = 0
        paragraghs = []
        cntOfChar = len(S)
        begin = -1
        end = 0
        for end in range(cntOfChar):
            if S[end] == '?':
                continue
            else:
                paragraghs.append((begin, end))
                begin = end
        if S[end] == '?':
            paragraghs.append((begin, cntOfChar))

        for paragragh in paragraghs:
            begin = paragragh[0]
            end = paragragh[1]
            if begin == -1 or end == cntOfChar:
                continue
            else:
                if (S[begin] != S[end] and (end - begin) % 2 == 0) or (S[begin] == S[end] and (end - begin) % 2 == 1):
                    result += 1
                
        return result

def main():
    obj = TaroFillingAStringDiv2()
    print obj.getNumber('A?A')

if __name__ == '__main__':
    main()
