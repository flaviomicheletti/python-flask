from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import letter

"""

SimpleDocTemplate ()

O `SimpleDocTemplate` auxilia na produção do documento pdf com configurações pré-estabelecidas.
Todos os elementos adicionados na list story são desenhados pela classe `Canvas()` do ReportLab.

`SimpleDocTemplate()` aceita como parâmetros:

    pagesize
    pageTemplates
    showBoundary
    leftMargin
    rightMargin
    topMargin
    bottomMargin
    allowSplitting
    title
    author
    subject
    creator
    keywords
    invariant
    pageCompression
    _pageBreakQuick
    rotation
    _debug
    encrypt
    cropMarks
    enforceColorSpace
    displayDocTitle
    lang
    initialFontName
    initialFontSize
    initialLeading
    cropBox
    artBox
    trimBox
    bleedBox
"""

#
# O exemplo abaixo gera um arquivo sem página alguma
#
doc = SimpleDocTemplate("pdfs/passo-001a.pdf")
story = []
doc.build(story)



#
# O exemplo abaixo gera um documento com uma página qualquer
#
doc = SimpleDocTemplate("pdfs/passo-001b.pdf")
story = []

# A função Spacer(width, height) adiciona um espaçamento entre as linhas.
# Segundo a documentação somente o parâmetro height é utilizado.
story.append(Spacer(1, 20))
doc.build(story)



# Na função construtora, além do nome do aquivo, podemos passar parâmetros de dimensões
# como margens e informações sobre o documento.
#
doc = SimpleDocTemplate("pdfs/passo-001c.pdf", pagesize=letter, rightMargin=10, leftMargin=10, topMargin=10, bottomMargin=10)
story  = []
story.append(Spacer(1, 20))
doc.build(story)