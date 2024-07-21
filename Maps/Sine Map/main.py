from sine_map import SineMap
from utils.plotting import saveInteractivePlot
import datetime

def main():
    # Parameters for Sine map
    alphaMin = 0.7
    alphaMax = 3.0
    stepSize = 1e-4  # 1e-3
    numTransient = 100
    numPlotPoints = 500
    numIterationsLyapunov = 200
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    sineMap = SineMap(alphaMin, alphaMax, stepSize, numTransient, numPlotPoints, numIterationsLyapunov)

    alphaValues, xValues, hoverText = sineMap.generateBifurcationData()

    saveInteractivePlot(alphaValues, xValues, hoverText, 'Sine Map Bifurcation Diagram',
                        'Bifurcation Parameter (alpha)', 'System States x(n)',
                        f'sineMap_bifurcation_{timestamp}.html', opacity = 0.1)

    alphaValuesLyapunov, lyapunovExponents, lyapunovHoverText = sineMap.generateLyapunovData()

    saveInteractivePlot(alphaValuesLyapunov, lyapunovExponents, lyapunovHoverText, 'Sine Map Lyapunov Exponent',
                        'Bifurcation Parameter (alpha)', 'Lyapunov Exponent',
                        f'sineMap_lyapunov_exponent_{timestamp}.html', mode='lines')

if __name__ == "__main__":
    main()
