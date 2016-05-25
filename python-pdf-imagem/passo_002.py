from reportlab.platypus import SimpleDocTemplate, PageBreak

"""

Platypus functions

"""

#
# PageBreak: Quebra de página
#
doc = SimpleDocTemplate("pdfs/passo-002a.pdf")
story = []
story.append(PageBreak())
story.append(PageBreak())
story.append(PageBreak())
story.append(PageBreak())
doc.build(story)