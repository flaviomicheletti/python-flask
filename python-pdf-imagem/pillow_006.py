from PIL import Image, ImageDraw

"""
Multiline Text

https://pillow.readthedocs.org/en/latest/reference/ImageDraw.html#PIL.ImageDraw.PIL.ImageDraw.Draw.multiline_text

PIL.ImageDraw.Draw.multiline_text(xy, text, fill=None, font=None, anchor=None, spacing=0, align="left")

xy - obrigatório, pode ser uma sequencia [x, y] ou uma tupla (x, y)

fill - opcional, cor da linha, pode ser (R, G, B) ou um número inteiro.

font - opcional, altera a fonte e seu tamanho

spacing - opcional, espaçamento entre as linhas

align - opcional, alinhamento do texto: left, center, right
"""

im = Image.new("RGB", (310, 310), "white")
draw = ImageDraw.Draw(im)

texto1 = """Lorem ipsum dolor sit,"""

texto2 = """Lorem ipsum dolor sit,
consectetuer adipiscing elit."""

#
# Espaçamento entre linhas
#
draw.multiline_text([30, 0],   texto2, fill="blue", spacing=10)

draw.multiline_text([30, 40],  texto2, fill="blue", spacing=2)

#
# O alinhamento não é utilizado em texto de apenas uma linha...
#
draw.multiline_text([30, 80],  texto1, fill="green")

draw.multiline_text((30, 100), texto1, fill="green", align="center")

draw.multiline_text((30, 120), texto1, fill="green", align="right")

#
# Sendo só é perceptivel em texto de duas ou mais linhas
#
draw.multiline_text([30, 150], texto2, fill="red")

draw.multiline_text((30, 190), texto2, fill="red", align="center")

draw.multiline_text((30, 230), texto2, fill="red", align="right")

del draw

im.save('imgs/pillow-006.png', "PNG")