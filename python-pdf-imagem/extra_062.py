from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

"""

Estilizando Tabelas

Propriedades:

    FONT                    - takes fontname, optional fontsize and optional leading.
    FONTNAME (or FACE)      - takes fontname.
    FONTSIZE (or SIZE)      - takes fontsize in points; leading may get out of sync.
    LEADING                 - takes leading in points.
    TEXTCOLOR               - takes a color name or (R,G,B) tuple.
    ALIGNMENT (or ALIGN)    - takes one of LEFT, RIGHT and CENTRE (or CENTER) or DECIMAL.
    LEFTPADDING             - takes an integer, defaults to 6.
    RIGHTPADDING            - takes an integer, defaults to 6.
    BOTTOMPADDING           - takes an integer, defaults to 3.
    TOPPADDING              - takes an integer, defaults to 3.
    BACKGROUND              - takes a color.
    ROWBACKGROUNDS          - takes a list of colors to be used cyclically.
    COLBACKGROUNDS          - takes a list of colors to be used cyclically.
    VALIGN                  - takes one of TOP, MIDDLE or the default BOTTOM
"""

doc = SimpleDocTemplate("pdfs/extra-62.pdf")
story = []
dados = [
    ['CENTER', 'DECIMAL', 'RIGHT'], # Primeira linha
    ['LEFT', 'TEXTCOLOR', 'BACKGROUND'], # Segunda linha
    ['VALIGN', 'VALIGN', 'FONTSIZE']  # Terceira linha
]

tabela = Table(dados, 100, 100)

tabela.setStyle(TableStyle([
                #        (ci, li),(cf, lf), alinhamento
                ('ALIGN', (0, 0), (0, 0), 'CENTER'),
                ('ALIGN', (1, 0), (1, 0), 'DECIMAL'),
                ('ALIGN', (2, 0), (2, 0), 'RIGHT'),

                ('ALIGN', (0, 1), (0, 1), 'LEFT'),
                #            (ci, li),(cf, lf), cor
                ('TEXTCOLOR', (1, 1), (1, 1), HexColor('#ff0000')),
                ('BACKGROUND', (2, 1), (2, 1), HexColor('#ffff00')),

                #         (ci, li),(cf, lf), alinhamento vertical
                ('VALIGN', (0, 2), (0, 2), 'TOP'),
                ('VALIGN', (1, 2), (1, 2), 'MIDDLE'),

                #           (ci, li),(cf, lf), tamanho da fonte
                ('FONTSIZE', (2, 2), (2, 2), 16),

		('INNERGRID', (0, 0), (-1, -1), 0.25, HexColor('#000000')),
		('BOX', (0, 0), (-1, -1), 0.25, HexColor('#000000')),
                ]))

story.append(tabela)
doc.build(story)