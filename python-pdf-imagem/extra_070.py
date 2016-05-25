from reportlab.platypus import SimpleDocTemplate
from reportlab.graphics.shapes import *
from reportlab.lib import colors

doc = SimpleDocTemplate("pdfs/extra-070.pdf")
story  = []

"""

Exemplo da ferramenta de desenho do reportlab

"""

drawing = Drawing(200, 200)
drawing.add(Rect(0, 0, 100, 100, fillColor=colors.yellow))

drawing.add(String(0, 0, 'Ponto (0, 0, start)', fontSize=18, textAnchor="start"))
drawing.add(String(100, 100, 'Ponto (100, 100, middle)', fontSize=18, fillColor=colors.red, textAnchor="middle"))
drawing.add(String(150, 150, 'Ponto (150, 150, end)', fontSize=18, fillColor=colors.blue, textAnchor="end"))
drawing.add(String(200, 200, 'Ponto (200, 200, numeric)', fontSize=18, fillColor=colors.green, textAnchor="numeric"))

drawing.add(Line(0, 200, 200, 200, strokeColor=colors.red))

drawing.add(Line(200, 200, 200, 0, strokeColor=colors.blue))

story.append(drawing)
doc.build(story)