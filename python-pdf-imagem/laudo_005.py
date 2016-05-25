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

doc = SimpleDocTemplate("pdfs/laudo-005.pdf", **doc_config)
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
Este relatório, de forma alguma, tem a proposta terapêutica ou psicanalítica. Deve ser entendido como a
 forma mais objetiva de comparar características profissionais ao desenho estratégico do cargo assumido ou proposto."""
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
    story.append(Paragraph(fator['titulo'], styles["Titulo"]))
    story.append(Paragraph("<b>" + fator['alto'] + "</b>", styles["JustificadoBold"]))

doc.build(story, onFirstPage=capa, onLaterPages=cabecalho)
