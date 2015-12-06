from sys import maxint

class ForgetfulAddition(object):
    def __init__(self):
        object.__init__(self)

    def minNumber(self, expression):
        result = maxint
        cntOfNums = len(expression)
        for i in range(1, cntOfNums):
            plus = int(expression[:i]) + int(expression[i:])
            if plus < result:
                result = plus
        return result
                
            
