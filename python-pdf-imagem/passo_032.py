from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.pdfgen import canvas

"""
SimpleDocTemplate.build(canvasmaker=canvas.Canvas)

O parâmetro canvasmaker do `SimpleDocTemplate.build()` por padrão utiliza o objeto `canvas.Canvas`
do `BaseDocTemplate() para criar todos os elementos e configurações do documento.

Para personalizar ou adicionar elementos no documento podemos criar uma nova classe e inicializamos
o objeto `canvas.Canvas` com os atributos do documento atual, assim podemos adicionar na função `save()`
os elementos personalizados no documento.

Trecho da documentação: https://www.reportlab.com/docs/reportlab-reference.pdf
If the canvasmaker argument is provided then it will be used instead of the default.
For example a slideshow might use an alternate canvas which places 6 slides on a page
(by doing translations, scalings and redefining the page break operations).

"""

class ExemploCanvas(canvas.Canvas):
    def __init__(self, * args, ** kwargs):
        # Inicializa o objeto Canvas(self, filename, parâmetros)
        canvas.Canvas.__init__(self, * args, ** kwargs)
        # Cria a list que guarda o estado de cada página do objeto
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total_paginas = len(self._saved_page_states)
        for estado in self._saved_page_states:
            self.__dict__.update(estado)
            self.drawString(100, 700, "Página %d de %d" % (self._pageNumber, total_paginas))
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

doc = SimpleDocTemplate("pdfs/passo-032.pdf")
story  = []

for i in range(10):
    story.append(Spacer(1, 100))

doc.build(story, canvasmaker=ExemploCanvas)