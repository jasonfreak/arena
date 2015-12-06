from functools import wraps

class BoardFolding(object):
    def __init__(self):
        object.__init__(self)

    def tonumber(self, character):
        if character.isdigit():
            return int(character)
        if character.islower():
            return 10 + ord(character) - ord('a')
        elif character.isupper():
            return 36 + ord(character) - ord('A')
        elif character == '#':
            return 62
        else:
            return 63


    def tuplePaper(self, paper):
        result = ()
        cntOfRows = len(paper)
        cntOfColumns = len(paper[0])
        for i in range(cntOfRows):
            row = ()
            for j in range(cntOfColumns):
                row = row + (paper[i][j],)
            result = result + (row,)
        return result

    def listPaper(self, paper):
        result = [] 
        cntOfRows = len(paper)
        cntOfColumns = len(paper[0])
        for i in range(cntOfRows):
            row = []
            for j in range(cntOfColumns):
                row.append(paper[i][j])
            result.append(row)
        return result

    def isValidFold(self, isRow, i, paper):
        cntOfRows = len(paper)
        cntOfColumns = len(paper[0])
        cntOfPartA = i + 1
        cntOfPartB = ((len(paper) if isRow else len(paper[0]))) - i - 1

#        print 'debug[57]', cntOfPartA, cntOfPartB
        isA2B = True if cntOfPartA <= cntOfPartB else False

        if isRow:
            if isA2B:
                for k in range(i+1):
                    for j in range(cntOfColumns):
                        if paper[k][j] != paper[2*i+1-k][j]:
                            return False
            else:
                for k in range(i+1, cntOfRows):
                    for j in range(cntOfColumns):
                        if paper[k][j] != paper[i-(k-i-1)][j]:
                            return False
        else:
            if isA2B:
                for k in range(i+1):
                    for j in range(cntOfRows):
#                        print 'debug[74]', i, j, k, paper
                        if paper[j][k] != paper[j][2*i+1-k]:
                            return False
            else:
                for k in range(i+1, cntOfColumns):
                    for j in range(cntOfRows):
#                        print 'debug[81]', i, j, k, paper
                        if paper[j][k] != paper[j][i-(k-i-1)]:
                            return False
        return True

    def howManyByRecursion(self, boards, offset, paper):
#        print 'debug[73]', offset, paper
        if boards.get((offset, paper), False):
            return
        boards[(offset, paper)] = True

        cntOfRows = len(paper)
        cntOfColumns = len(paper[0])

        for i in range(cntOfRows-1):
            if self.isValidFold(True, i, paper):
                cntOfPartA = i + 1
                cntOfPartB = len(paper) - i - 1
                isA2B = True if cntOfPartA <= cntOfPartB else False
                isB2A = True if cntOfPartA >= cntOfPartB else False
                new_paper = self.listPaper(paper)
                if isA2B:
                    new_paper = new_paper[i+1:]
                    new_offset = (offset[0]+i+1, offset[1])
                    self.howManyByRecursion(boards, new_offset, self.tuplePaper(new_paper))
                if isB2A:
                    new_paper = new_paper[:i+1]
                    new_offset = offset
                    self.howManyByRecursion(boards, new_offset, self.tuplePaper(new_paper))

        for j in range(cntOfColumns-1):
            if self.isValidFold(False, j, paper):
                cntOfPartA = j + 1
                cntOfPartB = len(paper[0]) - j - 1
                isA2B = True if cntOfPartA <= cntOfPartB else False
                isB2A = True if cntOfPartA >= cntOfPartB else False
                new_paper = self.listPaper(paper)
                if isA2B:
                    new_paper = [row[j+1:] for row in new_paper]
                    new_offset = (offset[0], offset[1]+j+1)
                    self.howManyByRecursion(boards, new_offset, self.tuplePaper(new_paper))
                if isB2A:
                    new_paper = [row[:j+1] for row in new_paper]
                    new_offset = offset
                    self.howManyByRecursion(boards, new_offset, self.tuplePaper(new_paper))


    def howMany(self, N, M, compressedPaper):
        paper = [[(self.tonumber(compressedPaper[i][j/6]) >> (j%6)) % 2 for j in range(M)] for i in range(N)]
#        print 'debug[111]', paper
        boards = {}
        self.howManyByRecursion(boards, (0, 0), self.tuplePaper(paper))
        return len(boards)

def main():
    obj = BoardFolding()
    print obj.howMany(2, 7, ('@@', '@@'))

if __name__ == '__main__':
    main()
