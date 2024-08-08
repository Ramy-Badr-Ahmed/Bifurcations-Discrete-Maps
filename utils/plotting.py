import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo
from typing import List

def saveInteractivePlot(xValues: np.ndarray, yValues: np.ndarray, hoverText: List[str],
                        title: str, xAxisTitle: str, yAxisTitle: str, fileName: str,
                        markerSize: float = 0.7, opacity: float = 0.7, mode: str = 'markers') -> None:
    """
    Saves an interactive scatter plot using Plotly.
    Args:
        xValues (ndarray): The x-coordinates of the data points.
        yValues (ndarray): The y-coordinates of the data points.
        hoverText (List[str]): The text to display when hovering over points.
        title (str): The title of the plot.
        xAxisTitle (str): The title of the x-axis.
        yAxisTitle (str): The title of the y-axis.
        fileName (str): The name of the file to save the plot as.
        markerSize (float, optional): The size of the markers. Defaults to 0.7.
        opacity (float, optional): The opacity of the markers. Defaults to 0.7.
        mode (str, optional): The mode of the plot (e.g., 'markers', 'lines'). Defaults to 'markers'.
    Returns:
        None
    """
    trace = go.Scattergl(
        x = xValues,
        y = yValues,
        mode = mode,
        marker = dict(
            color = '#027148',
            size = markerSize,
        ) if mode == 'markers' else dict(color = '#027148'),
        opacity = opacity if mode == 'markers' else 1.0,
        hoverinfo = 'text',
        hovertext = hoverText
    )

    layout = go.Layout(
        title = title,
        xaxis = dict(title = xAxisTitle, titlefont = dict(size = 16), tickfont = dict(size = 14)),
        yaxis = dict(title = yAxisTitle, titlefont = dict(size = 16), tickfont = dict(size = 14)),
        autosize = True,
        margin = dict(l = 50, r = 50, t = 50, b = 50),
        hovermode = 'closest'
    )

    fig = go.Figure(data = [trace], layout = layout)

    pyo.plot(fig, filename = fileName, auto_open = True)
