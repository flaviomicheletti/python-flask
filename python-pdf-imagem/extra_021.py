from reportlab.pdfgen import canvas
from reportlab.rl_config import defaultPageSize

"""

Centralizando elemento

"""

canvas = canvas.Canvas("pdfs/extra-021.pdf")

# Obs:
# defaultPageSize[0] é igual a largura padrão de uma folha A4
# defaultPageSize[1] é igual a altura padrão de uma folha A4

canvas.rect(defaultPageSize[0] / 2 - 50, defaultPageSize[1] / 2 - 50, 100, 100, fill=1)



#
# Sugestão para código legível
#
rec = {}
rec['width']  = 100
rec['height'] = 100
rec['x']      = defaultPageSize[0] / 2 - rec['width']  / 2
rec['y']      = defaultPageSize[1] / 2 - rec['height'] / 2

canvas.rect(rec['x'], rec['y'], rec['width'], rec['height'], fill=1)

canvas.save()