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
##### Example (Logistic Map):
```python
from logistic import LogisticMap
from utils.plotting import saveInteractivePlot
import datetime

# Parameters for logistic map
params = {
    'paramMin': 3.57,  # bifurcation parameter
    'paramMax': 4.0,   
    'stepSize': 1e-3,
    'numTransient': 300,
    'numPlotPoints': 300,
    'numIterationsLyapunov': 200
}

logisticMap = LogisticMap(**params)

# Generate and save bifurcation diagram
rhoValues, xValues, hoverText = logisticMap.generateBifurcationData()

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

plotParams = {
    'title': 'Logistic Map Bifurcation Diagram',
    'xAxisTitle': 'Bifurcation Parameter (rho)',
    'yAxisTitle': 'System States x(n)',
    'fileName': f'logisticMap_bifurcation_{timestamp}.html',
    'markerSize': 0.05,
    'opacity': 0.6,
}

saveInteractivePlot(rhoValues, xValues, hoverText, **plotParams)

# Generate and save Lyapunov exponent plot
rhoValuesLyapunov, lyapunovExponents, lyapunovHoverText = logisticMap.generateLyapunovData()

plotParams = {
    'title': 'Logistic Map Lyapunov Exponent',
    'xAxisTitle': 'Bifurcation Parameter (rho)',
    'yAxisTitle': 'Lyapunov Exponent',
    'fileName': f'logisticMap_lyapunov_exponent_{timestamp}.html',
    'mode': 'lines'
}

saveInteractivePlot(rhoValuesLyapunov, lyapunovExponents, lyapunovHoverText, **plotParams)
```
