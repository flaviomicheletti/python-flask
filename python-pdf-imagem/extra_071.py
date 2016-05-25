from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.lib import colors

doc = SimpleDocTemplate("pdfs/extra-071.pdf")
story  = []

"""

Exemplo do gerador de gráficos automático do reportlab

"""

drawing = Drawing(400, 200)
data = [
        (1, 2, 3, 3, 5, 4, 2, 3)
        ]
bc = HorizontalBarChart()
bc.x = 50
bc.y = 50
bc.height = 125
bc.width = 150
bc.data = data
bc.strokeColor = colors.black
bc.valueAxis.valueMin = 0
bc.valueAxis.valueMax = 5
bc.valueAxis.valueStep = 1
bc.categoryAxis.labels.boxAnchor = 'ne'
bc.categoryAxis.labels.dx = -5
bc.categoryAxis.labels.dy = 8
bc.categoryAxis.labels.angle = 0
bc.categoryAxis.categoryNames = ['Liderança','Comunicação','Empreendedorismo',
       'Detalhe','Decisão racional','Cumprimento à normas','Criatividade','Energia']
drawing.add(bc)


story.append(drawing)
doc.build(story)