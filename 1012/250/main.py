from math import sqrt

class TrianglesContainOrigin(object):
    def __init__(self):
        object.__init__(self)

    def points2vector(self, point1, point2):
        return (point2[0] - point1[0], point2[1] - point1[1])

    def innerProduct(self, vector1, vector2):
        return vector1[0] * vector2[0] + vector1[1] * vector2[1]

    def outerProduct(self, vector1, vector2):
        return vector1[0] * vector2[1] - vector1[1] * vector2[0]

    def distance(self, vector):
        return sqrt(self.innerProduct(vector, vector))

    def isTriangle(self, point1, point2, point3):
        vector0 = (0, 0)
        vector1 = self.points2vector(point1, point2)
        vector2 = self.points2vector(point3, point1)
        if vector1 == vector0 or vector2 == vector0:
            return False
        else:
            cosin = self.innerProduct(vector1, vector2) / (self.distance(vector1) * self.distance(vector2))
            if abs(cosin) == 1:
                return False
            else:
                return True

    def isLeft(self, point1, point2, point3):
        return True if self.outerProduct(self.points2vector(point1, point2), self.points2vector(point3, point1)) > 0 else False

    def isZeroBetween(self, point1, point2, point3):
        point0 = (0, 0)
        if self.isLeft(point1, point2, point3) and self.isLeft(point1, point2, point0) and self.isLeft(point1, point0, point3):
            return True
        elif self.isLeft(point1, point3, point2) and self.isLeft(point1, point3, point0) and self.isLeft(point1, point0, point2):
            return True
        else:
            return False

    def isZeroIn(self, point1, point2, point3):
        return self.isZeroBetween(point1, point2, point3) and self.isZeroBetween(point2, point3, point1) and self.isZeroBetween(point3, point1, point2)

    def count(self, x, y):
        result = 0
        cntOfPoints = len(x)
        for i in range(cntOfPoints-2):
            for j in range(i+1, cntOfPoints-1):
                for k in range(j+1, cntOfPoints):
                    point1 = (x[i], y[i])
                    point2 = (x[j], y[j])
                    point3 = (x[k], y[k])
                    if self.isTriangle(point1, point2, point3) and self.isZeroIn(point1, point2, point3):
                        result = result + 1
        return result

def main():
    obj = TrianglesContainOrigin()
#    print obj.count((-1, -1, 1), (1, -1, 0))
#    print obj.count((-1, -1, 1, 2), (1, -1, 2, -1))
#    print obj.count((-1,-2,3,3,2,1), (-2,-1,1,2,3,3))
    print obj.count((1,5,10,5,-5,7,-9,-6,-3,0,8,8,1,-4,7,-3,10,9,-6), (5,-6,-3,4,-2,-8,-7,2,7,4,2,0,-4,-8,7,5,-5,-2,-9))

if __name__ == '__main__':
    main()
