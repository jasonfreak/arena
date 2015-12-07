class ChocolateDividingEasy(object):
    def __init__(self):
        object.__init__(self)

    def getPiece(self, chocolate, pos1, pos2):
        result = 0
        for i in range(pos1[0], pos2[0]):
            for j in range(pos1[1], pos2[1]):
#                print 'debug[9]', i, j
                result = result + int(chocolate[i][j])
        return result

    def findBest(self, chocolate):
        library = {}

        cntRow = len(chocolate)
        cntCol = len(chocolate[0])

        best = 0
        for i_1 in range(1, cntRow-1):
            for i_2 in range(i_1+1, cntRow):
                for j_1 in range(1, cntCol-1):
                    for j_2 in range(j_1+1, cntCol):
#                        print 'debug[23]', i_1, i_2, j_1, j_2
                        pieces = []

                        poss_0 = ((0, 0), (i_1, j_1))
#                        print 'debug[28]', poss_0
                        pieces.append(library.get(poss_0, self.getPiece(chocolate, poss_0[0], poss_0[1])))
                        library[poss_0] = pieces[-1]

                        
                        poss_1 = ((0, j_1), (i_1, j_2))
#                        print 'debug[28]', poss_1
                        pieces.append(library.get(poss_1, self.getPiece(chocolate, poss_1[0], poss_1[1])))
                        library[poss_1] = pieces[-1]


                        poss_2 = ((0, j_2), (i_1, cntCol))
#                        print 'debug[28]', poss_2
                        pieces.append(library.get(poss_2, self.getPiece(chocolate, poss_2[0], poss_2[1])))
                        library[poss_2] = pieces[-1]

                            
                        poss_3 = ((i_1, 0), (i_2, j_1))
#                        print 'debug[28]', poss_3
                        pieces.append(library.get(poss_3, self.getPiece(chocolate, poss_3[0], poss_3[1])))
                        library[poss_3] = pieces[-1]

                        
                        poss_4 = ((i_1, j_1), (i_2, j_2))
#                        print 'debug[28]', poss_4
                        pieces.append(library.get(poss_4, self.getPiece(chocolate, poss_4[0], poss_4[1])))
                        library[poss_4] = pieces[-1]


                        poss_5 = ((i_1, j_2), (i_2, cntCol))
#                        print 'debug[28]', poss_5
                        pieces.append(library.get(poss_5, self.getPiece(chocolate, poss_5[0], poss_5[1])))
                        library[poss_5] = pieces[-1]


                        poss_6 = ((i_2, 0), (cntRow, j_1))
#                        print 'debug[28]', poss_6
                        pieces.append(library.get(poss_6, self.getPiece(chocolate, poss_6[0], poss_6[1])))
                        library[poss_6] = pieces[-1]

                        
                        poss_7 = ((i_2, j_1), (cntRow, j_2))
#                        print 'debug[28]', poss_7
                        pieces.append(library.get(poss_7, self.getPiece(chocolate, poss_7[0], poss_7[1])))
                        library[poss_7] = pieces[-1]


                        poss_8 = ((i_2, j_2), (cntRow, cntCol))
#                        print 'debug[28]', poss_8
                        pieces.append(library.get(poss_8, self.getPiece(chocolate, poss_8[0], poss_8[1])))
                        library[poss_8] = pieces[-1]


#                        print 'debug[80]', library


                        worst = min(pieces)

                        if worst > best:
                            best = worst

        return best

def main():
    obj = ChocolateDividingEasy()
    print obj.findBest(('9768', '6767', '5313'))
    print obj.findBest(('36753562', '91270936', '06261879', '20237592', '28973612', '93194784'))


if __name__ == '__main__':
    main()
        
