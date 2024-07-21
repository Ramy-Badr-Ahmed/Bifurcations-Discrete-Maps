![Python](https://img.shields.io/badge/Python-3670A0?style=plastic&logo=python&logoColor=ffdd54)

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

```shell
python Maps/LogisticMap/main.py

python Maps/TentMap/main.py

python Maps/SineMap/main.py
```
