from PIL import Image, ImageDraw

""" baseado neste exemplo http://effbot.org/imagingbook/imagedraw.htm """

#
# https://pillow.readthedocs.org/en/latest/reference/Image.html#PIL.Image.new
#
im = Image.new("RGB", (210, 210), "black")

#
# https://pillow.readthedocs.org/en/latest/reference/ImageDraw.html
#
draw = ImageDraw.Draw(im)

#
# https://pillow.readthedocs.org/en/latest/reference/ImageDraw.html#PIL.ImageDraw.PIL.ImageDraw.Draw.line
#
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

#
# https://pillow.readthedocs.org/en/latest/reference/Image.html#PIL.Image.Image.save
#
im.save('imgs/pillow-001.png', "PNG")