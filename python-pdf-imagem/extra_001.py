from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER, A6, B3

"""
The canvas should be thought of as a sheet of white paper with points on the sheet identified using Cartesian
(X,Y) coordinates which by default have the (0,0) origin point at the lower left corner of the page.
Furthermore the first coordinate x goes to the right and the second coordinate y goes up, by default

(http://www.reportlab.com/docs/reportlab-userguide.pdf, página 10)
"""

c = canvas.Canvas("pdfs/extra-001a.pdf")

# Os primeiros parâmetros são x e y como se fossem o plano cartesiano
c.drawString(20, 800, "Bem-vindo ao Reportlab!")

c.save()

"""
Dimensões da página

Por padrão o tamanho da página é definido como A4, mas pode ser alterado com parâmetro `pagesize`.
Abaixo está a lista com as dimensões suportadas:

    A6, A5, A4, A3, A2, A1 e A0;
    B6, B5, B4, B3, B2, B1 e B0;
    LETTER, LEGAL e ELEVENSEVENTEEN.
"""

#
# O exemplo abaixo gera um documento com as dimensões do papel carta
#
canvas_l = canvas.Canvas("pdfs/extra-001b", pagesize=LETTER)
canvas_l.drawString(60, 400, 'Tamanho: Letter')
canvas_l.save()



#
# O exemplo abaixo gera um documento com as dimensões do papel A6
#
canvas_A6 = canvas.Canvas("pdfs/extra-001c", pagesize=A6)
canvas_A6.drawString(60, 400, 'Tamanho: A6')
canvas_A6.save()



#
# O exemplo abaixo gera um documento com as dimensões do papel B3
#
canvas_B3 = canvas.Canvas("pdfs/extra-001d", pagesize=B3)
canvas_B3.drawString(60, 400, 'Tamanho: B3')
canvas_B3.save()