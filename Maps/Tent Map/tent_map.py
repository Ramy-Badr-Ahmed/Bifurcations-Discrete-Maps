from Maps.baseMap import BaseMap
import numpy as np

class TentMap(BaseMap):
    def mapFunction(self, mu, x):
        return mu * x \
            if x < 0.5 \
            else mu * (1 - x)

    def lyapunovExponentFormula(self, mu, x):
        return np.where(x < 0.5, mu, -mu)
