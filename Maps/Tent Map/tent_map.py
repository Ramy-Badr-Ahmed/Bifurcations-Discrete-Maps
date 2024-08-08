from typing import Any

from numpy import ndarray, dtype

from Maps.baseMap import BaseMap
import numpy as np

class TentMap(BaseMap):
    def mapFunction(self, mu: float, x: float) -> float:
        """
        Calculates the next state of the Tent map for a given bifurcation parameter and current state.
        Args:
            mu (float): The bifurcation parameter for the Tent map.
            x (float): The current state in the map.
        Returns:
            float: The next state of the map.
        """
        return mu * x \
            if x < 0.5 \
            else mu * (1 - x)

    def lyapunovExponentFormula(self, mu: float, x: float) -> ndarray[Any, dtype[Any]]:
        """
        The Lyapunov exponent formula for the Tent map.
        Args:
            mu (float): The bifurcation parameter for the Tent map.
            x (float): The current state in the map.
        Returns:
            float: The derivative of the mapping function with respect to x.
        """
        return np.where(x < 0.5, mu, -mu)
