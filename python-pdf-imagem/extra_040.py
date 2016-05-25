from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import Paragraph

"""
Adicionando elementos do módulo platypus no canvas

platypus = Page Layout and Typography Using Scripts
Capítulo 5 do manual.

It is a high level page layout library which
lets you programmatically create complex documents with a minimum of effort
"""

canvas = canvas.Canvas("pdfs/exemplo-040.pdf")
styles = getSampleStyleSheet()
width, height = LETTER

paragrafo1 = Paragraph("Primeiro parágrafo!", styles["Normal"])
paragrafo1.wrapOn(canvas, width, height)   # Configuração da página para o elemento Paragraph
paragrafo1.drawOn(canvas, 100, 700)        # Desenha o elemento Paragraph no documento

paragrafo2 = Paragraph("Segundo parágrafo!", styles["Normal"])
paragrafo2.wrapOn(canvas, width, height)
paragrafo2.drawOn(canvas, 100, 600)

canvas.save()
