import plotly.graph_objs as go
import plotly.offline as pyo

def saveInteractivePlot(xValues, yValues, hoverText, title, xAxisTitle, yAxisTitle, fileName, markerSize = 0.7, opacity = 0.7, mode = 'markers'):
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
