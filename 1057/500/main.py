class ABBA(object):
    def __init__(self):
        object.__init__(self)

    def getCanObtainByRecursion(self, initial, target):
        if initial not in target or initial[::-1] not in target:
            return False
        if initial == target:
            return True
        return self.getCanObtainByRecursion(initial+'A', target) or self.getCanObtainByRecursion(initial[::-1]+'B', target)

    def canObtain(self, initial, target):
        return 'Possible' if self.getCanObtainByRecursion(initial, target) else 'Impossible'
