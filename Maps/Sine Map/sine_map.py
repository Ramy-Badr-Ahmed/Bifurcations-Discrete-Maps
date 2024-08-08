from Maps.baseMap import BaseMap
import numpy as np

class SineMap(BaseMap):
    def mapFunction(self, alpha: float, x: float) -> float:
        """
        Calculates the next state of the Sine map for a given bifurcation parameter and current state.
        Args:
            alpha (float): The bifurcation parameter for the Sine map.
            x (float): The current state in the map.
        Returns:
            float: The next state of the map.
        """
        return alpha * np.sin(np.pi * x)

    def lyapunovExponentFormula(self, alpha: float, x: float) -> float:
        """
        The Lyapunov exponent formula for the Sine map.
        Args:
            alpha (float): The bifurcation parameter for the Sine map.
            x (float): The current state in the map.
        Returns:
            float: The derivative of the mapping function with respect to x.
        """
        return alpha * np.pi * np.cos(np.pi * x)
