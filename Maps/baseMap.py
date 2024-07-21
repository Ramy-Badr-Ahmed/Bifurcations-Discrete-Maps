import numpy as np

class BaseMap:
    def __init__(self, paramMin, paramMax, stepSize, numTransient, numPlotPoints, numIterationsLyapunov):
        self.paramMin = paramMin
        self.paramMax = paramMax
        self.stepSize = stepSize
        self.numTransient = numTransient
        self.numPlotPoints = numPlotPoints
        self.numIterationsLyapunov = numIterationsLyapunov

    def mapFunction(self, param, x):
        raise NotImplementedError("Individual subclass map should implement this method.")

    def lyapunovExponentFormula(self, param, x):
        raise NotImplementedError("Individual subclass map should implement this method.")

    def calculateLyapunovExponent(self, param):
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

    def generateBifurcationData(self):
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

        return bifurcationParam, bifurcationX, hoverText

    def generateLyapunovData(self):
        paramValues = np.linspace(self.paramMin, self.paramMax, num = int((self.paramMax - self.paramMin) / self.stepSize) + 1)
        lyapunovExponents = [self.calculateLyapunovExponent(param) for param in paramValues]

        hoverText = [f'param = {param:.3f}<br>Lyapunov Exponent = {le:.3f}' for param, le in zip(paramValues, lyapunovExponents)]
        return paramValues, lyapunovExponents, hoverText
