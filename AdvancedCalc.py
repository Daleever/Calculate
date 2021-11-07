from OrdinaryCalc import OrdinaryCalc


class AdvancedCalc (OrdinaryCalc):

    def TransformToKBite(self, Bite):
        self.KBite = Bite * 0.0009765625


    def getKBite (self):
        return self.KBite

