from PIL import Image, ImageDraw, ImageFont

"""

Centralizando elementos

"""
img_width  = 300
img_height = 300

im = Image.new("RGB", (img_width, img_height), "white")
draw = ImageDraw.Draw(im)

#
# Centralizando um quandrado 100x100
#
rec_x_ini = img_width  / 2 - 50
rec_y_ini = img_height / 2 - 50
rec_x_fim = img_width  / 2 + 50
rec_y_fim = img_height / 2 + 50
draw.rectangle([rec_x_ini, rec_y_ini, rec_x_fim, rec_y_fim], fill="green", outline="yellow")

#
# Desenhando um círculo dentro do quadrado
#
draw.ellipse([rec_x_ini + 10, rec_y_ini + 10, rec_x_fim - 10, rec_y_fim - 10], fill="blue", outline="black")

del draw

im.save('imgs/pillow-007.png', "PNG")