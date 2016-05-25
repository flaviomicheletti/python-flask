from laudo_008 import PDF

pdf = PDF()
pdf.doc_config['title'] = "Laudo Express"
pdf.laudo['tipo']       = "Laudo Express"
pdf.laudo['nome']       = "Lucas Andrade"
pdf.arquivo             = "pdfs/laudo-009.pdf"
pdf.gerar()