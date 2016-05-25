from reportlab.platypus import SimpleDocTemplate, Table

"""

Tabelas

"""

doc = SimpleDocTemplate("pdfs/extra-060.pdf")
story = []

#
# Criamos uma list com os dados de cada célula
#
dados = [
    ['00', '01', '02'], # Primeira linha
    ['10', '11', '12']  # Segunda linha
]

#
# Table(data, colWidths=None, rowHeights=None, style=None, splitByRow=1, repeatRows=0, repeatCols=0)
#
tabela = Table(dados, 50, 50)
story.append(tabela)
doc.build(story)