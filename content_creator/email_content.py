import pdfkit
from PIL import Image
import os

def html_to_jpg(html_file_path, output_image_path):
    # Convert HTML to JPG using wkhtmltoimage (part of wkhtmltopdf)
    # Ensure wkhtmltoimage is installed and accessible in the system's PATH.
    command = f"wkhtmltoimage --format jpg {html_file_path} {output_image_path}"
    os.system(command)

def jpg_to_pdf(jpg_file_path, output_pdf_path):
    # Convert JPG to PDF using Pillow
    image = Image.open(jpg_file_path)
    # Convert image to RGB, in case it's in a different mode (e.g., RGBA)
    rgb_im = image.convert('RGB')
    rgb_im.save(output_pdf_path)

# Example usage
html_file = "D:/WorkSpace/2023/February/28 February/html_code.html"  # Path to your HTML file
jpg_file = "output.jpg"     # Desired JPG output file path
pdf_file = "output.pdf"     # Desired PDF output file path

html_to_jpg(html_file, jpg_file)
jpg_to_pdf(jpg_file, pdf_file)
