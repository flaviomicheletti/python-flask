from PIL import Image, ImageDraw

"""

Posicionamento de elementos

"""
img_width  = 300
img_height = 300

im = Image.new("RGB", (img_width, img_height), "white")
draw = ImageDraw.Draw(im)

#
# Dimensões do quadrado
#
rec_x_ini = img_width / 2 - 50
rec_y_ini = img_height / 2 - 50
rec_x_fim = img_width / 2 + 50
rec_y_fim = img_height / 2 + 50

#
# Quadrado central
#
draw.rectangle([rec_x_ini, rec_y_ini, rec_x_fim, rec_y_fim], fill="black", outline="white")

#
# Quadrado superior esquerdo
#
draw.rectangle([img_width - 300, img_height - 300, img_width - 200, img_height - 200], fill="yellow", outline="white")

#
# Quadrado superior direito
#
draw.rectangle([img_width - 100, img_height - 300, img_width, img_height - 200], fill="green", outline="white")

#
# Quadrado central inferior esquerdo
#
draw.rectangle([img_width - 300, img_height - 100, img_width - 200 , img_height], fill="red", outline="white")

#
# Quadrado central inferior direito
#
draw.rectangle([img_width - 100, img_height - 100, img_width, img_height], fill="blue", outline="white")


#
# Desenhando strings
#
draw.text([rec_x_ini + 30,  rec_y_ini - 10],  "cima", fill="black")
draw.text([rec_x_ini - 95,  rec_y_ini + 45],  "esquerda", fill="black")
draw.text([rec_x_ini + 100, rec_y_ini + 45],  "direita", fill="black")
draw.text([rec_x_ini + 30,  rec_y_ini + 100], "baixo", fill="black")


del draw

im.save('imgs/pillow-008.png', "PNG")