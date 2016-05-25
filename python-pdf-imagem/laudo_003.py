from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm # 1cm -> 12px

doc_config = {
    'pagesize':     A4,
    'rightMargin':  1 * cm,
    'leftMargin':   1 * cm,
    'topMargin':    7 * cm,
    'bottomMargin': 2 * cm,
    'title':        "Laudo Plus",
    'author':       "Dom Brasil",
    'subject':      "Laudo",
    'creator':      "Dom Brasil",
    'lang':         "pt-br",
    'laudo':        "Laudo Plus",
    'nome':         "Deodoro da Fonseca",
    'empresa':      "Recursos de Testes LTDA",
    'cargo':        "Administrador"
}

def capa(canvas, doc):
    cabecalho = Image('static/topFrame.png', 535, 63)
    w, h = cabecalho.wrap(doc.width, doc.topMargin)
    cabecalho.drawOn(canvas, doc.leftMargin + 5, doc.height + doc.topMargin - 40)

    canvas.setFont('Helvetica', 14)
    canvas.setFillColor(HexColor('#3366cc'))
    canvas.drawRightString(560, 220, doc_config['laudo'])
    canvas.setFont('Helvetica', 10)
    canvas.setFillColor(HexColor('#6a6a6a'))
    canvas.drawRightString(560, 180, doc_config['nome'])
    canvas.setFillColor(HexColor('#6a6a6a'))
    canvas.drawRightString(560, 160, doc_config['empresa'])
    canvas.setFillColor(HexColor('#6a6a6a'))
    canvas.drawRightString(560, 140, doc_config['cargo'])

def cabecalho(canvas, doc):
    cabecalho = Image('static/topFrame.png', 535, 63)
    w, h = cabecalho.wrap(doc.width, doc.topMargin)
    cabecalho.drawOn(canvas, doc.leftMargin + 5, doc.height + doc.topMargin - 40)

doc = SimpleDocTemplate("pdfs/laudo-003.pdf", **doc_config)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Titulo", parent=styles['Normal'], fontSize=14, textColor=HexColor("#3366cc")))
styles.add(ParagraphStyle(name="Justificado", parent=styles['Normal'], textColor=HexColor("#505050"), alignment=TA_JUSTIFY, spaceBefore=8, spaceAfter=15))
styles.add(ParagraphStyle(name="JustificadoBold", parent=styles['Normal'], textColor=HexColor("#505050"), alignment=TA_JUSTIFY))

story  = []
story.append(PageBreak())

doc.build(story, onFirstPage=capa, onLaterPages=cabecalho)
