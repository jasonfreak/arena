from math import sqrt

class PointDistance(object):
    def __init__(self):
        object.__init__(self)

    def dot(self, v1, v2):
        return sum(map(lambda x, y: x * y, v1, v2))

    def isGreater(self, p1, p2, p3):
        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p3[0] - p2[0], p3[1] - p2[1])
        return True if self.dot(v1, v2) > 0 else False

    def findPoint(self, x1, y1, x2, y2):
        R = 10000
        p1 = (x1, y1)
        p2 = (x2, y2)
        if x1 == x2:
            p3 = (x1, sqrt(R-pow(x1, 2)))
            if not self.isGreater(p1, p2, p3):
                p3 = (x1, -sqrt(R-pow(x1, 2)))
        elif y1 == y2:
            p3 = (sqrt(R-pow(y1, 2)), y1)
            if not self.isGreater(p1, p2, p3):
                p3 = (-sqrt(R-pow(y1, 2)), y1)
        else:
            A = float(y1 - y2) / (x1 - x2)
            B = -A * x1 + y1
            x3 = float(-2*A*B + sqrt(4*pow(A,2)*pow(B,2)-4*(pow(A,2)+1)*(pow(B,2)-R))) / (2*(pow(A,2)+1))
            y3 = A * x3 + B
            p3 = (x3, y3)
            if not self.isGreater(p1, p2, p3):
                x3 = float(-2*A*B - sqrt(4*pow(A,2)*pow(B,2)-4*(pow(A,2)+1)*(pow(B,2)-R))) / (2*(pow(A,2)+1))
                y3 = A * x3 + B
                p3 = (x3, y3)
        return p3

def main():
    obj = PointDistance()
    print obj.findPoint(-50, -50, 50, -50)

if __name__ == '__main__':
    main()
