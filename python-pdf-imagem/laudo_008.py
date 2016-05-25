from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Flowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm # 1cm -> 12px
from reportlab.rl_config import defaultPageSize
from reportlab.pdfgen import canvas

from datetime import date

#
# Classe que gera o título do fator com a imagem da pontuação
#
class FatorBox(Flowable):
    def __init__(self, fator=None, style=None, imagem=None, x=0, y=0, width=defaultPageSize[0] - (2 * cm), height=55):
        Flowable.__init__(self)
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height
        self.fator  = fator
        self.style = style
        self.imagem = imagem

    def draw(self):
        p = Paragraph(self.fator, self.style)
        p.wrapOn(self.canv, self.width, self.height)
        p.drawOn(self.canv, 0, 0)

        self.canv.drawImage(self.imagem, 448, -3, width=80, height=36, mask='auto')

#
# Claase que gera a paginação do PDF
#
class Paginacao(canvas.Canvas):
    def __init__(self, * args, ** kwargs):
        canvas.Canvas.__init__(self, * args, ** kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total_paginas = len(self._saved_page_states)
        for estado in self._saved_page_states:
            self.__dict__.update(estado)
            if self._pageNumber != 1:
                self.setFillGray(0.5)
                self.drawString(485, 35, "Página %d de %d" % (self._pageNumber, total_paginas))
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

#
# Classe que gera o PDF
#
class PDF(object):
    def __init__(self):
        self.doc_config = {
            'pagesize':     A4,
            'rightMargin':  cm,
            'leftMargin':   cm,
            'topMargin':    7 * cm,
            'bottomMargin': 2 * cm,
            'title':        "Laudo Plus",
            'author':       "Dom Brasil",
            'subject':      "Laudo",
            'creator':      "Dom Brasil",
            'lang':         "pt-br"
        }
        # O objeto já vem com todos os dados
        self.laudo = {
            'tipo':         "Laudo Plus",
            'nome':         "Deodoro da Fonseca",
            'empresa':      "Recursos de Testes LTDA",
            'cargo':        "Administrador"
        }
        self.arquivo      = "pdfs/laudo-008.pdf"

    def capa(self, canvas, doc):
        cabecalho = Image('static/topFrame.png', 535, 63)
        w, h = cabecalho.wrap(doc.width, doc.topMargin)
        cabecalho.drawOn(canvas, doc.leftMargin + 5, doc.height + doc.topMargin - 40)

        canvas.setFont('Helvetica', 14)
        canvas.setFillColor(HexColor('#3366cc'))
        canvas.drawRightString(560, 220, self.laudo['tipo'])
        canvas.setFont('Helvetica', 10)
        canvas.setFillColor(HexColor('#6a6a6a'))
        canvas.drawRightString(560, 180, self.laudo['nome'])
        canvas.setFillColor(HexColor('#6a6a6a'))
        canvas.drawRightString(560, 160, self.laudo['empresa'])
        canvas.setFillColor(HexColor('#6a6a6a'))
        canvas.drawRightString(560, 140, self.laudo['cargo'])

    def cabecalho(self, canvas, doc):
        cabecalho = Image('static/topFrame.png', 535, 63)
        w, h = cabecalho.wrap(doc.width, doc.topMargin)
        cabecalho.drawOn(canvas, doc.leftMargin + 5, doc.height + doc.topMargin - 40)

    def gerar(self):
        doc = SimpleDocTemplate(self.arquivo, **self.doc_config)
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name="Titulo", parent=styles['Normal'], fontSize=14, textColor=HexColor("#3366cc")))
        styles.add(ParagraphStyle(name="Justificado", parent=styles['Normal'], textColor=HexColor("#505050"), alignment=TA_JUSTIFY, spaceBefore=8, spaceAfter=15))
        styles.add(ParagraphStyle(name="JustificadoBold", parent=styles['Italic'], textColor=HexColor("#505050"), alignment=TA_JUSTIFY, spaceBefore=8, spaceAfter=15, fontSize=8))

        story  = []
        
        # Capa
        story.append(PageBreak())

        # Introdução
        missao = "Velocidade através de diagnósticos, otimização e métricas sobre profissionais e cargos."
        ciclo  = """A presente metodologia tem como objetivo ordenar etapas que facilitem atingir resultados através do
         planejamento estratégico humano. Para tanto consideramos vários itens, desde valores, missão e objetivos macros
         de uma organização, até recompensas por metas atingidas. Estes itens se transformam em elos estratégicos que
         permitem conexão entre estratégia e resultados.<br/><br/>
        Elegemos como pilar fundamental de sustentação o entendimento e diferenciação dos aspectos comportamentais
         dos não comportamentais. Só através deste conhecimento será possível planejar ações de mudanças e desenvolvimento
         prováveis de se concretizarem.<br/><br/>
        Este relatório, de forma alguma, tem a proposta terapêutica ou psicanalítica. Deve ser entendido como a forma
         mais objetiva de comparar características profissionais ao desenho estratégico do cargo assumido ou proposto."""
        eixo_x = """Este eixo se refere a características comportamentais ou habilidades possíveis de serem administradas
         através de gerenciamento.<br/><br/>
        Alguns teóricos fazem referência a estas características chamando-as de atitudes, outros de habilidade e
         outros de aptidão."""
        eixo_y ="""Este eixo se refere a aspectos não comportamentais, tais como formação acadêmica, experiência
         dos profissionais sempre correlacionadas as demandas do cargo. Representa oportunidades de treinamento."""

        story.append(Paragraph("Missão", styles["Titulo"]))
        story.append(Paragraph(missao, styles["Justificado"]))
        story.append(Paragraph("Ciclo", styles["Titulo"]))
        story.append(Paragraph(ciclo, styles["Justificado"]))
        story.append(Paragraph("Eixo X", styles["Titulo"]))
        story.append(Paragraph(eixo_x, styles["Justificado"]))
        story.append(Paragraph("Eixo Y", styles["Titulo"]))
        story.append(Paragraph(eixo_y, styles["Justificado"]))
        story.append(PageBreak())

        # Gráfico
        story.append(Image('static/grafico_linear.png', 240, 280))
        story.append(PageBreak())

        # Fatores
        from fatores import Fatores
        fatores = Fatores()
        for fator in fatores.retornar_fatores():
            story.append(FatorBox(fator['titulo'], styles["Titulo"], 'static/imgPont1.png'))
            story.append(Paragraph("<b>" + fator['alto'] + "</b>", styles["JustificadoBold"]))
            story.append(Paragraph("Texto do laudo", styles["Justificado"]))

        # Assinatura
        story.append(Spacer(1, 60))
        story.append(Paragraph(date.today().strftime("%d/%m/%y"), styles["Justificado"]))
        story.append(Spacer(1, 10))
        story.append(Paragraph("Dom Brasil", styles["Justificado"]))

        doc.build(story, onFirstPage=self.capa, onLaterPages=self.cabecalho, canvasmaker=Paginacao)
