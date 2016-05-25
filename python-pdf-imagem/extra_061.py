from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

"""
Table border

Propriedades:
    GRID                    - Todas as bordas
    BOX                     - bordas externas
    INNERGRID               - bordas internas
    OUTLINE                 - equivalente ao BOX
    LINEBELOW               - borda de baixo
    LINEABOVE               - borda de cima
    LINEBEFORE              - borda lateral esquerda
    LINEAFTER               - borda lateral direita
"""

doc = SimpleDocTemplate("pdfs/extra-061.pdf")
story = []
dados = [
    ['10', '11', '12'], # Primeira linha
    ['20', '21', '22'], # Segunda linha
    ['30', '31', '32']  # Terceira linha
]



# Todas as bordas: com valores positivos
#
# É preciso adicionar o valor da posição da última célula na segunda tuple
tabela_bordas = Table(dados, 50, 50)
tabela_bordas.setStyle(TableStyle([
                #       (ci, li),(cf, lf), expessura, cor              # Células afetadas
		('GRID', (0, 0), (2, 2), 0.25, HexColor('#000000')),   # Todas
                ]))
story.append(tabela_bordas)
story.append(Spacer(1, 10))



# Todas as bordas: com valores negativos
#
# É possível adicionar nas tuples das propriedades valores negativos e obter o mesmo efeito.
# Abaixo também demonstra como adicionar bordas externas e internas separadas
tabela_bordas2 = Table(dados, 50, 50)
tabela_bordas2.setStyle(TableStyle([
                #      (ci, li),(cf, lf), expessura, cor                    # Células afetadas
		('BOX', (0, 0), (-1, -1), 2, HexColor('#000000')),          # Todas
		('INNERGRID', (0, 0), (-1, -1), 0.25, HexColor('#000000')), # Todas
                ]))
story.append(tabela_bordas2)

doc.build(story)