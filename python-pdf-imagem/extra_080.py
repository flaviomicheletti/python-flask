"""
Exemplo do módulo Pygal para gerar gráficos com configurações pré-definidas.

Instale os módulos abaixo para o Pygal gerar arquivos no formato PNG

    pip install lxml
    pip install cairosvg
    pip install tinycss
    pip install cssselect

Após a instalação importe o módulo pygal, instâncie o objeto gráfico e adicione os dados para gerar o gráfico.

http://www.pygal.org/en/latest/documentation/first_steps.html
"""
import pygal

#
# Objeto que gera gráfico de barras
#
bar_chart = pygal.Bar()

#
# Dados(nome, [valores])
#
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

#
# Salva o arquivo
#
bar_chart.render_to_png('imgs/extra-080.png')