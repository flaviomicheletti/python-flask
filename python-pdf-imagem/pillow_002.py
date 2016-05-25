from PIL import Image, ImageDraw

"""
Linhas 

https://pillow.readthedocs.org/en/latest/reference/ImageDraw.html#PIL.ImageDraw.PIL.ImageDraw.Draw.line

PIL.ImageDraw.Draw.line(xy, fill=None, width=0)

xy - obrigatório, pode ser uma sequencia [x, y, x1, y1] ou 2 tuplas (x, y, x1, y1)
dica: pense em "início" (x, y) e "fim" (x1, y1)

fill - opcional, cor da linha, pode ser (R, G, B) ou um número inteiro.

width - opcional, expessura da linha, 1 é o menor valor.

"""

im = Image.new("RGB", (210, 210), "black")
draw = ImageDraw.Draw(im)

#
# horizontal
#
draw.line([10, 10, 100, 10])

#
# vertical
#
draw.line((20, 20, 20, 100))


#
# Exemplo mais comum
#
# draw.line((100,200, 150, 300), fill=128, width=3)


#
# Funciona se passarmos só os valores
#
# draw.line((0, 64, 64, 0), 128, 5)


#
# Veja este formato
#
# draw.line((5, 0, 5, 10), (0, 0, 0), 2)


del draw

im.save('imgs/pillow-002.png', "PNG")