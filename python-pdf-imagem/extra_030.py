from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, inch, mm, pica

"""
Unidades de medidas

Auxilia na definição das dimensões dos elementos e em seu posicionamento com valores pre-definidos. 
Por exemplo, podemos definir as margens de um documento em centimetros ao invés de pixel. 

inch = polegandas   (1 inch = 72px)
cm   = centimetros  (1 cm   = 28px)
pica = paicas       (1 pica = 12px)
mm   = milimitros   (1 mm   = 3px)

É possível alterar as medidas de cada atributo ao adicionar um calculo operacional como nos exemplos abaixo
"""

canvas = canvas.Canvas("pdfs/extra-030.pdf")

canvas.rect(60,  700, inch, inch, fill=1)
canvas.rect(160, 700, inch + 50, inch + 50, fill=1)

canvas.rect(60,  600, cm, cm, fill=1)
canvas.rect(160, 600, cm - 10, cm - 10, fill=1)

canvas.rect(60,  500, pica, pica, fill=1)
canvas.rect(160, 500, pica / 2, pica / 2, fill=1)

canvas.rect(60,  400, mm, mm, fill=1)
canvas.rect(160, 400, mm * 2, mm * 2, fill=1)

canvas.save()