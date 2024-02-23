def create_email_html(text, filename, align='left'):
    html_content = f"<html><body><p style='text-align: {align};'>{text}</p></body></html>"
    with open(filename, 'w') as file:
        file.write(html_content)
