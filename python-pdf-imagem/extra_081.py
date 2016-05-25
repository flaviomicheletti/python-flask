"""

Exemplo de customização da configuração do gráfico de barras com Pygal

"""
import pygal

line_chart = pygal.HorizontalBar(show_legend=False)
line_chart.x_labels = 'IE', 'Firefox', 'Chrome', 'Safari', 'Opera'
line_chart.y_labels = y_labels = [
  {'label': 'One', 'value': 1},
  {'label': 'Three', 'value': 2},
  {'label': 'Four', 'value': 3},
  {'label': 'Four and a half', 'value': 4},
  {'label': 'Five', 'value': 5}]
line_chart.add('Cargo', [2, 1, 3, 2, 5])
line_chart.render_to_png('imgs/extra-081.png')