from reportlab.platypus import SimpleDocTemplate, Image

"""

Inserindo imagem

`Image()` aceita os seguintes parâmetros:

    width
    height
    kind
    mask
    lazy
    hAlign
"""

doc = SimpleDocTemplate("pdfs/passo-020.pdf")
story  = []

#
# Alinhado a esquerda
#
story.append(Image('static/python-logo.png', hAlign="LEFT"))



#
# Por padrão a imagem é inserida ao centro
# 
story.append(Image('static/python-logo.png'))



#
# Alinhado a direita
#
story.append(Image('static/python-logo.png', hAlign="RIGHT"))


#
# Alterando o tamanho da imagem (nome, width, height)
#
story.append(Image('static/python-logo.png', 200, 200))

doc.build(story)