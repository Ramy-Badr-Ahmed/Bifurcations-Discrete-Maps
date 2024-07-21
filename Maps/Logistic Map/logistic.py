from Maps.baseMap import BaseMap

class LogisticMap(BaseMap):
    def mapFunction(self, rho, x):
        return rho * x * (1 - x)

    def lyapunovExponentFormula(self, rho, x):
        return rho - 2 * rho * x
