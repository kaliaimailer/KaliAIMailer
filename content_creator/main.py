import image_module
import pdf_module
import text_module
import html_module
import alignment_module  # Ensure this is imported if needed for direct usage or reference

def generate_email_content(text, format_type, align):
    filename = f"email_content.{format_type}"
    if format_type == "jpg":
        image_module.create_email_image(text, filename, align)
    elif format_type == "pdf":
        pdf_module.create_email_pdf(text, filename, align)
    elif format_type == "txt":
        text_module.create_email_text(text, filename)  # Alignment not applied but kept for consistency
    elif format_type == "html":
        html_module.create_email_html(text, filename, align)
    else:
        print("Unsupported format.")

if __name__ == "__main__":
    text = input("Enter the email content: ")
    format_type = input("Enter the format (jpg, pdf, txt, html): ").lower()
    align = input("Enter alignment (left, center, right): ").lower()
    generate_email_content(text, format_type, align)
