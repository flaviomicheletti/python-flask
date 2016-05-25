from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm # 1cm -> 12px

doc_config = {
    'pagesize':     A4,
    'rightMargin':  1 * cm,
    'leftMargin':   1 * cm,
    'topMargin':    12 * cm,
    'bottomMargin': 2 * cm,
    'title':        "Laudo Plus",
    'author':       "Dom Brasil",
    'subject':      "Laudo",
    'creator':      "Dom Brasil",
    'lang':         "pt-br"
}

def cabecalho(canvas, doc):
    cabecalho = Image('static/topFrame.png', 535, 63)
    w, h = cabecalho.wrap(doc.width, doc.topMargin)
    cabecalho.drawOn(canvas, doc.leftMargin + 5, doc.height + doc.topMargin - 40)

doc = SimpleDocTemplate("pdfs/laudo-002.pdf", **doc_config)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Titulo", parent=styles['Heading2'], textColor=HexColor("#3366cc"), alignment=TA_RIGHT))
styles.add(ParagraphStyle(name="SubTitulo", parent=styles['Normal'], textColor=HexColor("#6a6a6a"), alignment=TA_RIGHT))

Story  = []
Story.append(Spacer(1, 8 * cm))
Story.append(Paragraph("Laudo Plus", styles["Titulo"]))
Story.append(Spacer(1, 20))
Story.append(Paragraph("Deodoro Sampaio", styles["SubTitulo"]))
Story.append(Spacer(1, 10))
Story.append(Paragraph("Empresa", styles["SubTitulo"]))
Story.append(Spacer(1, 10))
Story.append(Paragraph("Cargo", styles["SubTitulo"]))
Story.append(PageBreak())

doc.build(Story, onFirstPage=cabecalho, onLaterPages=cabecalho)
