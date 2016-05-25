from PIL import Image, ImageDraw

"""
Círculos

https://pillow.readthedocs.org/en/latest/reference/ImageDraw.html#PIL.ImageDraw.PIL.ImageDraw.Draw.ellipse

PIL.ImageDraw.Draw.ellipse(xy, fill=None, outline=None)

xy - obrigatório, pode ser uma sequencia [x, y, x1, y1] ou 2 tuplas (x, y, x1, y1)
dica: pense em "início" (x, y) e "fim" (x1, y1)

fill - opcional, cor da linha, pode ser (R, G, B) ou um número inteiro.

outiline - opcional, cor da linha.

"""

im = Image.new("RGB", (210, 210), "black")
draw = ImageDraw.Draw(im)

draw.ellipse([0, 0, 10, 10],      fill="green", outline="yellow")

draw.ellipse((0, 20) + (10, 30),  fill="green", outline="red")

draw.ellipse(((0, 40), (10, 50)), fill="green", outline="white")

draw.ellipse([0, 60, 10, 70], (0, 255, 0), (0, 0, 255))

del draw

im.save('imgs/pillow-004.png', "PNG")