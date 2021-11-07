from OrdinaryCalc import OrdinaryCalc


class AdvancedCalc (OrdinaryCalc):

    def TransformToKBite(self):
        self.KBite = self.num1 * 0.0009765625
        return self.KBite


    def getKBite (self):
        return self.KBite

