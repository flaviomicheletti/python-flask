from reportlab.pdfgen import canvas

"""
Canvas imagem

canvas.drawImage(self, image, x, y, width=None, height=None, mask=None)
canvas.drawInlineImage(self, image, x, y, width=None, height=None)

There are two similar-sounding ways to draw images. The preferred one is the drawImage method. This implements 
a caching system so you can define an image once and draw it many times; it will only be stored once in the PDF 
file. `drawImage` also exposes one advanced parameter, a transparency mask, and will expose more in future. 
The older technique, `drawInlineImage`, stores bitmaps within the page stream and is thus very inefficient if you
use the same image more than once in a document; but can result in PDFs which render faster if the images are 
very small and not repeated.
"""

canvas = canvas.Canvas("pdfs/extra-011.pdf")

canvas.drawImage("static/python-logo.png", 100,400, width=150, height=150, mask='auto')

canvas.drawInlineImage("static/python-logo.png", 100, 700)

canvas.showPage()

canvas.save()