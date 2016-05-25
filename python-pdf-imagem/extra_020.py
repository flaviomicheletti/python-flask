from reportlab.pdfgen import canvas

"""
Desenhando elementos

Alguns exemplos de como desenhar outros elementos além de textos.
https://www.reportlab.com/docs/reportlab-userguide.pdf
"""

canvas = canvas.Canvas("pdfs/extra-020.pdf")

#
# Linhas
#

# Parâmetros (x, y, x1, y1)
canvas.line(50, 700, 50, 750)  # linha vertical
canvas.line(50, 600, 100, 600) # linha horizontal
canvas.line(50, 650, 100, 750) # linha vertical

# Definindo a expessura da linha
canvas.setLineWidth(4)
canvas.line(50, 590, 100, 590)



#
# Retângulos
#

# Parâmetros (x, y, width, height)
canvas.rect(350, 700, 50, 100, fill=1) # Preenchendo o desenho

canvas.setLineWidth(2)
canvas.rect(450, 700, 100, 50, fill=0) # Apenas o contorno do desenho



#
# Circulos
#

# Parâmetros (x, y, radius)
canvas.circle(100, 500, 50, stroke=1, fill=0) # Com contorno e sem preenchimento
canvas.circle(300, 500, 80, stroke=0, fill=1) # Sem contorno e com preenchimento



#
# Colorindo elementos
#

# Parâmetros (R, G, B)
canvas.setFillColorRGB(255, 0, 0)
canvas.rect(60, 300, 50, 100, stroke=0, fill=1)

# Somente uma escala para tons de cinza (0 - 1)
canvas.setFillGray(0.9)
canvas.rect(180, 300, 50, 100, stroke=0, fill=1)

# Alterando a cor da borda
canvas.setStrokeColorRGB(0, 0, 255) 
canvas.rect(300, 300, 50, 100, stroke=1, fill=1)



#
# Utilizando o HexCode
#
from reportlab.lib.colors import HexColor

canvas.setFillColor(HexColor('#ff8100'))
canvas.rect(420, 300, 50, 100, stroke=1, fill=1)

canvas.save()