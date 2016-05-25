from PIL import Image, ImageDraw, ImageFont

"""
Text

https://pillow.readthedocs.org/en/latest/reference/ImageDraw.html#PIL.ImageDraw.PIL.ImageDraw.Draw.text

PIL.ImageDraw.Draw.text(xy, text, fill=None, font=None, anchor=None)

xy - obrigatório, pode ser uma sequencia [x, y] ou uma tupla (x, y)

fill - opcional, cor da linha, pode ser (R, G, B) ou um número inteiro.

font - opcional, altera a fonte e seu tamanho
"""

im = Image.new("RGB", (210, 210), "black")
draw = ImageDraw.Draw(im)

draw.text([0, 0],  "ImageDraw Text")

draw.text([0, 20], "ImageDraw Text", fill="red")

draw.text([0, 40], "ImageDraw Text", fill="blue", font=None) # Veja mais no próximo exemplo

del draw

im.save('imgs/pillow-005a.png', "PNG")



"""
ImageFont: Alterando a fonte da string

Ao importar o módulo ImageFont para alterar a fonte da string, pode ocorrer o seguinte erro:

    ImportError: The _imagingft C module is not installed

Para corrigir este erro de import acesse o terminal como root e instale a seguinte biblioteca:

    apt-get install libfreetype6-dev

Após a instalação da biblioteca, desinstale e instale novamente o módulo Pillow do seu ambiente:

    pip uninstall Pillow
    pip install Pillow

http://stackoverflow.com/questions/4011705/python-the-imagingft-c-module-is-not-installed

Após a instalação da bibliote o exemplo abaixo funcionará.
"""
im = Image.new("RGB", (210, 210), "black")
draw = ImageDraw.Draw(im)

draw.text([0, 0],  "Fonte Arial, 15", font=ImageFont.truetype("static/arial.ttf", 15))

del draw

im.save('imgs/pillow-005b.png', "PNG")


