from PIL import Image, ImageDraw, ImageFont

# Define o tamanho da imagem
size = (300,350)
preto = (0, 0, 0, 255)
cinza = (237, 237, 237, 255)
laranja = (255, 102, 0, 255)
azul_escuro = (0, 51, 102, 255)

# Cria a imagem definindo a paleta de cores e o tamanho
im = Image.new('RGBA', size)

# Cria o objeto de desenho
draw = ImageDraw.Draw(im)   

draw.text((10, 60), "Liderança", fill=preto)
# posição dos eixos 
#
# x0 = ponto inicial da largura
# y0 = ponto inicial da altura
# x1 = ponto final da largura
# y1 = ponto final da altura
#
#               x0   y0  x1   y1
draw.rectangle([130, 50, 280, 310], fill=cinza)

#draw.ellipse([50, 50, 450,450], fill=(0,0,255,255), outline=(0,0,0,255))
#
#draw.line([10,100,100,300], fill=(0,0,0), width=4)
#
#draw.point([50,30,60,40], fill=(0,0,0,255))
#
#draw.rectangle([60,60,120,120], fill=(0,0,0))
#
#
#red = (255,0,0,255)    # color of our text
#text_pos = (20,20) # top-left position of our text
#text = "Hello World!" # text to draw
## Now, we'll do the drawing: 


# Deleta o objeto de desenho
del draw

# Salva a imagem na pasta FilesTemp do servidor
im.save('imgs/grafico-001.png')