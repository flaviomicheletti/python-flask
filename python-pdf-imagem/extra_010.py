from reportlab.pdfgen import canvas

"""

Canvas texto

"""

canvas = canvas.Canvas("pdfs/extra-010.pdf")


#
# Alinhamento do texto
#

# A função drawString() desenha o texto com o ponto inicial a esquerda
canvas.drawString(100, 700, "primeiro")

# A função drawCentredString() desenha o texto com o ponto inicial no xentro
canvas.drawCentredString(100, 650, "segundo")

# A função drawRightString() desenha o texto com o ponto inicial no xentro
canvas.drawRightString(100, 600, "terceiro")



#
# Alterando a fonte do texto
# 
# O tipo e o tamanho da fonte pode ser alterado com a função setFont().
# Abaixo temos uma lista das fontes disponíveis:
# 
#     Courier, Courier-Bold, Courier-Oblique e Courier-BoldOblique;
#     Helvetica, Helvetica-Bold, Helvetica-Oblique e Helvetica-BoldOblique;
#     Times-Roman, Times-Bold, Times-Italic e Times-BoldItalic;
#     Symbol e ZapfDingbats.

canvas.setFont('Helvetica', 12)
canvas.drawString(100, 550, 'Estilo da fonte: Helvetica')

canvas.setFont('Courier', 16)
canvas.drawString(100, 500, 'Estilo da fonte: Courier')



#
# É possível instalar uma nova fonte com a função `registerFont()`
# http://stackoverflow.com/questions/4899885/how-to-set-any-font-in-reportlab-canvas-in-python
#
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial','static/arial.ttf'))
canvas.setFont('Arial', 20)
canvas.drawString(100, 450, "Estilo da fonte: Arial")



#
# Alterando a cor do texto
#
from reportlab.lib.colors import HexColor

canvas.setFillColor(HexColor('#e6e910'))
canvas.drawString(100, 400, 'Alterando a cor do texto...')


canvas.save()