from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

"""
Paragraph() & getSampleStyleSheet()

Para inserir um parágrafo no documento utilizamos a classe `Paragraph(str, StyleSheet)`.
Os  parâmetros aceitos são:

str:        Texto no formato string
StyleSheet: Estilo da fonte

A classe `Paragraph()` trabalha sempre em conjunto com a classe `getSampleStyleSheet()`, uma vez
que ao inserimos um texto no documento é preciso definir o seu o estilo de fonte.
"""

#
# Ao instânciar a classe `getSampleStyle() podemos utilizar os estilos embutidos do reportlab.
#
doc = SimpleDocTemplate("pdfs/passo-010a.pdf")
story = []
styles = getSampleStyleSheet()
story.append(Paragraph('Exemplo de parágrafo com o estilo Normal da fonte', styles["Normal"]))
doc.build(story)



#
# Estilos por apelidos
#
doc = SimpleDocTemplate("pdfs/passo-010b.pdf")
story  = []
styles = getSampleStyleSheet()
story.append(Paragraph('Title',      styles["title"]))
story.append(Paragraph('Heading1',   styles["h1"]))
story.append(Paragraph('Heading2',   styles["h2"]))
story.append(Paragraph('Heading3',   styles["h3"]))
story.append(Paragraph('Heading4',   styles["h4"]))
story.append(Paragraph('Heading5',   styles["h5"]))
story.append(Paragraph('Heading6',   styles["h6"]))
story.append(Paragraph('Bullet',     styles["bu"]))
story.append(Paragraph('Definition', styles["df"]))
doc.build(story)



#
# Estilos por nome
#
doc = SimpleDocTemplate("pdfs/passo-010c.pdf")
story  = []
styles = getSampleStyleSheet()
story.append(Paragraph('Title',      styles["Title"]))
story.append(Paragraph('Heading1',   styles["Heading1"]))
story.append(Paragraph('Heading2',   styles["Heading2"]))
story.append(Paragraph('Heading3',   styles["Heading3"]))
story.append(Paragraph('Heading4',   styles["Heading4"]))
story.append(Paragraph('Heading5',   styles["Heading5"]))
story.append(Paragraph('Heading6',   styles["Heading6"]))
story.append(Paragraph('Bullet',     styles["Bullet"]))
story.append(Paragraph('Definition', styles["Definition"]))
story.append(Paragraph('Normal',     styles["Normal"]))
story.append(Paragraph('Italic',     styles["Italic"]))
story.append(Paragraph('BodyText',   styles["BodyText"]))
story.append(Paragraph('Code',       styles["Code"]))
doc.build(story)