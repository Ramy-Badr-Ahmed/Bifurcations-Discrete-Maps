from tent_map import TentMap
from utils.plotting import saveInteractivePlot
import datetime

def main():
    # Parameters for tent map
    muMin = 1.01
    muMax = 2.0
    stepSize = 1e-4
    numTransient = 50
    numPlotPoints = 300
    numIterationsLyapunov = 200
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    tentMap = TentMap(muMin, muMax, stepSize, numTransient, numPlotPoints, numIterationsLyapunov)

    muValues, xValues, hoverText = tentMap.generateBifurcationData()

    saveInteractivePlot(muValues, xValues, hoverText, 'Tent Map Bifurcation Diagram',
                        'Bifurcation Parameter (mu)', 'System States x(n)',
                        f'tentMap_bifurcation_{timestamp}.html', markerSize = 1.2, opacity = 0.1)

    muValuesLyapunov, lyapunovExponents, lyapunovHoverText = tentMap.generateLyapunovData()

    saveInteractivePlot(muValuesLyapunov, lyapunovExponents, lyapunovHoverText, 'Tent Map Lyapunov Exponent',
                        'Bifurcation Parameter (mu)', 'Lyapunov Exponent',
                        f'tentMap_lyapunov_exponent_{timestamp}.html', mode='lines')

if __name__ == "__main__":
    main()
