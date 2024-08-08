![Python](https://img.shields.io/badge/Python-3670A0?style=plastic&logo=python&logoColor=ffdd54)  

![GitHub](https://img.shields.io/github/license/Ramy-Badr-Ahmed/Bifurcations)

# Bifurcation Diagrams for Discrete-Time Maps

This repository provides Python implementations for generating interactive bifurcation diagrams and analysing chaotic behavior in discrete-time dynamical systems. 

The following maps are currently included:

- Logistic Map
- Tent Map
- Sine Map

### Overview

Each map is implemented to analyse its bifurcation diagram and Lyapunov exponent, which are key to understanding the dynamics and chaos within these systems.

### Installation

1) Create and source virtual environment:
```shell
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
2) Install the dependencies:
```shell
pip install -r requirements.txt
```

### Example Usage

To analyse a specific map, run the corresponding script in the Maps directory. You can tweak the map parameters as needed.

Interactive plots will be generated and saved as offline HTML files within each map's directory.

>[!Note]
> Some plots have been uploaded to the `Maps` directories for reference.

##### Scripts
```shell
python Maps/LogisticMap/main.py

python Maps/TentMap/main.py

python Maps/SineMap/main.py
```
##### Example:
```python
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
```
