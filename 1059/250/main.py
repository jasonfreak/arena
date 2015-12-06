class BearCheats(object):
    def __init__(self):
        object.__init__(self)

    def eyesight(self, A, B):
        A = str(A)
        B = str(B)
        cntOfDigits = len(A)
        result = 0
        for i in range(cntOfDigits):
            if A[i] != B[i]:
                result = result + 1
            if result > 1:
                return 'glasses'

        return 'happy'
