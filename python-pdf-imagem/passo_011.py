from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT

"""
Através da classe `ParagraphStyle()` é possível incluir estilos além dos estilos embutidos.
A função `.add()` do objeto `getSampleStyleSheet()` é quem adiciona o estilo.

<code>
styles = getSampleStyleSheet()
styles.add(  ParagraphStyle(name='', estilos...)  )
</code>


`ParagraphStyle()` aceita como parâmetros:

    alignment
    allowWidows
    allowOrphans
    bulletAnchor
    backColor
    borderColor
    bulletIndent
    borderWidth
    borderPadding
    borderRadius
    bulletFontName
    bulletFontSize
    endDots
    firstLineIndent
    fontName
    fontSize
    leading
    leftIndent
    rightIndent
    spaceAfter
    spaceBefore
    splitLongWords
    underlineProportion
    wordWrap
    textColor
    textTransform
    parent

"""

doc = SimpleDocTemplate("pdfs/passo-011.pdf")
story  = []
styles = getSampleStyleSheet()

texto = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. \
Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, \
pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, \
vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis \
pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo \
ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, """

styles.add(ParagraphStyle(name='parag-base', spaceBefore=20))
styles.add(ParagraphStyle(name='parag-1', alignment=TA_LEFT,    parent=styles["parag-base"]))
styles.add(ParagraphStyle(name='parag-2', alignment=TA_CENTER,  parent=styles["parag-base"]))
styles.add(ParagraphStyle(name='parag-3', alignment=TA_RIGHT,   parent=styles["parag-base"]))
styles.add(ParagraphStyle(name='parag-4', alignment=TA_JUSTIFY, parent=styles["parag-base"]))

story.append(Paragraph(texto, styles["parag-1"]))
story.append(Paragraph(texto, styles["parag-2"]))
story.append(Paragraph(texto, styles["parag-3"]))
story.append(Paragraph(texto, styles["parag-4"]))

doc.build(story)