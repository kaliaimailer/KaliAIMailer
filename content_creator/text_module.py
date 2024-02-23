# Text alignment does not apply to plain text files in a meaningful way, as it depends on the viewer/editor.
def create_email_text(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
