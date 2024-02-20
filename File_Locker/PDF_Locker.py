import PyPDF2

def add_password_to_pdf(input_pdf_path, output_pdf_path, password):
    # Create a PdfFileReader object
    pdf_reader = PyPDF2.PdfReader(input_pdf_path)
    
    # Create a PdfFileWriter object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Add all pages to the writer object from the reader object
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
    # Add a password to the PDF
    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
    
    # Write out the new PDF
    with open(output_pdf_path, 'wb') as out_pdf_file:
        pdf_writer.write(out_pdf_file)

# Example usage
input_pdf = "AI.pdf"
output_pdf = "kali_protected.pdf"
password = "Kali@123#*"

add_password_to_pdf(input_pdf, output_pdf, password)
