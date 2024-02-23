from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import alignment_module

def create_email_pdf(text, filename, align='left'):
    c = canvas.Canvas(filename, pagesize=letter)
    text_width = c.stringWidth(text, 'Helvetica', 12)
    
    x = alignment_module.get_alignment_coordinates(align, text_width, letter[0])

    c.drawString(x, 720, text)
    c.save()
