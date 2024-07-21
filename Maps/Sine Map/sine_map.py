from Maps.baseMap import BaseMap
import numpy as np

class SineMap(BaseMap):
    def mapFunction(self, alpha, x):
        return alpha * np.sin(np.pi * x)

    def lyapunovExponentFormula(self, alpha, x):
        return alpha * np.pi * np.cos(np.pi * x)
