from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.rl_config import defaultPageSize

"""
canvas.saveState() & canvas.restoreState()

saveState():    salva os estilos das fontes, linhas e estados dos gráficos.
restoreState(): restaura o último estado dos estilos das fontes, linhas e estados dos gráficos.

Todas as alterações de estilo de string adicionadas no story não afetam o objeto canvas da função. 

Veja mais no exemplo `extra_050.py`

"""

#
# Desenha o conteúdo da primeira página
#
def primeira_pagina(canvas, doc):
    canvas.setFont('Times-Bold', 20)
    canvas.drawString(defaultPageSize[0] / 2, defaultPageSize[1] - 100, "Primeira página")
#
# Desenha o conteúdo da segunda página
#
def demais_paginas(canvas, doc):
    canvas.setFont('Times-Bold', 10)
    canvas.drawString(defaultPageSize[0] / 2, defaultPageSize[1] - 100, "Demais páginas: %s esquerda" % (doc.page))
    canvas.saveState()                  # Salva o estilo da font (Times-Bold, 30)
    canvas.setFont('Courier', 20)       # Seto o novo estilo da fonte ('Courier', 20)
    canvas.drawCentredString(defaultPageSize[0] / 2, defaultPageSize[1] - 150, "Demais páginas: %s centralizado" % (doc.page))
    canvas.restoreState()               # Restaura para o estilo de fonte que foi gravado (Times-Bold, 30)
    canvas.drawRightString(defaultPageSize[0] / 2, defaultPageSize[1] - 200, "Demais páginas: %s direita" % (doc.page))

doc = SimpleDocTemplate("pdfs/passo-031.pdf")
story  = []

for i in range(10):
    story.append(Spacer(1, 100))

doc.build(story, onFirstPage=primeira_pagina, onLaterPages=demais_paginas)