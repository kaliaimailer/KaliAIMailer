# Define alignment constants
ALIGN_LEFT = 'left'
ALIGN_CENTER = 'center'
ALIGN_RIGHT = 'right'

# Function to calculate alignment for image and PDF
def get_alignment_coordinates(align, content_width, canvas_width, margin=10):
    """
    Calculate the starting x-coordinate based on alignment.
    :param align: The alignment type (left, center, right)
    :param content_width: The width of the content to align
    :param canvas_width: The width of the canvas or page
    :param margin: Margin for left or right alignment
    :return: The x-coordinate for the starting position of the content
    """
    if align == ALIGN_CENTER:
        return (canvas_width - content_width) / 2
    elif align == ALIGN_RIGHT:
        return canvas_width - content_width - margin
    else:  # Default to left alignment
        return margin
