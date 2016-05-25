from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

"""
Canvas saveState e restoreState

saveState():    salva os estilos das fontes, linhas e estados dos gráficos.
restoreState(): restaura o último estado dos estilos das fontes, linhas e estados dos gráficos.

Veja mais na página 16 https://www.reportlab.com/docs/reportlab-userguide.pdf

"""

canvas = canvas.Canvas("pdfs/exemplo-030.pdf")

canvas.setLineWidth(4)
canvas.line(60, 800, 100, 600)

canvas.setFont('Helvetica', 30)
canvas.drawString(60, 500, 'Estilo da fonte: Helvetica')

#
# Salva todos os estilos configurados
#
canvas.saveState()

#
# Alterando os estilos
#
canvas.setLineWidth(15)
canvas.line(60, 800, 200, 600)

canvas.setFillColor(HexColor('#e6e910'))
canvas.setFont('Courier', 14)
canvas.drawString(60, 460, 'Alterando a cor do texto...')

#
# Restaurando todos os estilos que foram salvos
#
canvas.restoreState()

canvas.line(60, 800, 300, 600)
canvas.drawString(60, 420, 'Estilo da fonte: Helvetica')

canvas.save()