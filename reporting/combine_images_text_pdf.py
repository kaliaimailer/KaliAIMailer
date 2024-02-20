from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import PyPDF2

def create_pdf_with_text_and_images(pdf_filename, text_filename, image_paths):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter
    margin = 72  # Margin for text
    text_height = height - margin  # Start writing text from the top (with some margin)
    min_height_before_page_break = 50  # Minimum height before starting a new page

    with open(text_filename, 'r', encoding='utf-8') as text_file:  # Ensure correct encoding
        for line in text_file:
            if text_height < min_height_before_page_break:
                c.showPage()  # Start a new page
                text_height = height - margin  # Reset text height for the new page
            c.drawString(margin, text_height, line.strip())
            text_height -= 15  # Decrease for next line; adjust as needed

    c.showPage()  # Ensure images start on a new page
    text_height = height - margin  # Reset text height for images

    for image_path in image_paths:
        try:
            image = ImageReader(image_path)
            image_width, image_height = image.getSize()
            aspect_ratio = image_width / image_height
            if text_height - (400 / aspect_ratio) < min_height_before_page_break:
                c.showPage()
                text_height = height - margin
            c.drawImage(image, margin, text_height - (400 / aspect_ratio), width=400, height=400 / aspect_ratio)
            text_height -= 400 / aspect_ratio + 20  # Adjust space for the next image or text
        except Exception as e:
            print(f"Error adding image {image_path}: {e}")

    c.save()

def add_password_to_pdf(input_pdf_path, output_pdf_path, password):
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    pdf_writer = PyPDF2.PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    with open(output_pdf_path, 'wb') as out_pdf_file:
        pdf_writer.write(out_pdf_file)

# Example usage
pdf_filename = "output.pdf"
protected_pdf_filename = "protected_output.pdf"
text_filename = "example.txt"
image_paths = ["image.png"]
password = "Kali@123#*"

create_pdf_with_text_and_images(pdf_filename, text_filename, image_paths)
add_password_to_pdf(pdf_filename, protected_pdf_filename, password)