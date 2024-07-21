from logistic import LogisticMap
from utils.plotting import saveInteractivePlot
import datetime

def main():
    # Parameters for logistic map
    rhoMin = 3.57
    rhoMax = 4.0
    stepSize = 1e-4
    numTransient = 300
    numPlotPoints = 300
    numIterationsLyapunov = 200
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    logisticMap = LogisticMap(rhoMin, rhoMax, stepSize, numTransient, numPlotPoints, numIterationsLyapunov)

    rhoValues, xValues, hoverText = logisticMap.generateBifurcationData()

    saveInteractivePlot(rhoValues, xValues, hoverText, 'Logistic Map Bifurcation Diagram',
                        'Bifurcation Parameter (rho)', 'System States x(n)',
                        f'logisticMap_bifurcation_{timestamp}.html', markerSize = 0.05, opacity = 0.6)

    rhoValuesLyapunov, lyapunovExponents, lyapunovHoverText = logisticMap.generateLyapunovData()

    saveInteractivePlot(rhoValuesLyapunov, lyapunovExponents, lyapunovHoverText, 'Logistic Map Lyapunov Exponent',
                        'Bifurcation Parameter (rho)', 'Lyapunov Exponent',
                        f'logisticMap_lyapunov_exponent_{timestamp}.html', mode='lines')


if __name__ == "__main__":
    main()
