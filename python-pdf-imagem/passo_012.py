from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

"""
Utilizando elementos HTML ao inserir um texto com `Paragraph()`

Lista de tags HTML que são aceitos:
<b>, <i>, <u>, <strong>, <strike>, <br/>, <font>, <greek>, <super>, <a>, <img>, <seq>
"""

doc = SimpleDocTemplate("pdfs/passo-012s.pdf")
story  = []
styles = getSampleStyleSheet()


#
# Elementos básicos
#
story.append(Paragraph('<b>Bold</b> <i>Italic</i> <u>Sublinhado</u>', styles["Normal"]))
story.append(Spacer(1,10))

story.append(Paragraph('<strong>Strong</strong> <strike>Strike</strike><br/>Quebra de linha', styles["Normal"]))
story.append(Spacer(1,10))

story.append(Paragraph('<font face="times"color="red">Alterando a fonte</font>', styles["Normal"]))
story.append(Spacer(1,10))

story.append(Paragraph('Equation (&alpha;):<greek>e</greek><super><greek>ip</greek></super>= -1', styles["Normal"]))
story.append(Spacer(1,10))

#
# Link
#
story.append(Paragraph('<a href="http://www.google.com.br" color="blue">Link</a>', styles["Normal"]))
story.append(Spacer(1,10))

#
# Imagem
#
story.append(Paragraph('Imagem inline <img src="static/testimg.gif" valign="top"/>', styles["Normal"]))
story.append(Spacer(1,10))

#
# Sequência
#
story.append(Paragraph('<seq id="spam"/>, <seq id="spam"/>. Reset<seqreset id="spam"/> = <seq id="spam"/>.', styles["Normal"]))
story.append(Spacer(1,10))

doc.build(story)