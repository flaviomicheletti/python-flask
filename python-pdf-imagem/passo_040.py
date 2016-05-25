from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph, Flowable
from reportlab.lib.styles import getSampleStyleSheet

"""
Criando elemento Flowable Customizável

Todos os elementos do módulo platypus herdam da classe Flowable os atributos e funções para desenhar
o elemento no documento seguindo os padrões de margem e posicionamento definidos no SimpleDocTemplate.

Com isso podemos criar elementos customizáveis com o auxilio do canvas e inseri-los no documento.
"""

class TextBox(Flowable):
    def __init__(self, texto="", x=0, y=0, width=200, height=10):
        Flowable.__init__(self)
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height
        self.texto  = texto
        self.styles = getSampleStyleSheet()

    def draw(self):
        self.canv.line(self.x, 0, 400, 0)
        p = Paragraph(self.texto, style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height)
        p.drawOn(self.canv, 0, 0)


doc = SimpleDocTemplate("pdfs/passo-040.pdf")
story  = []
story.append(TextBox("Titulo um"))
story.append(Spacer(0, 10))
story.append(TextBox("Titulo dois"))

doc.build(story)