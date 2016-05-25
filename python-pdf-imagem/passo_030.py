from reportlab.platypus import SimpleDocTemplate, Spacer

"""
SimpleDocTemplate.build()

`SimpleDocTemplate.build()` aceita os seguintes parâmetros:

story:        List (flowables) dos elementos do documento
onFirstPage:  Adiciona no documento o conteúdo da função na primeira página
onLaterPages: Adiciona no documento o conteúdo da função nas demais páginas
canvasmaker:  Adiciona no documento um novo objeto canvas em todas as páginas (veja no exemplo passo_032)

As funções de callback (onFirstPage, onLaterPages) recebem como parâmetro `canvas` e `doc` da classe 
`SimpleDocTemplate()`, isso permite a utilização do objeto canvas para desenhar os elementos.
"""

#
# Desenha o conteúdo da primeira página
#
def primeira_pagina(canvas, doc):
    canvas.drawString(100, 700, "Primeira página")
    
#
# Desenha o conteúdo da segunda página
#
def demais_paginas(canvas, doc):
    canvas.drawString(100, 700, "Demais páginas: %s" % (doc.page))

doc = SimpleDocTemplate("pdfs/passo-030.pdf")
story  = []

for i in range(10):
    story.append(Spacer(1, 100))

doc.build(story, onFirstPage=primeira_pagina, onLaterPages=demais_paginas)