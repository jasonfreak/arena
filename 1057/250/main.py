class ChessFloor(object):
    def __init__(self):
        object.__init__(self)

    def minimumChanges(self, floor):
        positiveColors = {}
        negativeColors = {}

        cntOfRow = len(floor)
        cntOfCol = len(floor[0])

        for i in range(cntOfRow):
            for j in range(cntOfCol):
                if i % 2 == j % 2:
                    positiveColors[floor[i][j]] = positiveColors.get(floor[i][j], 0) + 1
                else:
                    negativeColors[floor[i][j]] = negativeColors.get(floor[i][j], 0) + 1

        positiveColor = max(positiveColors.keys(), key=lambda x: positiveColors[x])
        negativeColor = max(negativeColors.keys(), key=lambda x: negativeColors[x])

        if positiveColor != negativeColor:
            return cntOfRow * cntOfCol - (positiveColors[positiveColor] + negativeColors[negativeColor])
        else:
            positiveMax = positiveColors[positiveColor]
            positiveColors[positiveColor] = 0
            negativeMax = negativeColors[negativeColor]
            negativeColors[negativeColor] = 0

            positiveColor = max(positiveColors.keys(), key=lambda x: positiveColors[x])
            negativeColor = max(negativeColors.keys(), key=lambda x: negativeColors[x])

            return cntOfRow * cntOfCol - max((positiveMax + negativeColors[negativeColor], negativeMax + positiveColors[positiveColor]))
