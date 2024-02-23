from PIL import Image, ImageDraw, ImageFont
import alignment_module

def create_email_image(text, filename, align='left'):
    image = Image.new('RGB', (800, 200), color=(255, 255, 255))
    d = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 15)
    textwidth, textheight = d.textsize(text, font)

    x = alignment_module.get_alignment_coordinates(align, textwidth, 800)

    d.text((x, 10), text, fill=(0, 0, 0), font=font)
    image.save(filename)
