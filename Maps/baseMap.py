import numpy as np
from typing import List, Tuple, Any
from numpy import ndarray, dtype, floating


class BaseMap:
    def __init__(self, paramMin: float, paramMax: float, stepSize: float,
                 numTransient: int, numPlotPoints: int, numIterationsLyapunov: int):
        """
        Base class for creating bifurcation maps and calculating Lyapunov exponents.

        This base class provides a generic generation of bifurcation data and calculating
        Lyapunov exponents for various dynamical systems. It is intended to be subclassed
        to implement specific mapping functions and Lyapunov exponent calculations.

        Attributes:
            paramMin (float): Minimum parameter value for the mapping.
            paramMax (float): Maximum parameter value for the mapping.
            stepSize (float): Step size for parameter increments.
            numTransient (int): Number of transient iterations before data collection.
            numPlotPoints (int): Number of points to plot for each parameter value.
            numIterationsLyapunov (int): Number of iterations for calculating the Lyapunov exponent.
        """
        self.paramMin = paramMin
        self.paramMax = paramMax
        self.stepSize = stepSize
        self.numTransient = numTransient
        self.numPlotPoints = numPlotPoints
        self.numIterationsLyapunov = numIterationsLyapunov

    def mapFunction(self, param: float, x: float) -> float:
        """
        Abstract method to be implemented by subclasses. Calculates the next state in the mapping for a given parameter.
        Args:
            param (float): The parameter value for the mapping.
            x (float): The current state in the map.
        Raises:
            NotImplementedError: If not implemented in the subclass.
        """
        raise NotImplementedError("Individual subclass map should implement this method.")

    def lyapunovExponentFormula(self, param: float, x: float) -> float:
        """
        Abstract method to be implemented by subclasses. Provides the formula for calculating the Lyapunov exponent for a given mapping.
        Args:
            param (float): The parameter value for the mapping.
            x (float): The current state in the map.
        Raises:
            NotImplementedError: If not implemented in the subclass.
        """
        raise NotImplementedError("Individual subclass map should implement this method.")

    def calculateLyapunovExponent(self, param: float) -> float:
        """
        Calculates the Lyapunov exponent for a given bifurcation parameter. Iterates the map function and accumulates the logarithm of the
        derivative to compute the Lyapunov exponent. Handles numerical errors and resets the value of system state x if invalid results are encountered.
        Args:
            param (float): The parameter value for which to calculate the Lyapunov exponent.
        Returns:
            float: The calculated Lyapunov exponent, or NaN if an error occurs.
        """
        x = np.random.rand()
        lyapunovExponent = 0

        with np.errstate(over = 'raise', under = 'raise', invalid = 'raise'):
            for _ in range(self.numIterationsLyapunov):
                try:
                    x = self.mapFunction(param, x)
                    if np.isinf(x) or np.isnan(x):
                        raise ValueError(f"Invalid x value detected: {x}")

                    lyapunovExponent += np.log(abs(self.lyapunovExponentFormula(param, x)))

                except (FloatingPointError, ValueError) as e:
                    print(f"Error during Lyapunov exponent calculation at param = {param}: {e}")
                    x = np.random.rand()     # resetting x to a valid value
                    lyapunovExponent = np.nan
                    break

        return lyapunovExponent / self.numIterationsLyapunov \
            if not np.isnan(lyapunovExponent) \
            else np.nan

    def generateBifurcationData(self) -> Tuple[np.ndarray, np.ndarray, List[str]]:
        """
        Generates bifurcation data for the configured parameter range. Iterates over bifurcation parameter values,
        performs transient iterations, and collects x-values for plotting.
        Returns:
            tuple: A tuple containing:
            - bifurcationParam (ndarray): The parameter values used for the bifurcation diagram.
            - bifurcationX (ndarray): The corresponding x-values for the bifurcation diagram.
            - hoverText (list of str): Text for displaying parameter and x-values in visualisations.
        """
        paramValues = np.linspace(self.paramMin, self.paramMax, num = int((self.paramMax - self.paramMin) / self.stepSize) + 1)
        bifurcationX = []
        bifurcationParam = []
        hoverText = []
        x = np.zeros(self.numPlotPoints)
        x[0] = np.random.rand()

        for param in paramValues:
            # Transient phase
            for _ in range(self.numTransient):
                x[0] = self.mapFunction(param, x[0])
                if np.isinf(x[0]) or np.isnan(x[0]):        # Check for validity
                    print(f'Overflow/NaN detected during transient phase at param = {param}, x = {x[0]}')
                    x[0] = np.random.rand()  # Reset x to a valid value

            # Collect data
            for n in range(1, self.numPlotPoints):
                x[n] = self.mapFunction(param, x[n - 1])
                if np.isinf(x[n]) or np.isnan(x[n]):        # Check for validity
                    print(f'Overflow/NaN detected during data collection at param = {param}, x = {x[n]}')
                    x[n] = np.random.rand()  # Reset x to a valid value

            hoverText.extend([f'param = {param:.3f}<br>x = {xi:.3f}' for xi in x])
            bifurcationX.extend(x)
            bifurcationParam.extend([param] * self.numPlotPoints)

        return np.array(bifurcationParam), np.array(bifurcationX), hoverText
        #return bifurcationParam, bifurcationX, hoverText

    def generateLyapunovData(self)-> Tuple[np.ndarray, np.ndarray, List[str]]:
        """
        Generates Lyapunov exponent data for the configured parameter range. Calculates the Lyapunov exponent for each parameter value and
        prepares data for visualisation.

        Returns:
            tuple: A tuple containing:
                - paramValues (ndarray): The parameter values used for Lyapunov exponent calculation.
                - lyapunovExponents (ndarray): The corresponding Lyapunov exponents.
                - hoverText (list of str): Text for displaying parameter and Lyapunov exponent values in visualisations.
        """
        paramValues = np.linspace(self.paramMin, self.paramMax, num = int((self.paramMax - self.paramMin) / self.stepSize) + 1)
        lyapunovExponents = [self.calculateLyapunovExponent(param) for param in paramValues]

        hoverText = [f'param = {param:.3f}<br>Lyapunov Exponent = {le:.3f}' for param, le in zip(paramValues, lyapunovExponents)]
        return np.array(paramValues), np.array(lyapunovExponents), hoverText
