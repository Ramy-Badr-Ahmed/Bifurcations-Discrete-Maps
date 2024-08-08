from Maps.baseMap import BaseMap

class LogisticMap(BaseMap):
    def mapFunction(self, rho: float, x: float) -> float:
        """
        Calculates the next state of the Logistic map for a given bifurcation parameter and current state.
        Args:
            rho (float): The bifurcation parameter for the Logistic map.
            x (float): The current state in the map.
        Returns:
            float: The next state of the map.
        """
        return rho * x * (1 - x)

    def lyapunovExponentFormula(self, rho: float, x: float) -> float:
        """
        The Lyapunov exponent formula for the Logistic map.
        Args:
            rho (float): The bifurcation parameter for the Logistic map.
            x (float): The current state in the map.
        Returns:
            float: The derivative of the mapping function with respect to x.
        """
        return rho - 2 * rho * x
